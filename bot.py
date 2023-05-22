## built-in modules
import os

## third-party modules
import discord

#-------------------start-of-yClient()--------------------------------------------------------------

class yClient(discord.Client):

    def __init__(self, intents):
        super().__init__(intents=intents)
        self.synced = False
    
    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        print('Yasaseru is ready.')

#-------------------start-of-main()--------------------------------------------------------------

intents = discord.Intents.default()
intents.members = True  # to receive member related events
intents.guild_messages = True  # to receive guild message related events
intents.message_content = True  # to receive message content related events

activity = discord.Activity(name='/translate', type=discord.ActivityType.watching)

Yasaseru = yClient(intents=intents)

Yasaseru.activity = activity

tree = discord.app_commands.CommandTree(Yasaseru)

#-------------------start-of-on_message()--------------------------------------------------------------

@Yasaseru.event
async def on_message(message):
    if message.content == "hi":
        await message.channel.send('Hello, world!')

#-------------------start-of-translate()--------------------------------------------------------------

@tree.command(name="translate", description="Translates a message from Japanese to English")
async def translate(interaction: discord.Interaction, message: str):
    await interaction.response.send_message(str(message) + " was altered", ephemeral=True)

#-------------------start-of-translate_menu()--------------------------------------------------------------

@tree.context_menu(name = "translate")
async def translate_menu(interaction: discord.Interaction, message: discord.Message):
    await interaction.response.send_message(str(message.content) + " was altered", ephemeral=True) 

#-------------------start-of-sub_main()--------------------------------------------------------------

Yasaseru.run(os.environ.get('YASASERU_TOKEN'))
