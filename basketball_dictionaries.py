# this is a list of dictionaries
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
    def __init__(self, player_dict):
        # player_dict is a dictionary and we are accessing the key "name" to get the value
        self.name = player_dict["name"]
        self.age = player_dict["age"]
        self.position = player_dict["position"]
        self.team = player_dict["team"]

    def display_player(self):
        print(
            f"Name: {self.name}\nAge: {self.age}\nPosition: {self.position}\nTeam: {self.team}\n")

    def __repr__(self):
        # this will tell python to print in the format we want
        return f"Name: {self.name}\nAge: {self.age}\nPosition: {self.position}\nTeam: {self.team}\n"
    @classmethod
    def get_team(cls, playas_list):
        for player_dict in playas_list:
            player = cls(player_dict)
            player.display_player()
            # we are adding an object(player) to the list
        return cls

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
print(jason["name"])
player_jason = Player(jason)
# <__main__.Player object at 0x0fdsfdsfdsf some address in memory
print(player_jason)
# this tells us that player_jason is an instance of the Player class
player_kevin = Player(kevin)
# this creates a new variable for kevin, and pass the kevin dictionary into the player init method
print(player_kevin)
player_kyrie = Player(kyrie)
print(player_kyrie)

# Challenge 3: Make a list of Player instances from a list of dictionaries
# ... (class definition and large list of players here)
# Create your loop here!


# Write your for loop here to populate the new_team variable with Player objects from orignal list.
# for loop over list of dictionaries
# each time we loop we use the dictionary info to create a new player instance
new_team = []
# empty list to store player instances
for player_dict in players:
    player = Player(player_dict)
    # player.display_player()
    new_team.append(player)
    # we are adding an object(player) to the list

print(new_team)  # we expect to print a list of players in the format we did above

# Ninja Bonus: Add an @class method called get_team(cls, team_list) that, given a list of dictionaries populates and returns a new list of Player objects.
print("++++++++++++Ninja Bonus++++++++++++")
Player.get_team(players)
# here we are calling the class method get_team and passing in the list of dictionaries in this case players