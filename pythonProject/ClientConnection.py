import paho.mqtt.client as mqtt

import config
from Room import Room


def client_con(room, mode):
    global start, end
    client = mqtt.Client("light_up")
    client.connect(config.mqtt_host, config.mqtt_port, 300)
    client.loop_start()

    if room == "kitchen":
        start = 1
        end = 15
        space_finder(client,start, end)

        Room.KITCHEN = mode
        client.publish("lightUp/room/kitchen", Room.KITCHEN)


    elif room == "bedroom":
        start = 16
        end = 30
        space_finder(client,start, end)

        Room.BEDROOM = mode
        client.publish("lightUp/room/bedroom", Room.BEDROOM)


    elif room == "office":
        start = 31
        end = 45
        space_finder(client,start, end)

        Room.OFFICE = mode
        client.publish("lightUp/room/office", Room.OFFICE)


    elif room == "livingroom":
        start = 46
        end = 60
        space_finder(client,start, end)

        Room.LIVINGROOM = mode
        client.publish("lightUp/room/livingroom", Room.LIVINGROOM)










    client.loop_stop()


def space_finder(client, start, end):
    client.publish("lightUp/start", start)
    client.publish("lightUp/end", end)