#include <vector>
#include <memory>
#include <iostream>
#include <utility> 

// enum for the street to keep track of when the action happened
enum class Street
  {
    PREFLOP,
    FLOP,
    TURN,
    RIVER
  };// end of Street


// struct to hold a single action
struct Action
  {
    int playerID;
    float betSize; // 0 for check/fold
    bool isFold;
    bool isAggressive; // true if bet or raise
    Street street;
  };// end of Action


class HandHistory
  {
  private:
    std::vector<std::shared_ptr<Action>> historyLog;

 
public:
  HandHistory()
      {
        // An average hand rarely goes over 20 actions
        historyLog.reserve(20);
      }// end of constructor

    void addAction(int playerID, float amount, bool isFold, Street currentStreet)
      {
        std::shared_ptr<Action> newAction = std::make_shared<Action>();
        newAction->playerID = playerID;
        newAction->betSize = amount;
        newAction->isFold = isFold;
        newAction->street = currentStreet;

        // Determine if this is an aggressive action (bet > 0 and not a fold)
        if (amount > 0.0f && !isFold){
          newAction->isAggressive = true;
        }
        else{
          newAction->isAggressive = false;
        }

        historyLog.push_back(std::move(newAction));
      }// end of addAction


    // helper to get the history for the VAE input
    std::vector<std::shared_ptr<Action>> getLog() const
      {
        // returns a copy of the vector 
        return historyLog;
      }// end of getLog


    void printHistory() const
      {
        if (historyLog.empty()){
          std::cout << "History is empty.\n";
          return;
        }
        else{
          for (size_t i = 0; i < historyLog.size(); ++i){
            std::cout << "Player " << historyLog[i]->playerID 
                      << " Bet: " << historyLog[i]->betSize 
                      << " on Street: " << static_cast<int>(historyLog[i]->street) << "\n";
          }
        }
      }// end of printHistory


    void clearHistory()
      {
        historyLog.clear();
      }// end of clearHistory

  };// end of HandHistory
