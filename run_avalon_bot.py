#!/usr/bin/env python
from __future__ import division, print_function, absolute_import
import argparse
import json 
import os
import avalonbot


def send_email(subject, to_addresses,
               sender, #eg: "avutils-mail-sender@stanford.edu",
               smtp_server, #eg: "smtp.stanford.edu",
               contents=""):
    from email.mime.text import MIMEText
    import smtplib
    msg = MIMEText(contents)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ",".join(to_addresses)

    s = smtplib.SMTP(smtp_server)
    s.starttls();
    s.sendmail(sender, to_addresses, msg.as_string())
    s.quit()


def parse_config(json_config_file):
    parsed_config = json.loads(open(json_config_file).read()) 
    assert "players" in parsed_config, "Please specify a 'players' entry"
    assert "cards" in parsed_config, "Please specify a 'cards' entry"

    players = []
    for player_info in parsed_config["players"]:
        assert "email" in player_info,\
            "All player entries must have 'email'; got: "+str(player_info) 
        assert "name" in player_info,\
            "All player entries must have 'name'; got: "+str(player_info) 
        players.append(avalonbot.game.Player(name=player_info["name"],
                                             email=player_info["email"])) 

    cards = []
    for card_type in parsed_config["cards"]:
        cards.append(
         avalonbot.cards.card_type_to_class[card_type]())

    return players, cards


def json_dump(obj):
    return json.dumps(obj, indent=4, separators=(',', ': '))


def run_game(args):
    players, cards = parse_config(args.json_config_file)
    game = avalonbot.game.Game(players=players, cards=cards) 
    game.assign_cards_to_players()

    secret_info = game.prepare_secret_info_to_tell_each_player() 
    card_types_info = game.prepare_info_on_cards_types()
    good_team_cards, bad_team_cards = game.prepare_info_on_teams()

    for player,private_info in secret_info.items():
        contents = ("Hi "+player.name+",\n"
                    "Here is your avalon card assignment:\n"
                    +json_dump(private_info)+"\n"
                    +"\nHere is info on the cards present in this game:\n"
                    +"\nCards for the good team:\n"
                    +json_dump(good_team_cards)+"\n"
                    +"\nCards for the bad team:\n"
                    +json_dump(bad_team_cards)+"\n"
                    +"\nDescriptions of each card:\n"
                    +json_dump(card_types_info))
        
        send_email(subject="Your Avalon Card Assignment for "
                           +"game: "+str(args.game_name),
                   to_addresses=[player.email],
                   sender="avalon-bot@stanford.edu",
                   contents=contents,
                   smtp_server=args.smtp_server) 


if __name__=="__main__":
    parser = argparse.ArgumentParser("Welcome to Avalon Bot!"
            +" You will need access to a smtp server for sending mail\n")
    parser.add_argument("--game_name", required=True,
                        help="A name for the game to put in the email subject line")
    parser.add_argument("--smtp_server", required=True)
    parser.add_argument("--json_config_file", required=True,
                        help="See example config")
    args = parser.parse_args()
    run_game(args)
    