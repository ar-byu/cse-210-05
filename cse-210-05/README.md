# Cycles
"The best rides are the ones where you bite off much more than you can chew, and live through it." ~ Doug Bradbury

"On the other side of the screen, it all looks so easy." ~ Kevin Flynn (TRON)

## Getting Started
---
Make sure you have Python 3.8 or newer installed, as well as the Raylib module. You can install the Raylib module from a terminal and running this command:
 
```
python3 -m pip install raylib
```
Once you have installed the module and downloaded the files for this game, you can run it from a terminal using the following command (or a variation, if you have it saved into a subfolder):
```
python3 cycles
```
You can also run the program from an IDE such as Visual Studio Code. Select the "main" program and press the Run button.

### How To Play
---
Cycles is a two-player game. You play as a "cycle". Player 1 is red, Player 2 is green. Player 1 uses the W, A, S, and D keys to move their snake. Player 2 uses I, J, K, and L. The object of the game is to make your opponent crash. You can also collect coins (represented by a yellow '0') to earn points. The last player remaining wins.

## Project Structure
---
The project files and folders are organized as follows:

```
casting             (cast object files for game)
director            (game master file)
services            (keyboard and screen files)
shared              (shared files for positioning and color)
__main__.py         (the main access point for the game)
README.md           (general information)
```
## Required Technologies
---
* Python 3.8.0 or newer
* Raylib Python CFFI 3.7

## Authors
---
Anna Rector, CSE 210 student. lighteternal.lunae@gmail.com, arector2002@gmail.com

_**It is important to note that most of the classes and methods in this project were copied from CSE 210's earlier project, Snake, due to the similarities between both games.**_