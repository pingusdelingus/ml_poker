#include "./Card.cpp"
#include <memory>
#define MAX_HAND_SIZE 25


class Hand{

public:
  
  std::shared_ptr<Card>arr [MAX_HAND_SIZE];
  int currIndex = 0;
  int length;
    
void getCard(std::shared_ptr<Card> newCard)
  {
    if (arr[currIndex] == nullptr){
      arr[currIndex] = std::move(newCard);
      return;
    } 
    else{
      std::cout << "theres a problem in getCard for " << this << " \n";
    }
      
  }

  Hand(){
  for (int i = 0; i < MAX_HAND_SIZE; i++){
      arr[i] = nullptr;
    }
    currIndex = 0;
    length = MAX_HAND_SIZE;
  }// end of default constructor


  Hand(std::shared_ptr<Card>*  ptr, int len){
   
    // should check for length errors
    if (len > MAX_HAND_SIZE) return;

    length = len;
    for (int i = 0; i < length ; i++){
      if (ptr[i] != nullptr){
      
        arr[i] = std::move(ptr[i]); // could also call copy constructor with assignment op. but this is safer
      
      }

    }// end of for

  }// end of Hand constructor

  std::string poker_score(Hand* community_cards){
    

    for (int i = 0;  i < length; i ++){
          
      
    }// end of for
  return std::string("");
  }

  int bj_score(){
    int result = 0;
    
    for (int i = 0; i < length; i++){
  
      result += arr[i]->getNumValue(); 

    }// end of for

    return result;
  }// end of bj_score

}; // end of Hand
