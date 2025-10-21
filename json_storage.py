import json


game_info = [{'name':'leroy', 'health':100, 'ammo':25, 'level':5},
             {'name':'leroy1', 'health':100, 'ammo':25, 'level':5},
             {'name':'leroy2', 'health':100, 'ammo':25, 'level':5}
             
             
             ]

# open up a new file
with open('leroy_info.json', 'w') as f:
    # write leroy info to the text file
    json.dump(game_info, f)

# read the leroy info
with open('leroy_info.json', 'r') as f:
    new_player_info = json.load(f)



print(new_player_info)