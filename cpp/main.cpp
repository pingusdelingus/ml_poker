#include <iostream>
#include <cstdlib>
#include "./Card.cpp"
#include "./Deck.cpp"

Deck allocate_deck();

std::string usr_choices[3] = {"(S)tand", "(H)it", "(D)ouble Down"};

void finish_hand(){
  std::cout << "hand done! \n" ;
}

void blackjack(Deck * d)
{
    char usrChoice = 'a';
  std::cout << usr_choices[0] << ", " << usr_choices[1] << ", " << usr_choices[2] << "\n";
  std::cin >> usrChoice ;

usrChoice = toupper(usrChoice);

  switch (usrChoice){
    case 'S':
    finish_hand();
    break;

    case 'H':
      std::cout << "dealing : " << d->deal()->toString() << "\n";
      break;

    case 'D':
      std::cout << "dealing : " << d->deal()->toString() << "\n";
      break;
  }


}// end of blackjack

int main(void)
{
 // Card * c = new Card(10, "Spades");


  //std::cout << c->toString() <<  "\n";


  Deck* d = new Deck();

  std::cout << "finished initializing deck \n";

//  d->printDeck();

//  std::cout << d->toString() << "\n";
 
  blackjack(d);

  
return 0;
}// end of main
