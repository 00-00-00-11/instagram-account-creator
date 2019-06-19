from modules.config import Config
from modules.requestbot import runBot
from modules.seleniumbot import runbot


def accountCreator():
    if Config["bot_type"] == 1:
        runbot()
    else:
        runBot()

try:
    accountCreator()
except KeyboardInterrupt:
    print("Exiting gracefully.")
