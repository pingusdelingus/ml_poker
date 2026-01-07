struct PokerPolicy : torch::nn::Module {
    RecurrentVAE vae{nullptr};
    torch::nn::Linear fc1{nullptr}, fc2{nullptr}, fc_action{nullptr};

    PokerPolicy(int game_state_dim, int history_dim, int z_dim) 
        : vae(history_dim, 64, z_dim) { // Initialize VAE submodule
        
        register_module("vae", vae);
        
        // Policy Input: Game State + Latent Context (z)
        fc1 = register_module("fc1", torch::nn::Linear(game_state_dim + z_dim, 128));
        fc2 = register_module("fc2", torch::nn::Linear(128, 64));
        fc_action = register_module("fc_action", torch::nn::Linear(64, 3)); // Fold, Call, Raise
    }

    torch::Tensor forward(torch::Tensor game_state, torch::Tensor opponent_history) {
        // 1. Get the "Vibe" of the opponent
        // We only need 'z' here, ignore reconstruction
        auto vae_out = vae.forward(opponent_history);
        torch::Tensor z = std::get<3>(vae_out); 
        
        // 2. Detach z? 
        // CRITICAL RESEARCH DECISION: 
        // If you detach(), VAE trains only on reconstruction loss (Unsupervised).
        // If you don't detach, VAE also learns to optimize for winning (End-to-End).
        // For "pure" opponent modeling, detaching is often safer.
        z = z.detach(); 

        // 3. Combine State + Context
        auto combined = torch::cat({game_state, z}, 1);
        
        auto x = torch::relu(fc1->forward(combined));
        x = torch::relu(fc2->forward(x));
        return torch::softmax(fc_action->forward(x), 1);
    }
};
