from machine import I2C, Pin
from esp8266_i2c_lcd import I2cLcd
from umqtt.simple import MQTTClient
import time

i2c = I2C(scl=Pin(5), sda=Pin(4))
lcd = I2cLcd(i2c, 0x27, 2, 16)

CONFIG = {
    "broker": "123.*.*.*",
    "client_id": b"NodeMCU",
    "topic": b"message",
}

def print_message(topic, msg):
	print("Received: " + msg.decode('UTF-8'))
	lcd.clear()
	lcd.putstr(msg.decode('UTF-8'))


client = MQTTClient(CONFIG['client_id'], CONFIG['broker'])	
client.set_callback(print_message)
client.connect()
print("waiting for message")
client.subscribe(CONFIG['topic'])
while True:
	client.wait_msg()
	time.sleep(1)
client.disconnect()

