# This will load the initial data
mysql -u root "-pSiva@1234" < /mntdata/KoreBots/status.sql
echo "#############################################" >> /mntdata/KoreBots/status.log 
echo "Ececuting status job at `date`               " >> /mntdata/KoreBots/status.log
