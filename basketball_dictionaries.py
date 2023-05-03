players = [
    {
        "name": "Kevin Durant",
        "age": 34,
        "position": "small forward",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum",
        "age": 24,
        "position": "small forward",
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving",
        "age": 32,
        "position": "Point Guard",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard",
        "age": 33,
        "position": "Point Guard",
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid",
        "age": 32,
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

# Update the constructor to accept a dictionary with a single player's information instead of individual arguments for the attributes.
# Player class with updated constructor


class Player():
    def __init__(self, player):
        self.name = player["name"]
        self.age = player["age"]
        self.position = player["position"]
        self.team = player["team"]

    def display_player(self):
        print(
            f"Name: {self.name}\nAge: {self.age}\nPosition: {self.position}\nTeam: {self.team}\n")

# Challenge 2: Create instances using individual player dictionaries.


kevin = {
    "name": "Kevin Durant",
    "age": 34,
    "position": "small forward",
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum",
    "age": 24,
    "position": "small forward",
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving",
    "age": 32,
    "position": "Point Guard",
    "team": "Brooklyn Nets"
}

# Create your Player instances here!

player_jason = Player(jason)
player_kevin = Player(kevin)
player_kyrie = Player(kyrie)


# Challenge 3: Make a list of Player instances from a list of dictionaries
# ... (class definition and large list of players here)
# Create your loop here!


# Write your for loop here to populate the new_team variable with Player objects.
new_team = []
for player in players:
    player = Player(player)
    # player.display_player()
    new_team.append(player)

print(new_team[1].age)
