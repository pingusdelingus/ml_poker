#ifndef CARD_HEADER
#define CARD_HEADER
#include <iostream>
#include <string>


class Card{

public:
  std::string number;
  std::string suit;

  Card(int num, std::string s)
  {
    if (num >= 2 && num <= 10){
    number = std::to_string(num);
    }
    else{
    switch(num){
      case 11:
      number = std::string("Jack");
      break;
      case 12:
      number = std::string("Queen");
      break;
      case 13:
      number = std::string("King");
      break;
      case 14:
      number = std::string("Ace");
      break;
      default:
      std::cout << "problem while constructing a card with : " << num << std::endl;
      break;
    }// end of swtich

    }// end of else

    suit = s; // this should call the copy constructor for a std::string
    // don't use strncpy() above
  }// end of constructor

  int getNumValue(){
    return std::stoi(number); // like atoi but for std::string's 
  }

  std::string toString()
  {
    std::string ans = number + " of " ;
    return ans + suit;
  }// end of toString

};

#endif
