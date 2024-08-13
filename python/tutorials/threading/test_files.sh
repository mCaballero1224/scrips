#!/bin/bash

for i in {1..9}
do
	touch "./test${i}.txt"
	echo "id" > "./test${i}.txt"
done

echo "Test files created."
