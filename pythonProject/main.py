# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import paho.mqtt.client as mqtt
from chatbot import ChatBot

import config


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    client_con("bedroom", "red")


def client_con(room, mode):
    client = mqtt.Client("light_up")
    client.connect(config.mqtt_host, config.mqtt_port, 300)
    client.loop_start()

    client.publish("lightUp/room", room)
    client.publish("lightUp/mode", mode)

    client.loop_stop()


def bot_con():
    chatbot = ChatBot(config.telegram_token)
    chatbot.send_room()




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    bot_con()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
