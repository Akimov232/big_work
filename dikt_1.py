player_1 = {}

player_status = {'Fireway': 'amazon' , 'Dewedor': 'necromancer'}

player_status['Fireway'] = 'barbarian'

player_status['Mark'] = 'bard'

del player_status['Fireway']

for key in player_status.keys():
    print(key)

print(player_status.keys())

print(player_status.values())