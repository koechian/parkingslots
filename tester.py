import pickle
import cv2

# import math
# from platform import node

# WIDTH, HEIGHT = 107, 48
# GATE = (42, 13)

# with open("slots.p", "rb") as f:
#     nodes = pickle.load(f)

# index = []
# index.extend(range(1, len(nodes)))

# i = 1
# Dict = dict()

# for x in nodes:

#     Dict[i] = {
#         "pos": x,
#         "distance": abs(math.floor(x[0] + (WIDTH / 2)) - GATE[0])
#         + abs((math.floor(x[1] + (HEIGHT / 2)) - GATE[1])),
#         "occupied": True,
#     }

#     if i != 69:
#         i = i + 1
#     else:
#         break

# # Dict created after the slots have been loaded into node pos

# with open("data/slots.p", "rb") as f:
#     Dict = pickle.load(f)

with open("compDict.p", "rb") as f:
    Dict = pickle.load(f)


minDistance = min(d["distance"] for d in Dict.values())

# Dict[2]["occupied"] = False

print(minDistance)
suggested = [
    k
    for k in Dict
    if (Dict[k]["distance"] == minDistance and Dict[k]["occupied"] == False)
]