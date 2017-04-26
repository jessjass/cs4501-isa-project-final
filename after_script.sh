#!/bin/bash
docker-compose down
docker rm $(docker ps -a -q) -f
rm -rf db