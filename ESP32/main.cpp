#include <WiFi.h>
#include <PubSubClient.h>
#include <TinyGPS++.h>
#include <HardwareSerial.h>

const char* ssid = "ssd";
const char* password = "senha";

//mosquitto broker
const char* mqtt_server = "test.mosquitto.org";
const int mqtt_port = 1883;
const char* mqtt_topic = "teste/cuiaba/rastreamento";

WiFiClient espClient;
PubSubClient client(espClient);

TinyGPSPlus gps;
HardwareSerial gpsSerial(1);

void setup_wifi() {
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }
}

void reconnect_mqtt() {
  while (!client.connected()) {
    String clientId = "ESP32Client-" + String(random(0xffff), HEX);
    client.connect(clientId.c_str());
    delay(2000);
  }
}

void publish_location(double latitude, double longitude) {
  String json = "{\"email\":\"dispositivo@esp32.com\",\"latitude\":" + String(latitude, 6) + ",\"longitude\":" + String(longitude, 6) + "}";
  client.publish(mqtt_topic, json.c_str());
}

void setup() {
  Serial.begin(115200);
  gpsSerial.begin(9600, SERIAL_8N1, 16, 17);
  setup_wifi();
  client.setServer(mqtt_server, mqtt_port);
}

void loop() {
  if (!client.connected()) {
    reconnect_mqtt();
  }
  client.loop();

  while (gpsSerial.available() > 0) {
    char c = gpsSerial.read();
    gps.encode(c);
  }

  if (gps.location.isUpdated()) {
    double lat = gps.location.lat();
    double lon = gps.location.lng();
    publish_location(lat, lon);
    delay(10000);
  }
}
