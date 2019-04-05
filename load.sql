
USE employees;
drop table proc_status;

CREATE TABLE proc_status (
   setid        int             NOT NULL,
   proc_name    VARCHAR(30)     NOT NULL,
   task_name    VARCHAR(30)      NOT NULL,
   start_time   DATETIME        NOT NULL,
   end_time     DATETIME        NOT NULL,
   Status       VARCHAR(20)     NOT NULL,
   PRIMARY KEY (setid,proc_name,task_name,start_time,end_time)
);
LOAD DATA LOCAL INFILE "/home/siva_sunku/KoreBots/data.csv"
INTO TABLE proc_status
COLUMNS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
ESCAPED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;
