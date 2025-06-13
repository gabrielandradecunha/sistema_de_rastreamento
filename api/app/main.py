from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import users
import os
from dotenv import load_dotenv
from app.core.setupdb import setupdb
from app.models.User import User
import paho.mqtt.client as mqtt
import threading
import json

load_dotenv()
url_frontend = os.getenv('URL_FRONTEND')

######################################### mqtt ##################################

def call_mqtt():

    user = os.getenv('MOSQUITTO_USER')
    password = os.getenv('MOSQUITTO_PASSWORD')
    mqtt_host = os.getenv('MOSQUITTO_HOST')
    mqtt_port = os.getenv('MOSQUITTO_PORT')
    mqtt_topic = os.getenv('MOSQUITTO_TOPIC')

    def on_connect(client, userdata, flags, reason_code, properties):
        print(f"MQTT broker conected with result code: {reason_code}")
        client.subscribe(mqtt_topic)

    def on_disconnect(client, userdata, rc):
        print("MQTT broker disconnected with result code: %s", rc)

    def on_message(client, userdata, msg):
        print(f"Topic: {msg.topic}")

        json_string = msg.payload
        data = json.loads(json_string)

        User.update(data["email"], data["longitude"], data["latitude"])

    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    # caso nao usar broker publico
    #client.username_pw_set(user, password)
    client.connect(str(mqtt_host), int(mqtt_port), 60)

    # tls opcional
    #client.tls_set()

    client.on_connect = on_connect
    client.on_message = on_message

    def run_mqtt():
        client.loop_forever()

    mqtt_thread = threading.Thread(target=run_mqtt)
    mqtt_thread.daemon = True
    mqtt_thread.start()

call_mqtt()

##################################################################################


app = FastAPI()

origins = [
    str(url_frontend), 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

app.include_router(users.router, tags=["getuser"])

@app.get("/")
def read_root():
    return {"message": "API para o sistema de rastreamento de veiculos"}

@app.get("/setupdb")
def setup_db():
    setupdb()