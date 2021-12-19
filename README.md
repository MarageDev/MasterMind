# MindMaster
![GitHub last commit](https://img.shields.io/github/last-commit/MarageDev/MasterMind?style=for-the-badge)
[![ds](https://img.shields.io/badge/DISCORD-Link-blue.svg?style=for-the-badge)](https://discord.gg/8T2Ba2V2hj)
## What is it ?
  This is a simple python code replicating the game Master Mind made by Mordecai Meirowitz in 1970. It's a 2 player game.
> ***Note :*** 
> The project MindMaster stills Work-In-Progress
### How to play
  Once you've opened the code, run it with a terminal and follow the console logs, you need to be 2. Firstly, one player needs to enter a ***code of 4 digits*** ( if it isn't, it'll show a warning in the console ), then the 2nd player needs to enter test codes to see if it's the one entered by the 1st player. Below the test code, there's an ***hint log*** telling if the number entered are presents in the code entered by the 1st player to help the other to find the code.
### How to run
  From source code :
- Open the `MasterMind.py` file
- Run it on ***terminal*** with the key `F5` ( on Visual Studio ) or find an option `Start debugging`
- Follow the instructions in the terminal

## Information
You can change manually some settings like that :
> The number in front of the code-line is the line where this part of the code is in the `MasterMind.py` file
```py
### Change the number of tries allowed
90    tries = 5                                               # Set the number of tries allowed
```
```py
### Change target code's length to make
21    if len(code) != 4:                                      # Target code's length
```

### Example of console logs
```markdown
Enter a 4 digit code :
- 7598
The code is : 7598

Enter a code to test :
- 1435
X X X X
The code contains : 5

You have 4 tries left

Enter a code to test :
- 7489
7 X X X
The code contains : 7 8 9

You have 3 tries left

Enter a code to test :
- 7598
7 5 9 8
The code contains : 7 5 9 8

You've found the code, good work !
```


## Coming Features
- [ ] Reworked Logs
- [ ] An app to run it instead of runing it in the terminal and get a nicer UI
- [x] A 1 player mode where the target code will be random
- [ ] Maybe letter support
- [ ] Customization settings ( tries, code format... )
- [ ] Reworked ReadMe on github with images and maybe videos ( And maybe add this project to a global github webpage with all my work )
## Credits
Marage and Mordecai Meirowitz for the original idea




### License
This work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0
International License][cc-by-nc-sa].
[![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]
[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg
