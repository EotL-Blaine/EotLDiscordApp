'''
MudWho

JSON package containing the who list for the MUD is converted and displayed to
the appropriate channel.

The auto-who will run every so many minutes and will post a message to the #who
channel.  The !who command, if given in the who channel, will update it with
a new list, otherwise it will send the results to the requester in a private
message.

An id of "mud_who" just outputs to the #who channel
Any other id (in format "mud_xx") will be the result of a command, and it will
be matched to the corresponding request in the pending list.
'''
import json
from mud_stuff import test_list

counts = {"player": 0, "wiz": 0, "guest": 0, "active": 0, "total": 0}

def get_level(lvl):
    if lvl.isdigit():
        counts["player"] += 1
        l =  f'{lvl:^6}'
    else:
        l = f'[{lvl:4}]'
        if l == "guest": counts["guest"] += 1
        else: counts["wiz"] += 1
    counts["total"] += 1
    return l

def default_who(jlist=None):
    plist = test_list.test_list_python if jlist is None else json.loads(jlist)
    data = plist["data"]
    who = ["```md", "==============[ EotL - Who ]==============", ]

    for d in data:
        gname = d["spec"] if d["spec"] is not "" else d["guild"]
        if gname is None:
            gname = ""

        lvl = get_level(d["level"])

        imins = d["idle"] // 60
        idle = f'({imins}m)'
        # Idle prefixes: '#' idle < 10m, '-' idle <50m, '>' over an hour
        if imins <= 10:
            pre = '#'
            counts["active"] += 1
        elif imins <= 60:
            pre = '-'
            counts["active"] += 1
        else : pre = '>'
        who.append(f'{pre} {lvl} {d["name"]:13} {gname:12} {idle}')

    who.append(
        f'\nThere are a total of {counts["total"]} people on, {counts["active"]} active.\n'
        f'{counts["wiz"]} are wizards, '
        f'{counts["guest"]} are guests, and '
        f'{counts["player"]} are players.'
        '```'
    )
    #
    # for w in who:
    #     print(w)
    return who



if __name__ == "__main__":
    # Convert test list to json
    who_json = str(test_list.test_list_json)
    who = default_who(who_json)

    # who_py = json.loads(who_json)
    # # who_py = test_list.test_list
    # who = default_who(who_py)





