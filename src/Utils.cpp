torch::Tensor encodeHistory(const std::shared_ptr<HandHistory>& history)
  {
    std::vector<float> flattenedData;
    std::vector<std::shared_ptr<Action>> logs = history->getLog();

    // Iterate and normalize data
    for (size_t i = 0; i < logs.size(); ++i){
      std::shared_ptr<Action> act = logs[i];
      
      // Feature 1: Bet Size (Normalized by Big Blind or Pot)
      flattenedData.push_back(act->betSize / 100.0f); 

      // Feature 2: Is Aggressive? (0.0 or 1.0)
      if (act->isAggressive){
        flattenedData.push_back(1.0f);
      }
      else{
        flattenedData.push_back(0.0f);
      }
      
      // ... Add more features like Street, Player Position, etc.
    }

    // Pad with zeros if history is shorter than max sequence length (e.g. 20)
    // RNNs usually expect fixed sequence lengths in batches
    while (flattenedData.size() < 20 * 5) { // Assuming 5 features per action
        flattenedData.push_back(0.0f);
    }

    // Convert C++ vector to Tensor
    // Shape: (1, SequenceLength, FeatureCount)
    torch::Tensor t = torch::from_blob(flattenedData.data(), 
        {1, 20, 5}, 
        torch::kFloat32);

    // Clone it because from_blob does not take ownership of the memory
    return t.clone(); 
  }// end of encodeHistory
