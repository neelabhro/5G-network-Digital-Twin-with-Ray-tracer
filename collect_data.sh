#!/bin/bash

# Set the time t in seconds 
t=1

n=5 # measurement samples taken 

while true
do
for ((i=1; i<=n; i++))
do
	# Change for script to run 
	python rsrp_measure.py 
#	sudo kill -9 $(lsof -t)
	python sinr_measure.py
#	sleep $t
done
	read -n 1 -s -r -p "press for next measurement"
done
#w=30

#sleep $w

#for ((i=1; i<=n; i++))
#do 
#	python rsrp.py
#
#	sleep $t

#done
