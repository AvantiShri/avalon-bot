from __future__ import division, print_function, absolute_import
import random
from collections import OrderedDict


#Mimicking Enums
class CardType(object):
    LOYAL_SERVANT_OF_ARTHUR="LOYAL_SERVANT_OF_ARTHUR"
    MERLIN="MERLIN"
    PERCIVAL="PERCIVAL"
    MINION_OF_MORDRED="MINION_OF_MORDRED"
    ASSASSIN="ASSASSIN"
    MORGANA="MORGANA"
    MORDRED="MORDRED"
    OBERON="OBERON"


#Mimicking Enums
class Team(object):
    GOOD_GUYS="GOOD_GUYS"
    BAD_GUYS="BAD_GUYS"


class Card(object):

    def __init__(self, team, card_type, special_abilities):
        self.team = team
        self.card_type = card_type
        self.special_abilities = special_abilities

    def get_additional_info_to_provide_to_player(self, game):
        raise NotImplementedError()

    def get_card_summary(self):
        return OrderedDict([("Team", str(self.team)),
                            ("Special abilities", self.special_abilities)])


class LoyalServantOfArthur(Card):

    def __init__(self):
        Card.__init__(self,
            team=Team.GOOD_GUYS,
            card_type=CardType.LOYAL_SERVANT_OF_ARTHUR,
            special_abilities="This card has no special abilities.")

    def get_additional_info_to_provide_to_player(self, game):
        return ("As a loyal servant, you don't have any additional info"
                +" beyond what the other cards in the game are. Review those"
                +" cards and their abilities to strategize.")

    
class Merlin(Card):

    def __init__(self):
        Card.__init__(self,
            team=Team.GOOD_GUYS,
            card_type=CardType.MERLIN,
            special_abilities=("You will be given information on who "
        +"the players on the bad team are, *with the exception of"
        +" MORDRED* (if MORDRED is present in the game)."
        +" You will not know the specific roles of the players on the"
        +" bad team you are told about. If PERCIVAL is in the game, you"
        +" should try to figure out who PERCIVAL is and convince them "
        +" that you are MERLIN and not MORGANA. You should not be too "
        +" obvious about being MERLIN or else the bad team will win by "
        +" assassinating you at the end."))

    def get_additional_info_to_provide_to_player(self, game):
        bad_team_players = []
        for player in game.players:
            if (player.card.team==Team.BAD_GUYS and
                player.card.card_type != CardType.MORDRED):
                    bad_team_players.append(player)
        return ("You know that the following players are on the bad team: "
                +", ".join(str(x) for x in bad_team_players))


class Percival(Card):

    def __init__(self):
        Card.__init__(self,
            team=Team.GOOD_GUYS,
            card_type=CardType.PERCIVAL,
            special_abilities=(
             "You will be told which two other players are "
     +"MORGANA and MERLIN, but you won't know exactly who is who."
     +" You should try to figure out whom to trust."))

    def get_additional_info_to_provide_to_player(self, game):
        morgana_or_merlin = []  
        for player in game.players:
            if (player.card.card_type==CardType.MORGANA
                or player.card.card_type==CardType.MERLIN):
                morgana_or_merlin.append(player) 
        assert len(morgana_or_merlin)==2
        return ("These two players are EITHER MORGANA OR MERLIN: "
                +" & ".join(str(x) for x in morgana_or_merlin))


class BadGuy(Card):

    def __init__(self, card_type, special_abilities):
        Card.__init__(self, team=Team.BAD_GUYS,
                      card_type=card_type,
                      special_abilities=special_abilities)

    def get_additional_info_to_provide_to_player(self, game):
        bad_team_players = []
        for player in game.players:
            if (player.card.team==Team.BAD_GUYS
                and player.card.card_type != CardType.OBERON): 
                bad_team_players.append(player)
        return ("You know that the following players are on the bad team: "
                +", ".join(str(x) for x in bad_team_players))


class Assassin(BadGuy):

    def __init__(self):
        super(Assassin, self).__init__(
            card_type=CardType.ASSASSIN,
            special_abilities = (
            "At the end of the game, you will take the"
            +" final call on who Merlin is likely to be. If you guess right,"
            +" the bad team wins."))


class MinionOfMordred(BadGuy):

    def __init__(self):
        super(MinionOfMordred, self).__init__(
            card_type=CardType.MINION_OF_MORDRED,
            special_abilities="This card has no special abilities.")


class Morgana(BadGuy): 

    def __init__(self):
        super(Morgana, self).__init__(
            card_type=CardType.MORGANA,
            special_abilities = (
        "PERCIVAL will be given your"
    +" name along with the name of the person playing MERLIN, but"
    +" PERCIVAL will not be told who is who. You should try to figure"
    +" out who PERCIVAL is and convince PERCIVAL that you are MERLIN."))


class Mordred(BadGuy):
    
    def __init__(self):
        super(Mordred, self).__init__(
            card_type=CardType.MORDRED,
            special_abilities=(
             "Merlin does not know you are on the bad team"
            +" (this is a major advantage for the bad team)."))


class Oberon(BadGuy):
    
    def __init__(self):
        super(Oberon, self).__init__(
                card_type=CardType.OBERON,
                special_abilities = (
      "The other players on the bad team won't know that"
     +" you are also on the bad team (this is a disadvantage for the"
     +" bad team)."))


card_type_to_class = {
    "LOYAL_SERVANT_OF_ARTHUR": LoyalServantOfArthur,
    "MERLIN": Merlin,
    "PERCIVAL": Percival,
    "MINION_OF_MORDRED": MinionOfMordred,
    "ASSASSIN": Assassin,
    "MORGANA": Morgana,
    "MORDRED": Mordred,
    "OBERON": Oberon
}