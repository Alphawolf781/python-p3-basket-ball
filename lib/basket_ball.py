def game_dict():
    return {
        "home": {
            "team_name": "Cleveland Cavaliers",
            "colors": ["Wine", "Gold"],
            "players": [
                {
                    "name": "Jarrett Allen",
                    "number": 31,
                    "position": "Center",
                    "points_per_game": 16.1,
                    "rebounds_per_game": 10.8,
                    "assists_per_game": 1.6,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.3,
                    "career_points": 3945,
                    "age": 24,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Darius Garland",
                    "number": 10,
                    "position": "Point Guard",
                    "points_per_game": 21.7,
                    "rebounds_per_game": 3.3,
                    "assists_per_game": 8.6,
                    "steals_per_game": 1.3,
                    "blocks_per_game": 0.1,
                    "career_points": 3142,
                    "age": 22,
                    "height_inches": 73,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Evan Mobley",
                    "number": 4,
                    "position": "Center",
                    "points_per_game": 15.0,
                    "rebounds_per_game": 8.3,
                    "assists_per_game": 2.5,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.7,
                    "career_points": 1034,
                    "age": 21,
                    "height_inches": 83,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Kevin Love",
                    "number": 0,
                    "position": "Power Forward",
                    "points_per_game": 13.6,
                    "rebounds_per_game": 7.2,
                    "assists_per_game": 2.2,
                    "steals_per_game": 0.4,
                    "blocks_per_game": 0.2,
                    "career_points": 14305,
                    "age": 34,
                    "height_inches": 80,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Isaac Okoro",
                    "number": 35,
                    "position": "Small Forward",
                    "points_per_game": 8.8,
                    "rebounds_per_game": 3.0,
                    "assists_per_game": 1.8,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 0.3,
                    "career_points": 1234,
                    "age": 21,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Ricky Rubio",
                    "number": 99,
                    "position": "Point Guard",
                    "points_per_game": 13.1,
                    "rebounds_per_game": 4.1,
                    "assists_per_game": 6.6,
                    "steals_per_game": 1.4,
                    "blocks_per_game": 0.2,
                    "career_points": 7399,
                    "age": 31,
                    "height_inches": 74,
                    "shoe_brand": "Adidas",
                },
            ],
        },
            
        "away": {
            "team_name": "Washington Wizards",
            "colors": ["Red", "White", "Navy Blue"],
            "players": [   
                {
                    "name": "Bradley Beal",
                    "number": 3,
                    "position": "Shooting Guard",
                    "points_per_game": 23.2,
                    "rebounds_per_game": 4.7,
                    "assists_per_game": 6.6,
                    "steals_per_game": 0.9,
                    "blocks_per_game": 0.4,
                    "career_points": 14231,
                    "age": 29,
                    "height_inches": 76,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kyle Kuzma",
                    "number": 33,
                    "position": "Power Forward",
                    "points_per_game": 17.1,
                    "rebounds_per_game": 8.5,
                    "assists_per_game": 3.5,
                    "steals_per_game": 0.6,
                    "blocks_per_game": 0.9,
                    "career_points": 5336,
                    "age": 27,
                    "height_inches": 81,
                    "shoe_brand": "Puma",
                },
                {
                    "name": "Kentavious Caldwell-Pope",
                    "number": 1,
                    "position": "Shooting Guard",
                    "points_per_game": 13.2,
                    "rebounds_per_game": 3.4,
                    "assists_per_game": 1.9,
                    "steals_per_game": 1.1,
                    "blocks_per_game": 0.3,
                    "career_points": 7911,
                    "age": 29,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Davis Bertans",
                    "number": 42,
                    "position": "Power Forward",
                    "points_per_game": 5.6,
                    "rebounds_per_game": 2.1,
                    "assists_per_game": 0.6,
                    "steals_per_game": 0.3,
                    "blocks_per_game": 0.3,
                    "career_points": 3165,
                    "age": 29,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kristaps Porzingis",
                    "number": 6,
                    "position": "Power Forward",
                    "points_per_game": 22.1,
                    "rebounds_per_game": 8.8,
                    "assists_per_game": 2.9,
                    "steals_per_game": 0.7,
                    "blocks_per_game": 1.5,
                    "career_points": 6371,
                    "age": 27,
                    "height_inches": 87,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Rui Hachimura",
                    "number": 8,
                    "position": "Power Forward",
                    "points_per_game": 11.3,
                    "rebounds_per_game": 3.8,
                    "assists_per_game": 1.1,
                    "steals_per_game": 0.5,
                    "blocks_per_game": 0.2,
                    "career_points": 1913,
                    "age": 24,
                    "height_inches": 80,
                    "shoe_brand": "Jordan",
                },
            ]
        }
    }


