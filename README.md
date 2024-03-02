# cfgw
Classic WolfGoatFarmerCabbage

Collaborators: Hammad Sheikh

This project references code from aimacode https://github.com/aimacode/aima-python.

Goal: Write a Python class, WolfGoatCabbage, that describes the Wolf, goat and cabbage problem and can then be used to solve it by calling a search algorithm.

* Represent the state by a set of characters, representing the objects on the left bank. Use the characters: ‘F’, ‘G’, ‘W’, ‘C’. Note that it is sufficient to represent the objects on one bank since the remaining will be on the other bank. E.g., {‘F’, ‘G’} represents Farmer and Goat on the left bank and Wolf and Cabbage on the right.
*	An action in this puzzle is 1-2 objects crossing in the boat. Represent an action as a set of characters representing the objects crossing. E.g., {‘F’, ‘G’} represents the farmer and goat crossing. Note that it is not necessary to represent the direction of the boat as this will be clear from the state (e.g., if the farmer is on the left, then the boat will have to cross to the right).

The code should print something like:

[{'G', 'F'}, {'F'}, {'C', 'F'}, {'G', 'F'}, {'W', 'F'}, {'F'}, {'G', 'F'}]

[{'G', 'F'}, {'F'}, {'W', 'F'}, {'G', 'F'}, {'C', 'F'}, {'F'}, {'G', 'F'}]
