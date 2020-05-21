

def get_discord_who(guild):
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')
    return members


    # members = get_discord_who(guild)
    # print(f'Guild Members from get_discord_who:\n - {members}')
    #
    # members = client.users;
    # for m in members:
    #     print(f'-->{m.name}')
    # print(f'Guild Members from client.users:\n - {members}')


