#include <torch/torch.h>

struct RecurrentVAE : torch::nn::Module {
    torch::nn::LSTM encoder_lstm{nullptr};
    torch::nn::Linear fc_mu{nullptr}, fc_logvar{nullptr};
    torch::nn::Linear decoder_input{nullptr};
    torch::nn::LSTM decoder_lstm{nullptr};
    torch::nn::Linear fc_out{nullptr};
    
    int hidden_size;
    int latent_dim;

    RecurrentVAE(int input_dim, int hidden_dim, int z_dim) 
        : hidden_size(hidden_dim), latent_dim(z_dim) {
        
        // ENCODER: Compresses time-series data (History)
        encoder_lstm = register_module("encoder_lstm", 
            torch::nn::LSTM(torch::nn::LSTMOptions(input_dim, hidden_dim).batch_first(true)));
            
        // LATENT SPACE: Maps LSTM output to Normal Distribution parameters
        fc_mu = register_module("fc_mu", torch::nn::Linear(hidden_dim, z_dim));
        fc_logvar = register_module("fc_logvar", torch::nn::Linear(hidden_dim, z_dim));

        // DECODER: Tries to reconstruct the history from 'z' (ensures 'z' is meaningful)
        decoder_input = register_module("decoder_input", torch::nn::Linear(z_dim, hidden_dim));
        decoder_lstm = register_module("decoder_lstm", 
            torch::nn::LSTM(torch::nn::LSTMOptions(hidden_dim, hidden_dim).batch_first(true)));
        fc_out = register_module("fc_out", torch::nn::Linear(hidden_dim, input_dim));
    }

    torch::Tensor reparameterize(torch::Tensor mu, torch::Tensor logvar) {
        if (is_training()) {
            auto std = torch::exp(0.5 * logvar);
            auto eps = torch::randn_like(std);
            return mu + eps * std;
        }
        return mu; // Deterministic during inference
    }

    // Forward pass returns {Reconstruction, Mu, LogVar, Z}
    std::tuple<torch::Tensor, torch::Tensor, torch::Tensor, torch::Tensor> forward(torch::Tensor x) {
        // x shape: (Batch, SequenceLength, Features)
        
        // 1. Encode
        torch::Tensor _, hidden_state; 
        std::tie(_, hidden_state) = encoder_lstm->forward(x);
        // Take the last hidden state of the LSTM
        auto last_hidden = hidden_state.get<0>().squeeze(0); 
        
        // 2. Latent Space
        auto mu = fc_mu->forward(last_hidden);
        auto logvar = fc_logvar->forward(last_hidden);
        auto z = reparameterize(mu, logvar);
        
        // 3. Decode (Reconstruct the sequence)
        auto dec_start = decoder_input->forward(z).unsqueeze(1).repeat({1, x.size(1), 1});
        auto decoded_out = decoder_lstm->forward(dec_start).get<0>();
        auto recon_x = fc_out->forward(decoded_out);

        return {recon_x, mu, logvar, z};
    }
};
