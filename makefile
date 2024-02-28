all: hash1 hash2 hash3 sampleRead

sampleRead: sampleRead.cpp Board.h Board.cpp
	g++ -o sampleRead sampleRead.cpp Board.cpp
	
hash3: main.cpp Board.h Board.cpp Hash.h Hash.cpp List.h List.cpp
	g++ -o hash3 -DHASHFUNCTION3 main.cpp Board.cpp

hash2: main.cpp Board.h Board.cpp Hash.h Hash.cpp List.h List.cpp
	g++ -o hash2 -DHASHFUNCTION2 main.cpp Board.cpp

hash1: main.cpp Board.h Board.cpp Hash.h Hash.cpp List.h List.cpp
	g++ -o hash1 -DHASHFUNCTION1 main.cpp Board.cpp
