# EotLDiscordApp

Discord Bot for End of the Line LPMUD (eotl.org:2010)
David Halek (blaine @ eotl)

In-game features
- send channel messages from the game to equivalent channels in Discord
- users can request the list of Discord members (with idle status and highest role)
- send entrance/exit messages to a logins channel in Discord
- (maybe) show deaths a short time after they happen on a deaths channel
- (maybe) show eval gain/loss for the game for the current day
 
Discord features
- see who is logged into the game
  - standard is to do a who showing eval/wiz level, and idle time
    filtering out anyone idle for more than an hour most likely
  - can also do who -ps eval f:3000 or whatever
- see who has logged into the game on a given day
- request channel privs (requires making sure they have an eval 80 or higher in game)
- discord channel messages will be echoed in-game

It may also allow the ability to:
- send private messages back/forth
- check mudmail for the player chars registered to a discord user