def num_points_per_game(name):
#    fetch the game data
    game_data = game_dict()

    # check both home and away teams
    for team in ['home', 'away']:
        for player in game_data[team]['players']:
            if player['name'] == name:
                return player['points_per_game']
            
    return None
print(num_points_per_game("Bradley Beal"))

def player_age(name):
    # fetch the game data
    game_data = game_dict()

    # iterate over the players to get the age
    for team in ['home','away']:
        for player in game_data[team]['players']:
            if player['name'] == name:
                return player['age']
            
    return None
print(player_age("Bradley Beal"))

def team_colors(team_name):
    # fetch game data
    game_data = game_dict()

    # Get the team name
    for team in ['home', 'away']:
        if game_data[team]['team_name'] == team_name:
                return game_data[team]["colors"]
            
    return None
print(team_colors("Cleveland Cavaliers"))

def team_names():
    # fetch game data
    game_data = game_dict()

    # Get the team name
    home_team_name = game_data['home']['team_name']
    away_team_name = game_data['away']['team_name']

    return [home_team_name,away_team_name]
print(team_names())

def player_numbers(team_name):
    # fetch game data
    game_data = game_dict()

    for team in ['home', 'away']:
        if game_data[team]['team_name'] == team_name:
                return[player['number'] for player in game_data[team]['players']]
    return None
print(player_numbers("Cleveland Cavaliers"))

def player_stats(Player_name):
     game_data = game_dict()

     for team in ['home', 'away']:
          for player in game_data[team]['players']:
               if player['name'] == Player_name:
                    return {"name": player['name'],
                            "number": player['number'],
                            "position" :player['position'],
                            "points_per_game":player['points_per_game'],
                            "rebounds_per_game":player['rebounds_per_game'],
                            "assists_per_game":player['assists_per_game'],
                            "steals_per_game":player['steals_per_game'],
                            "blocks_per_game":player['blocks_per_game'],
                            "career_points":player['career_points'],
                            "age":player['age'],
                            "height_inches":player['height_inches'],
                            "shoe_brand":player['shoe_brand']
                              }


     return None
print(player_stats("Bradley Beal"))

def average_rebounds_by_shoe_brand():
   
    # Fetch the game data
    game_data = game_dict()
    
    # Dictionary to hold rebounds by shoe brand
    rebounds_by_brand = {}
    
    # Iterate through both home and away teams
    for team in ['home', 'away']:
        for player in game_data[team]['players']:
            shoe_brand = player['shoe_brand']
            rebounds = player['rebounds_per_game']
            
            if shoe_brand not in rebounds_by_brand:
                rebounds_by_brand[shoe_brand] = []
            
            rebounds_by_brand[shoe_brand].append(rebounds)
    
    # Calculate and print the average rebounds for each shoe brand
    for brand, rebounds in rebounds_by_brand.items():
        average_rebounds = sum(rebounds) / len(rebounds)
        print(f"{brand}:  {average_rebounds:.2f}")

# Example usage
average_rebounds_by_shoe_brand()
