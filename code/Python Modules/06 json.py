# https://youtu.be/9N6a-VLBa2I?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU

import json

with open("Python Modules/06.1 states.json") as f:
    data = json.load(f)

for state in data["states"]:
    # print(state["name"])
    del state["area_codes"]  # delete a key

with open("Python Modules/06.2 new_states.json", "w") as f:
    json.dump(data, f, indent=2)  # dumps -> string. dump -> file

