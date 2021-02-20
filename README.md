# cancel_135865_final_project_Solitaire



Classic card game Solitaire using Python.

The game developed is an interactive version of the popular classic game named Solitaire where the user has to release and play into position certain cards to build up each foundation, in sequence and in suit, from the ace through the king to finally be able to build the whole pack onto the foundations and win the game.

This version was developed using python with the graphics library.

The code is composed of 3 classes SolitaireGame, Card and Button. The 3 of them worked together to generate the gameplay and be able to accomplish the desired objectives. First the user is prompted with a “splash screen” with to buttons to either start or quit the game. After Start Game is pressed then the game starts and the user is able to select the cards using his computer mouse left click and then click the other card where the card can be attached, if not, the card won’t be added, and the user will have to keep trying until the card can be attached and it will be automatically added below. 

Some of the principles to which we recurred when developing our code was to class encapsulation, making it organized, understandable, easier to reuse the code, and be able to implement such class in other program interfaces. The other principle was polymorphism that gave us the flexibility to use each object to perform the desired action. After applying these two principles we were able developed the whole game in a fast and efficient way.


Attention/Notice
In this version the foundations stack wasn’t able to be implemented so the cards couldn’t be added to a foundation stack and the K card can’t be moved to an empty pile. The card must be clicked middle down because if not it would select the card below of it.
