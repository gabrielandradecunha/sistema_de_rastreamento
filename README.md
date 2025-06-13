# sistema de rastreamento de veiculos
Sistema de rastreamento veicular desenvolvido com FastAPI, utilizando o protocolo MQTT para comunicação com microcontroladores. A localização dos veículos é exibida em um mapa interativo por meio do GeoServer e da biblioteca OpenLayers.

<i>Vehicle tracking system developed with FastAPI, using the MQTT protocol for communication with microcontrollers. The location of vehicles is displayed on an interactive map through GeoServer and the OpenLayers library.</i>
<img src="image.png" />

## Setup
Up PostgreSQL and Geoserver container with docker-compose
```bash
sudo docker-compose up -d
```

Setup API and create database
```bash
cd api/
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 -m
```
Setup database
```bash
curl -X POST http://localhost:8000/setupdb
```
Create postgres trigger (oiptional)
```bash
sudo docker exec -it postgres_rastreamento psql -U postgres -d postgres -f /docker-entrypoint-initdb.d/init.sql
```