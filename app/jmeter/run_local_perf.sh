#!/bin/bash
jmeter -n -t LocalPerformanceTest.jmx -l local-perf-results.log -e -o local-perf-results