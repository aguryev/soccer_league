from data_provider import SoccerClubData, SoccerPlayerData

class SoccerClub:
    def __init__(self, id):
        data = SoccerClubData().get(id)
        self.id = id
        self.title = data["title"]
        lineup = data["lineup"]
        self.defense = lineup[0]
        self.support = lineup[1]
        self.attack = lineup[2]


class SoccerPlayer:
    def __init__(self, id):
        data = SoccerPlayerData().get(id)
        self.first_name = data["firstName"]
        self.last_name = data["lastName"]
        self.defence = data["deffence"]
        self.control = data["control"]
        self.attack = data["attack"]
        self.position = data["position"]
        self.club = SoccerClub(data["club"])
