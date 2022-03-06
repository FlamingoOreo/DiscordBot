import discord

token = "OTQ3ODk0MzAxOTQ4NTM0Nzk0.Yhz5XA.bzkLZr2dpkPN9A_DE20KxFunf0Q"

class bot(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

Bot1 = bot()
Bot1.run(token)

