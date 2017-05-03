# Project 6 Write Up
## Getting Started

#### To load up our Docker application, run:
```
./before_script.sh
```
This will:

* Load up the mysql container (10 sec delay before connecting)
* Load up the mysql-cmdline container (10 sec delay before connecting)
  - Create database and add necessary users/permissions
* Load up remaining containers, including:
  - __models__: django container that connects to mysql container to serve exp layer
  - __exp__: django container that connects to models container to serve web layer
  - __web__: django container that connects to exp layer to serve lb
  - __web2__: django container that connects to exp layer to serve lb
  - __es__: elastic search container to serve search functionality
  - __kafka__: kafka container to provide queueing service
  - __batch__: python container that listens for kafka listings and serves es, also contains haproxy config
  - __lb__: haproxy container for load balancing, users connect through lb
  - __selenium-chrome__: remote chrome driver for running selenium tests
  - __selenium__: python container for running selenium end-to-end tests
  - __jmeter__: jmeter container for running performance tests

#### To clean up our Docker application (when you're done), run:
 ```
 ./after_script.sh
 ```
This will:
* Decompose the Docker containers
* Remove the existing database directory

## Load Balancing with HAProxy
## Continuous Integration with Travis
## End-to-end Testing with Selenium
We wrote end-to-end tests using Selenium and integrated them into Travis CI by setting up a standalone Chrome remote driver (selenium-chrome), using one of Selenium's available docker containers. You can find more information [here.](https://github.com/SeleniumHQ/docker-selenium)
## Performance Testing with JMeter
We decided to implement performance testing with JMeter to see how fast our application would scale, both on the DigitalOcean and running locally. 

## Hosting on Digital Ocean
You can view our hosted app [here.](http://107.170.79.157:8000/)
