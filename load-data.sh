#! /usr/bash
# This will load the initial data
python3.6 create.py  > data.csv
mysql -u root "-pSiva@1234" < load.sql

