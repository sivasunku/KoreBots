#! /bin/bash
mysql -u root "-pSiva@1234" < /home/siva_sunku_gmail_com/kore/test_db/proc-update.sql
logFile='/home/siva_sunku_gmail_com/kore/test_db/update.log'
echo "##################################################" >> $logFile
echo "Starting the update process at  `date` " >> $logFile
