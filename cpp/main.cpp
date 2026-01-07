#include <iostream>
#include <cstdlib>
#include "./Card.cpp"
#include "./Deck.cpp"
#include "./Hand.cpp"


Deck allocate_deck();

std::string usr_choices[3] = {"(S)tand", "(H)it", "(D)ouble Down"};

void finish_hand(){
  std::cout << "hand done! \n" ;
}

void blackjack(Deck * d)
{
  int playerValue = 0;
  char usrChoice = 'a';
  std::cout << usr_choices[0] << ", " << usr_choices[1] << ", " << usr_choices[2] << "\n";
  std::cin >> usrChoice ;

  Hand* player = new Hand();
  Hand* house = new Hand();

  player->getCard(d->deal());
  house->getCard(d->deal());
  player->getCard(d->deal());
  house->getCard(d->deal());

usrChoice = toupper(usrChoice);
while (usrChoice != 'S' || playerValue <= 21)
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
