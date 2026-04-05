# Battle Boats

A command-line Battleship-style game written in Python. Sink all hidden ships on a 10x10 grid by guessing coordinates. Ships are randomly placed each game, and your accuracy is scored at the end.

## Features

- 10x10 game board
- 4 ships of varying lengths (2, 3, 4, 5) randomly placed horizontally or vertically
- Hit and miss markers on the board
- Input validation and duplicate guess detection
- Accuracy score displayed upon winning

## Installation

```bash
git clone https://github.com/is386/battle-boats.git
cd battle-boats
```

**Requirements:** Python 3

## Usage

```bash
python3 battleboats.py
```

## Board

```
            Battle Boats
    0  1  2  3  4  5  6  7  8  9
   -----------------------------
0|  X  .  .  .  X  X  .  .  .  .
1|  .  .  .  .  .  .  .  .  .  .
2|  .  .  .  .  .  .  .  .  .  .
3|  .  .  .  X  .  .  .  .  X  .
4|  .  .  .  O  .  .  .  .  .  .
5|  .  .  .  O  .  .  .  .  X  .
6|  .  .  .  X  .  .  .  .  .  .
7|  .  .  .  O  .  .  .  .  .  .
8|  .  .  .  .  .  .  .  X  .  .
9|  .  .  X  X  .  .  X  .  .  .
```

- `.` — unexplored cell
- `O` — hit
- `X` — miss

## How to Play

1. The game randomly places 4 ships (lengths 2, 3, 4, 5) on a hidden 10x10 grid.
2. Enter a two-digit coordinate `XY` where `X` is the column (0-9) and `Y` is the row (0-9).
   - Example: `34` targets column 3, row 4.
3. The board updates with `O` for a hit or `X` for a miss.
4. You cannot guess the same coordinate twice.
5. Sink all ships (14 total hits) to win. Your accuracy percentage is displayed at the end.
