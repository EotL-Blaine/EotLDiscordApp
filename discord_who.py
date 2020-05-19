


def get_discord_who(guild):

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')
