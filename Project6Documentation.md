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
Implementing continuous integration with Travis required building up the mysql containers in the docker-compose. As part of the before_script section, Travis builds up the application by creating a db directory, building the mysql and mysql-cmdline containers, and then composing the remaining containers. 

The main script runs the unit tests in the models container and E2E tests in the selenium container. 

There were lots of challenges getting Travis CI up and running due to setting the up the db containers, escaping special characters like '$', and setting up the correct user permissions. It was pretty cool to see the green light once it started working!

## E2E Testing with Selenium
We wrote end-to-end tests using Selenium and integrated them into Travis CI by setting up a standalone Chrome remote driver (selenium-chrome), using one of Selenium's available docker containers. You can find more information [here.](https://github.com/SeleniumHQ/docker-selenium)
## Performance Testing with JMeter
We decided to implement performance testing with JMeter to see how fast our application would scale, both on the DigitalOcean and running locally. 
### Test case overview
Go to the jmeter directory and with JMeter installed, you can open up the test file with the JMeter GUI via:
```
jmeter -t local-perf-test.jmx
```
* Users Config & Events Config
  - I created two config csv files for Users and Events that contain the form-data needed for logging in a user and creating an event.
* HTTP Cookie Manager
  - Allows for sessions to persist throughout performance test
* HTTP Request Defaults
  - Sets up base url for all HTTP requests (localhost:8000 for local test and lb:80 for docker tests)
* Various HTTP Request Samplers
  - These were used to set up a user's interaction (end-to-end) in the JMeter tests. 
  - First, we test the performance of accessing the home page and sign-in page.
  - Then, we sign the user in once during each iteration.
  - After, we perform various actions on the site, like accessing user dashboard, creating an event, and searching.
  - Finally, we log the user out once during each iteration.

### To run the tests with application running locally and generate reports
```
./run_local_perf.sh
```
Example output from running local jmeter tests:
```
summary +     34 in 00:00:12 =    2.8/s Avg:   120 Min:    17 Max:   329 Err:     0 (0.00%) Active: 1 Started: 4 Finished: 3
summary +     21 in 00:00:05 =    3.8/s Avg:   136 Min:    19 Max:   330 Err:     0 (0.00%) Active: 0 Started: 5 Finished: 5
summary =     55 in 00:00:18 =    3.1/s Avg:   126 Min:    17 Max:   330 Err:     0 (0.00%)
Tidying up ...    @ Wed May 03 14:33:36 EDT 2017 (1493836416755)
```
You can view results of the local perf test as a csv in local-perf-results-summary.csv or view the web interface by:
```
cd local-perf-results
open index.html
```
When you're done viewing the results, be sure to clean before running another test locally (clean_local_perf.sh is in app/jmeter).
```
./clean_local_perf.sh
```
### How the JMeter tests are run in the Docker container:

JMeter Docker container in docker-compose.yml:
```
jmeter:
  image: hauptmedia/jmeter
  container_name: jmeter
  links:
    - web
  volumes:
    - ./app/jmeter:/opt/jmeter/tests
  command: bash -c "bin/jmeter -n -t tests/docker-local-perf-test.jmx -l tests/docker-local-perf-results.log"
```
We created a duplicate of the local-perf-test.jmx file with the HTTP Default settings configured to test on the lb container (haproxy).

### Performance Analysis
#### Testing Web Application Locally
It was fun to mess with the number of threads (users), X, and ramp-up period (in secs), Y, to see how well our app could handle X requests in Y seconds. If Y < X, we ran into a bunch of errors, especially in the create event and search events (probably due to the images). To get 0.00% rate of error, Y had to be roughly 3X. There was about a 20.00% error rate with Y being around 2X.
#### Testing Web Application Digital Ocean

## Hosting on Digital Ocean
You can view our hosted app [here.](http://107.170.79.157:8000/)
