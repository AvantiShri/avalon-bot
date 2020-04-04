from enum import Enum #Python 3 - enums
import random


class CardType(Enum):
    LOYAL_SERVANT_OF_ARTHUR="LOYAL_SERVANT_OF_ARTHUR"
    MERLIN="MERLIN"
    PERCIVAL="PERCIVAL"
    MINION_OF_MORDRED="MINION_OF_MORDRED"
    MORGANA="MORGANA"
    MORDRED="MORDRED"
    OBERON="OBERON"


class Team(Enum):
    GOOD_GUYS="GOOD_GUYS"
    BAD_GUYS="BAD_GUYS"


class Card(object):

    def __init__(self, player_assigned_to):
        self.player_assigned_to = player_assigned_to

    @classmethod
    def get_additional_info_to_provide_to_player(self, game):
        raise NotImplementedError()


class LoyalServantOfArthur(Card):

    team=Team.GOOD_GUYS 
    card_type=CardType.LOYAL_SERVANT_OF_ARTHUR
    special_abilities="This card has no special abilities."

    @classmethod
    def get_additional_info_to_provide_to_player(self, game):
        return ("As a loyal servant, you don't have any additional info"
                +" beyond what the other cards in the game are. Review those "
                +" cards and their abilities as it will help you strategize.")

    
class Merlin(object):

    team=Team.GOOD_GUYS 
    card_type=CardType.MERLIN
    special_abilities=("This player will be given information on who "
        +"the players on the bad team are, *with the exception of"
        +" MORDRED* (if MORDRED is present in the game)."
        +" This player will not know the specific roles of the players on the"
        +" bad team that they are told about.")

    @classmethod
    def get_additional_info_to_provide_to_player(self, game):
        bad_team_players = []
        for card in game.cards:
            if (card.team==Team.BAD_GUYS and
                card.card_type != CardType.MORDRED):
                    bad_team_players.append(card)
        return ("You know that the following players are on the bad team: "
                +", ".join(bad_team_players))


class Percival(object):

    team=Team.GOOD_GUYS
    card_type=CardType.PERCIVAL
    special_abilities=("This player will be told which two other players are "
     +"MORGANA and MERLIN, but they won't know exactly who is who"
     +" between the two")

    @classmethod
    def get_additional_info_to_provide_to_player(self, game):
        morgana_or_merlin = []  
        for card in game.cards:
            if (card.card_type==CardType.MORGANA
                or card.card_type==CardType.MERLIN):
                morgana_or_merlin.append(card) 
        assert len(morgana_or_merlin)==2
        return ("These two players are EITHER MORGANA OR MERLIN: "
                +" & ".join([x.get_name() for x in morgana_or_merlin]))


class BadGuy(object):

    team=Team.BAD_GUYS 

    @classmethod
    def get_additional_info_to_provide_to_player(self, game):
        bad_team_players = []
        for card in game.cards:
            if (card.team==Team.BAD_GUYS
                and card.card_type != CardType.OBERON): 
                bad_team_players.append(card)
        return ("You know that the following players are also on the bad team: "
                +", ".join(bad_team_players))


class MinionOfMordred(BadGuy):
    card_type=CardType.MINION_OF_MORDRED
    special_abilities="This card has no special abilities."


class Mordred(BadGuy):
    card_type=CardType.Mordred
    special_abilities=(" Merlin does not know this player is on the bad team"
    +" (this is a major advantage for the bad team).")


class Oberon(BadGuy):
    card_type=CardType.OBERON
    special_abilities = ("The other players on the bad team won't know this "
     +" player is also on the bad team (this is a disadvantage for the "
     +" bad team).")
