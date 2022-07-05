import json


class AbstractDataProvider:
    def __init__(self):
        self.data = {}

    def get(self, identifier):
        return self.data.get(identifier)


class SoccerPlayerData(AbstractDataProvider):
    def __init__(self):
        with open("data/pilkarze.json", "r") as f:
            data = json.load(f)
            self.data = {item["id"]: item for item in data}


class SoccerClubData(AbstractDataProvider):
    def __init__(self):
        with open("data/kluby.json", "r") as f:
            self.data = json.load(f)
