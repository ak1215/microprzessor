from paho.mqtt import client
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

import ClientConnection
import ColourManager


class ChatBot():

    def start(self, update: Update, context: CallbackContext) -> None:
        update.message.reply_text(
            "Hello " + update.message.chat.first_name + ", Welcome to LighUp.We are glad you chose us.Lets start configuring your home the way you want to. To find a list of the commands, type in /help.")

    def help_command(self, update: Update, context: CallbackContext) -> None:
        """Displays info on how to use the bot."""
        update.message.reply_text("""Commands:
        /show_settings: shows you options of different settings 
                                 available 
        how to use: /show_settings
        
        /show_colours: gives you an option of colors to choose from
        how to use: /show_colours
        
        /colour: changes room color according to your wish
        how to use: /colour {room name} {color you want}
        
        /setting: sets preset options for your lights
        how to use: /setting {room name} {setting name}

        /on: turns the lights on
        how to use: /on {room name}

        /off: turns the light off
        how to use:  /off {room name}""")

    def show_colours(self, update: Update, context: CallbackContext) -> None:
        update.message.reply_text(
            """Colours:
            red
            blue
            orange
            yellow
            green
            pink
            purple
            white""")

    def show_settings(self, update: Update, context: CallbackContext) -> None:
        update.message.reply_text(
            """Settings:
            These settings will make your house more fun
            morning: slowly turns on your light
            night: slowly dims your light till completely off
            reading: sets a warm environment for your eyes
            disco: changes all colours frequently to give a disco feel""")


    def on_command(self, update: Update, context: CallbackContext) -> None:
        ClientConnection.client_con(context.args[0], "on")

    def off_command(self, update: Update, context: CallbackContext) -> None:
        ClientConnection.client_con(context.args[0], "off")

    def change_colour(self, update: Update, context: CallbackContext) -> None:
        """Displays info on how to use the bot."""
        ClientConnection.client_con(context.args[0], context.args[1])

    def setting(self, update: Update, context: CallbackContext) -> None:
        ClientConnection.client_con(context.args[0], context.args[1])

    def send_room(self):
        return self.room

    def __init__(self, token):
        self.updater = Updater(token)
        # Create the Updater and pass it your bot's token.
        self.updater.dispatcher.add_handler(CommandHandler('start', self.start))
        # After start: name..., room...,
        self.updater.dispatcher.add_handler(CommandHandler('help', self.help_command))
        self.updater.dispatcher.add_handler(CommandHandler('colour', self.change_colour))
        self.updater.dispatcher.add_handler(CommandHandler('on', self.on_command))
        self.updater.dispatcher.add_handler(CommandHandler('off', self.off_command))
        self.updater.dispatcher.add_handler(CommandHandler('show_settings', self.show_settings))
        self.updater.dispatcher.add_handler(CommandHandler('show_colours', self.show_colours))
        self.updater.dispatcher.add_handler(CommandHandler('setting', self.setting))


        self.room = ""
        self.changed = False
        self.mode = ""

        # Start the Bot
        self.updater.start_polling()
