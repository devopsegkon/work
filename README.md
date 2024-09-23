# Fetch Take-Home Exercise — Site Reliability Engineering
The solution to the [take home exercise](https://fetch-hiring.s3.us-east-1.amazonaws.com/site-reliability-engineer/health-check.pdf) was written in Python.
The solution is the file [fetch.py](https://github.com/devopsegkon/work/blob/main/fetch.py) .

## How to Test the Solution

In order to test that the solution works, please follow the following instructions:

## Pre-requisites

1. Solution must be run on a mac machine.
2. Solution was tested using Python 3.12.5.

## How to Install the Solution

In order to run the solution, please follow the following steps:

1. Create a sub-directory on your mac.
2. Download [fetch tar gz file](https://drive.google.com/file/d/1OltztsIxGBSVqp1FlG7KEGbTA10QFfip/view?usp=drive_link) to the sub-directory you created.
3. Execute: 
   - tar -xzvf fetch.tar.gz
   - cd fetch
   - source fetch-int/bin/activate
   - cd fetch-int
   - python3 fetch.py <path-to-sample.yaml>

## Alternatively, skip the Install and just run the executable file. 

Alternatively, download the [file](https://drive.google.com/file/d/1nxRuCzfnv-6kguWHELEXbrsqqLTpM9Bb/view?usp=drive_link) fetch to a sub-directory on your mac. This file is an executable.  Run it as:

./fetch <path-to-sample.yaml>
