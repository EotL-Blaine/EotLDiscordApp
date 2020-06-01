import json

test_list = {
    "id" : "auto_who",
    "channel" : "bitch",
    "data" : [
        {
            "level" : "Jan",
            "name" : "Cozminsky",
            "guild": "",
            "spec" : "",
            "idle" : 180,
        },
        {
            "level" : "Arch",
            "name" : "Arphen",
            "guild" : "Capacitor",
            "spec" : "",
            "idle" : 660,
        },
        {
            "level": "Frob",
            "name": "Blaine",
            "guild": "Crusader",
            "spec": "Cleric",
            "idle": 999,
        },
        {
            "level": "235",
            "name": "Torr_alt",
            "guild": "Headhunter",
            "spec": "",
            "idle": 3700,
        },
        {
            "level": "117",
            "name": "Dude",
            "guild": "Fighter",
            "spec": "Bodyguard",
            "idle": 900,
        },
        {
            "level": "95",
            "name": "Ratchet",
            "guild": "Fighter",
            "spec": "Berserker",
            "idle": 540,
        },
        {
            "level": "9",
            "name": "Gorda",
            "guild": "",
            "spec": "",
            "idle": 3900,
        },
    ]
}

test_list_json = json.dumps(test_list)
# print(type(test_list_json), ":", test_list_json)
# test_list_python = json.loads(test_list_json)
# print(type(test_list_python), ":", test_list_python)

# y = json.dumps(test_list, indent=4)
# print(y)

''
# class WhoList:
#     id = "mud_who"
#     data = ({ ([ ({ }) ] )})
#
#     def __init__(self):
#         self.id = test_list["id"]
#         self.data = test_list["data"]
#         pass
#
#


