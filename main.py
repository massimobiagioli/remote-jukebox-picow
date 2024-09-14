import time
import ubinascii
from umqtt.simple import MQTTClient
import random
import config
import json
import uart_mp3


client_id = ubinascii.hexlify(machine.unique_id())
TOPIC = b"jukebox"

MP3_DEFAULT_VOLUME=15


def sub_cb(topic, msg):
    json_message = json.loads(msg.decode('utf-8'))
    play(json_message["folderNumber"], json_message["songNumber"])


def send_uart_command(command):
    uart.write(bytearray.fromhex(command))
    

def play(folder_number, song_number):
    uart_mp3.play_with_folder_and_filename(folder_number, song_number)


def reset():
    print("Resetting...")
    time.sleep(5)
    machine.reset()
    

def init_uart_mp3_player():
    uart_mp3.reset()
    uart_mp3.set_volume(MP3_DEFAULT_VOLUME)
    

def main():
    print("Init Serial for UART communication")
    
    print(f"Begin connection with MQTT Broker :: {config.mqtt["broker"]}")
    mqtt_client = MQTTClient(
        client_id,
        config.mqtt["broker"],
    )
    mqtt_client.set_callback(sub_cb)
    mqtt_client.connect()
    mqtt_client.subscribe(TOPIC)
    print(f"Connected to MQTT  Broker :: {config.mqtt["broker"]}, and waiting for callback function to be called!")
    
    print("Init UART mp3 player")
    init_uart_mp3_player()
    
    
    while True:
        mqtt_client.check_msg()
        time.sleep(.2)
    

if __name__ == "__main__":    
    while True:
        try:
            main()
        except OSError as e:
            print("Error: " + str(e))
            reset()