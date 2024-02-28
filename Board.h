//=======================================================================
// Matt Kretchmar
// February 2024
// Board.h
//
// This file contains a class definition for manipulating boards in the
// RushHour game.
//
// See Config0, Config1, and Config2 for example input files containing
// RushHour game boards.  Briefly, we use the letters A..P to represent
// the cars.
// Car A is the red "goal" car.
// Colors A..L are 2-space cars
// Colors M..P are 3-space trucks
// color key here:
// A: red   B: pink     C: light blue  D: green    E: forrest
// F: lime  G: black    H: orange      I: tan      J: yellow
// K: brown L: purple   M: gold        N: violet   O: sea green   P: blue
//
// A board is typically created with a blank constructor.
// The cin >> friend method will read a board from stdin of the format shown
//	in the Config files.  The cout >> prints the boards in the same format.
// operator== and operator= are included so that the HashTable class can
//	call them for hashing purposes.
// getHashValue should return the hash value.  This is the method you will
//	need to write (actually three of them).  The integer argument
//	as input should be the hash table size.
//=======================================================================
#ifndef _BOARD_H
#define _BOARD_H
#include <iostream>
using namespace std;

#define BOARD_SIZE 6
class Board
{
public:
            Board             ( void );
            Board             ( const Board &b );
            ~Board            ( void );
   Board    operator=         ( const Board &board );
   int      getHashValue      ( int numHashSlots ) const;
   bool     operator==        ( const Board &b ) const;

   friend   ostream & operator<< ( ostream &os, const Board &b );
   friend   istream & operator>> ( istream &is, Board &b );

private:
   unsigned char board[BOARD_SIZE][BOARD_SIZE];
   // feel free to add any private methods you think may be helpful
   // for your hash functions.
};

#endif
