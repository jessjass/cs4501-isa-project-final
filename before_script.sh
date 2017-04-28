#!/bin/bash
mkdir db
docker-compose create mysql
docker-compose start mysql
sleep 10
docker-compose create mysql-cmdline
docker-compose start mysql-cmdline
sleep 10
docker exec -it mysql-cmdline bash -c "mysql -u root -p'\$3cureUS' -h db -e 'CREATE DATABASE cs4501;'"
docker exec -it mysql-cmdline bash -c "mysql -u root -p'\$3cureUS' -h db -e 'CREATE USER \"www\"@\"%\" IDENTIFIED BY \"\$3cureUS\";' "
docker exec -it mysql-cmdline bash -c "mysql -u root -p'\$3cureUS' -h db -e 'GRANT ALL ON cs4501.* TO \"www\"@\"%\";' "
docker exec -it mysql-cmdline bash -c "mysql -u root -p'\$3cureUS' -h db -e 'GRANT ALL ON test_cs4501.* TO \"www\"@\"%\";' "
docker-compose up -d models exp web kafka es batch
sleep 10
docker-compose up jmeter