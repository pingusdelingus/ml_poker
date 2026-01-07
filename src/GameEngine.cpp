#include <vector>
#include <memory>
#include <iostream>

class Player;
class Deck;
class HandHistory;

class GameEngine
  {
  private:
    std::shared_ptr<Deck> deck;
    std::vector<std::shared_ptr<Player>> players;
    std::shared_ptr<HandHistory> currentHistory;
    float potSize;

  public:
    GameEngine()
      {
        potSize = 0.0f;
        // Initialize deck and history...
      }// end of constructor

    // The main loop that runs a single hand from start to finish
    void playHand()
      {
        // 1. Setup
        resetGame();
        dealPreflop();

        // 2. Betting Rounds (Preflop, Flop, Turn, River)
        // We iterate through streets
        for (int street = 0; street < 4; ++street){
          bool roundComplete = false;
          while (!roundComplete){
            // Get current player
            int playerIdx = getNextPlayerIndex();
            std::shared_ptr<Player> activePlayer = players[playerIdx];

            // ASK THE BOT FOR A MOVE
            // This is where your VAE/RL model gets queried
            // We pass the history so the VAE can "read" the table
            int action = activePlayer->decideAction(currentHistory);

            // Execute the move (update pot, history, player stack)
            processAction(playerIdx, action);

            // Check if betting round is over
            if (isRoundComplete()){
              roundComplete = true;
            }
          }

          // Deal community cards if not River
          if (street < 3){
            dealCommunityCards();
          }
        }
        
        // 3. Showdown
        resolveWinner();
      }// end of playHand

    void processAction(int playerIdx, int action)
      {
        // Update the HandHistory object here
        // Update potSize
        // Validates if the move is legal (e.g., cannot raise if stack is 0)
      }// end of processAction

    bool isRoundComplete()
      {
        // Logic to check if everyone has acted and bets match
        return false; // placeholder
      }// end of isRoundComplete

    void resetGame()
      {
        potSize = 0.0f;
        if (currentHistory != nullptr){
          currentHistory->clearHistory();
        }
      }// end of resetGame
      
     // ... helper functions like dealPreflop, getNextPlayerIndex
  };// end of GameEngine
