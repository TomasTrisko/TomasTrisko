import random

colors = {"c": "cervena", "z": "zelena", "m": "modra", "b": "bila", "h": "hneda"}
color_codes = [key for key in colors]
print(color_codes)
rnd = random.randint(0, 2)
print(colors[color_codes[rnd]])