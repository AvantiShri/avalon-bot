# avalon-bot
This is a bot to assist in playing [Avalon](https://hobbylark.com/card-games/How-to-Play-Avalon) online (e.g. over zoom). Given a configuration specifying the players, their emails, and the cards in the game, this bot will email each player their (randomly chosen) card, as well as additional privileged information appropriate to the player (e.g. it will tell the PERCIVAL player which two other players are either MORGANA or MERLIN, etc). In other words, each player will get an email that looks something like this:
![](https://github.com/AvantiShri/avalon-bot/raw/master/ExampleEmail1.png "Example Email")

## Running the bot
I've created a Google Colab notebook that demonstrates how to run the bot. It can be accessed [here](https://colab.research.google.com/github/AvantiShri/avalon-bot/blob/master/Avalon_Bot_Playing_Avalon_Online_With_Friends_(e_g_over_Zoom).ipynb).

## Tips for playing on Zoom

### Voting

It turns out Zoom's built-in vote functionality is a little finicky. So I recommend using other methods to do the votes. For the non-anonymous vote, having each player enter their vote in the chat worked out fine (someone should do a countdown so that the votes are entered roughly simultaneously). For the anonymous votes, there are several websites that allow you to create quick straw polls, e.g. https://www.strawpoll.me/ (you might want to visit those sites in incognito mode to be prevent them from using cookies). There are also other creative solutions, e.g. having everyone visit a [codeshare](https://codeshare.io/new) page and enter their votes by typing a single "y" or "n" character (my friends actually did this and it worked ok).

### Keeping track of past votes
My friends and I tracked this by sending messages to the group chat, and it worked fine.

### Player order
Because the position of windows in zoom's gallery view can move around, we find it's best to fix the player order in advance e.g. alphabetically or reverse-alphabetically.

### Other
- Decide in advance on whether or not you are going to allow sending PMs. The original game was designed to have everyone physically in the same room, so private communication wouldn't have been possible (except when using the "Lady of the Lake").
- The rules of Avalon are available online, e.g. [here](https://hobbylark.com/card-games/How-to-Play-Avalon) 

## Running the bot from the Command Line (for more tech-savvy users)

This package is on pypi and can be installed with pip:
```
pip install avalonbot
```

The bot can then be run with:
```
run_avalon_bot --game_name YourGameNameHere --smtp_server specify.your.smtp.server --sender email.for.bot@example.com [--password passwordforbot] --json_config_file /path/to/json_config.json
```

### Config file format
See example_config/avalon_config.json for an example config file. The format is:
```
{
  "players: [
    {"name": "Name_of_player_1",
		 "email": "email.of@player1"},
		{"name": "Name_of_player_2",
		 "email": "email.of@player2"},
    (...additional player info, separated by commas...)
  ],
  "cards": [
      (This is a comma-separated list of the cards
       present in the game. If you have two of a particular
       type of card, repeat that card twice. The length of this
       list should be equal to the length of the "players" list.
       The possible cards are:)
      "LOYAL_SERVANT_OF_ARTHUR",
      "MERLIN",
      "PERCIVAL",
      "MINION_OF_MORDRED",
      "ASSASSIN",
      "MORGANA",
      "MORDRED",
      "OBERON"
  ]
}
```
