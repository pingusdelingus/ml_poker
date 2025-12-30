#include "./Card.cpp"
#include <assert.h>
#include <random>
#define DECK_LENGTH 52
#define RIFFLE_NUM 2


std::random_device rd;
std::mt19937 gen(rd());

class Deck
{
public:
  std::shared_ptr<Card> arr[52];
  int currIndex;
  int numRemaining;
  float pctFull;

  std::string toString()
  {

      std::string ans = "Num Cards Remaining : " + std::to_string(numRemaining) + "\n";
      ans += "Percent Full : " + std::to_string(pctFull) + "\n";
    printDeck();
      return ans;

  }// end of toString

bool isEmpty(){
  return 0 == numRemaining;
  }

  std::shared_ptr<Card> deal()
  {

    if (isEmpty()){
      std::cout << "deck is empty! \n";
      return nullptr;
    }
    
    assert(arr[currIndex] != nullptr); 

  std::shared_ptr<Card> ans = std::move(arr[currIndex]);
    arr[currIndex] = nullptr;
    currIndex++;
    numRemaining--;
    pctFull = static_cast<float> (numRemaining ) / DECK_LENGTH;

   return ans; 

  }// end of deal

  Deck()
  {
    std::string suits[4] = {"Hearts", "Spades", "Clubs", " Diamonds"};

    for (int i = 0; i < 4; i++){
      for (int j = 0; j < 13; j++){
        int index = (i * 13) + j;
        arr[index] = std::make_shared<Card>(j+2, suits[i]);
      }
    }
    std::cout << " added all cards to arr " << "\n";
    currIndex = 0;
    numRemaining = 52;
    pctFull = (float) numRemaining / (float) DECK_LENGTH;

    std::cout << " entering shuffle \n";
    shuffle();
    // assert that cards are shuffled

  }// end of constructor

void riffle(){
    std::cout << "start of a riffle \n";
    int selectIndex = DECK_LENGTH / 2;
    
  std::uniform_int_distribution<> upper (selectIndex, DECK_LENGTH - 1);
  std::uniform_int_distribution<> lower (0, selectIndex - 1);


    int mid = selectIndex;
    for (int i = 0; i < mid; i++){

  int choice_upper = upper(gen);
  int choice_lower = lower(gen); 

      swap(arr, choice_upper, choice_lower );

    }

    std::cout << "end of riffle \n"; 

  }// end of riffle

void swap(std::shared_ptr<Card> * arr, int i1, int i2)
  {

    auto tmp = arr[i1];

    arr[i1] = arr[i2];
    arr[i2] = tmp;

//arr[i1]->number = arr[i1]->number ^ arr[i2]->number;
//arr[i2]->number = arr[i1]->number ^ arr[i2]->number;
//arr[i1]->number = arr[i1]->number^ arr[i2]->number;

  }// end of swap 

void slideArr(int slideIndex)
  {
    int tmpIndex = (slideIndex - 1) % DECK_LENGTH;
 
    std::shared_ptr<Card> tmp = arr[tmpIndex];
    arr[tmpIndex] = arr[(tmpIndex + 1) % DECK_LENGTH];

    arr[slideIndex] = arr[(slideIndex + 1) % DECK_LENGTH];

      //slide over now 
    int i = 0;
    for (i = 0; i < slideIndex - 2; i++){
      arr[i] = arr[i + 1];

    }
    arr[i] = tmp;

  }// end of slideArr


void cut ()
{
  int lb = DECK_LENGTH / 3;
  std::uniform_int_distribution<> upper (lb,  2 * lb);
int i = upper(gen);
  slideArr(i);

}// end of cut 

void printDeck()
{
    for (int i = 0; i < DECK_LENGTH; i++){
      if (arr[i] != NULL){
      
      std::cout << arr[i]->toString() << "\n";
        }

    }

  }// end of printDeck

  void shuffle()
  {
    for (int i = 0 ; i < RIFFLE_NUM; i++){ riffle(); }
    cut();

    for (int i = 0 ; i < RIFFLE_NUM; i++){ riffle(); }
    cut();

  }// end of shuffle

};// end of Deck class
