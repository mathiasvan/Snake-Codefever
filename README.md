# Snake game CodeFever

# How to play

## Overview

Using the arrow keys for the green snake and the wasd keys for the blue snake, try to get as many points as possible while trying not to bump into each other!

## Running the game

There are two ways to run the game:

1. If you have python installed, click on the `main.py` file.
2. If you are on Windows, you can run the `.exe` file in the `dist` folder. If you run into errors, try turning off your anti-virus.

# How to compile .exe file (Windows)

## Installation of pyinstaller (1 time)

In the terminal, run:

```powershell
pip install pyinstaller
```

## Compile .exe file

Run this command in the terminal in the directory with the `main.py` file to compile the `.exe` file.

```powershell
pyinstaller --onefile --noconsole main.py
```

The file will be created in the `dist` folder.
⚠️Turn of your virus scanner before running the file!

## Further reference

This documentation is based on [this](https://stackoverflow.com/questions/54210392/how-can-i-convert-pygame-to-exe) post on stackoverflow.
