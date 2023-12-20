# Chess Bot Challenge

For a little challenge for friends

## TLDR

The idea is to make a little game where the goal is to write a chess bot without external resources and with a constraint on the size of the code.


## How to participate

1. Clone the repository
2. Install the requirement (python-chess) with the command `pip install -r requirement.txt`
3. make your own bot, you can take `DummyBot1.py` as exemple. The Code should contain a class that heritate from the class `Bot` defined in `BotTemplate.py`
4. Give a nice name to your class, it will be used as the name for your bot ;)
5. send your bot !

## How to test/run your bot

A script has be coded to test and generate match between two bots. The script is in the file `engine.py`. 
Just specify the paths to the python file with the bots you want.

```
python engine.py DummyBot1.py DummyBot2.py
```

Some arguments can be added:
- `-v` or `--verbose` will show the game as it goes. It will also display some informations such as the time left after a player has moved.
- `--max_length ???` can be used to change the max length for the code of the bots. (default: 1000)
- `--time_per_bot ???` can be used to change the clock of the game. This time is the total time allowed for each bot during the game. If after some moves a bot use all of his time it will count as a defeat.
- `--nb_games ??` can be used to run multiples games. We advice not to use the verbose argument to run multiples games faster.


## Rules

1. Do not search for solutions online.
2. Your code should contain 1024 tokens or less (see *How do we count tokens* for details)
3. You can import non-standard library beside `numpy`

## How do we count tokens

We use tokens as they are parsed by python. `COMMENT` tokens (one line comment) will be ignored in the count.

To see tokens in your code you can use : 
`python -m tokenize -e you_python_file.py`

You can count your tokens without `COMMENT` token by using:
`python -m tokenize -e you_python_file.py | grep -v COMMENT | wc -l`
