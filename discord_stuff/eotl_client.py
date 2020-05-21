
#     async def on_message(self, message):
#         '''
#         Called when a member posts a message in a discord channel
#
#         :param message: message object
#         '''
#
#         if message.author == self.user:
#             return
#
#         if (message.content[0] == '!'):
#             await message.channel.send(
#                 f'Command given: {message.content[1:]}'
#             )
#             # do command
#             return
#
#         # if (message.content == 'testing 123'):
#         await message.channel.send(
#             f'Message: {message.content}\n'
#         )
#         print(f"Relayed: {message.content}")
