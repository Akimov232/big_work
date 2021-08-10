import pickle
game_data = [
    ("Mike" , "Daniil"),
    ("items ", ["club " , "shield"])
]

with open("seven.data" , "wb") as sf:
    pickle.dump(game_data , sf)

with open("seven.data" , "rb") as lf:
    load_data = pickle.load(lf)
print(load_data)