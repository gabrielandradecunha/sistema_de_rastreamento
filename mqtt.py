import json
import threading
import psycopg2
import paho.mqtt.client as mqtt


DB_CONFIG = {
    "host": "localhost",
    "database": "rastreamento",
    "user": "postgres",
    "password": "postgres",
    "port": 5433
}

def get_connection():
    return psycopg2.connect(**DB_CONFIG)

#########################################
# MQTT
#########################################

MQTT_HOST = "test.mosquitto.org"
MQTT_PORT = 1883
MQTT_TOPIC = "teste/mqtt/rastreamento"

def start_mqtt_consumer():

    def on_connect(client, userdata, flags, reason_code, properties):
        print(f"[MQTT] Connected with code {reason_code}")
        client.subscribe(MQTT_TOPIC)

    def on_message(client, userdata, msg):
        try:
            payload = msg.payload.decode("utf-8")
            print(f"[MQTT] Payload: {payload}")

            data = json.loads(payload)

            email = data["email"]
            longitude = data["longitude"]
            latitude = data["latitude"]

            conn = get_connection()
            cursor = conn.cursor()

            # atualiza usuário
            cursor.execute("""
                UPDATE users
                SET longitude = %s, latitude = %s
                WHERE email = %s
            """, (longitude, latitude, email))

            conn.commit()
            cursor.close()
            conn.close()

            print("[DB] Localização atualizada com sucesso")

        except Exception as e:
            print(f"[ERROR] {e}")

    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(MQTT_HOST, MQTT_PORT, 60)

    thread = threading.Thread(target=client.loop_forever)
    thread.daemon = True
    thread.start()

#########################################
# starting
#########################################

if __name__ == "__main__":
    print("[SYSTEM] Starting MQTT consumer...")
    start_mqtt_consumer()

    while True:
        pass
