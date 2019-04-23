# This will load the initial data
python3.6 create.py  > /mntdata/KoreBots/data.csv
mysql -u root "-pSiva@1234" < load.sql
mysql -u root "-pSiva@1234" < status.sql

