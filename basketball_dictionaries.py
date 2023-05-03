players = [
    {
    	"name": "Kevin Durant",
    	"age":34,
    	"position": "small forward",
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum",
    	"age":24,
    	"position": "small forward",
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving",
    	"age":32,
        "position": "Point Guard",
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard",
    	"age":33,
        "position": "Point Guard",
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid",
    	"age":32,
        "position": "Power Foward",
    	"team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]

class Player:
    def __init__(self, player):
        self.name = player["name"]
        self.age = player["age"]
        self.position = player["position"]
        self.team = player["team"]

    def display_player(self):
        print(f"Name: {self.name}\nAge: {self.age}\nPosition: {self.position}\nTeam: {self.team}\n")


# Update the constructor to accept a dictionary with a single player's information instead of individual arguments for the attributes.
class Player:
    def __init__(self, player):
        self.name = player["name"]
        self.age = player["age"]
        self.position = player["position"]
        self.team = player["team"]

    def display_player(self):
        print(f"Name: {self.name}\nAge: {self.age}\nPosition: {self.position}\nTeam: {self.team}\n")

print("Player 1:")
