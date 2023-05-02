import discord
import os

from discord.ext import commands
from time import sleep
from discord.errors import LoginFailure,HTTPException

intents = discord.Intents.default()
intents.members = True  # to receive member related events
intents.guild_messages = True  # to receive guild message related events
intents.message_content = True  # to receive message content related events

##-------------------start-of-initialize_bot()---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def initialize_bot(configDir):

    '''

    Initializes the bot and returns the client object
    
    Parameters:
    configDir (string) - the directory where the config files are stored for Yasaseru

    Returns:
    Yasaseru (discord.ext.commands.bot.Bot) - the client object for Yasaseru
    '''

    token = "" ## the bot token

    try:
        with open(os.path.join(configDir,'botToken.txt'), 'r', encoding='utf-8') as file:  ## get saved bot token if exists
            token = file.read()

        Yasaseru = commands.Bot(command_prefix='!', intents=intents)
        
        print("Used saved token in " + os.path.join(configDir,'botToken.txt')) 
        
    except (LoginFailure,HTTPException): ## else try to get  token manually
                            
            token = input("DO NOT DELETE YOUR COPY OF THE TOKEN\n\nPlease enter Yasaseru's bot token you have : ")

            try: ## if valid save the  token
 
                if(os.path.isdir(configDir) == False):
                    os.mkdir(configDir, 0o666)
                    print(configDir + " created due to lack of the folder")

                    sleep(.1)
                            
                if(os.path.isfile(os.path.join(configDir,'botToken.txt')) == False):
                    print(os.path.join(configDir,'botToken.txt') + " was created due to lack of the file")

                    with open(os.path.join(configDir,'botToken.txt'), 'w+', encoding='utf-8') as file: 
                        file.write(token)

                    sleep(.1)

                    Yasaseru = commands.Bot(command_prefix='!', intents=intents)

            except (LoginFailure,HTTPException): ## if invalid token exit
                     
                os.system('cls')
                        
                print("Authorization error with bot, please double check your token as it appears to be incorrect.\n")
                os.system('pause')
                        
                exit()

            except Exception as e: ## other error, alert user and raise it

                os.system('cls')
                        
                print("Unknown error with bot, The error is as follows " + str(e)  + "\nThe exception will now be raised.\n")
                os.system('pause')

                raise e
            
    return Yasaseru,token

##-------------------start-of-main()---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

configDir = os.path.join(os.environ['USERPROFILE'],"YasaseruConfig")

Yasaseru,token = initialize_bot(configDir)

##-------------------start-of-on_ready()---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@Yasaseru.event
async def on_ready():
    print('Yasaseru is ready.')
    
##-------------------start-of-on_message()---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@Yasaseru.event
async def on_message(message):
    if message.content == "hi":
        await message.channel.send('Hello, world!')

##-------------------start-of-sub_main()---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Yasaseru.run(token)