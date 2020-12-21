#!/bin/bash

docker-compose up -d --build
docker port web
