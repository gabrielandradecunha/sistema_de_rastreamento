#!/bin/bash

# script sh to create tables 

sudo docker exec -it postgres_rastreamento psql -U postgres -c 'CREATE TABLE IF NOT EXISTS users (
                                                                id SERIAL PRIMARY KEY,
                                                                nome VARCHAR(100),
                                                                email VARCHAR(100) UNIQUE,
                                                                senha VARCHAR(100),
                                                                longitude DOUBLE PRECISION,
                                                                latitude DOUBLE PRECISION
                                                            )'