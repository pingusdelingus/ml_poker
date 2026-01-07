CC=g++

CFLAGS = -Wall -O3 -Werror



main: main.o Card.o Hand.o Deck.o
	$(CC) $(CFLAGS) -o main main.o Card.o Hand.o Deck.o

# Individual object files
main.o: main.cpp 
	$(CC) $(CFLAGS) -c main.cpp

Card.o: Card.cpp 
	$(CC) $(CFLAGS) -c Card.cpp

Hand.o: Hand.cpp 
	$(CC) $(CFLAGS) -c Hand.cpp

Deck.o: Deck.cpp 
	$(CC) $(CFLAGS) -c Deck.cpp

clean:
	rm -f *.o main
