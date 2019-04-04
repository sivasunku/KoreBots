-- Run this before below
python3.6 proc-create.py  > /home/siva_sunku_gmail_com/kore/test_db/proc-data.csv


USE employees;

CREATE TABLE proc_status (
   setid        int             NOT NULL,
   proc_name    VARCHAR(20)     NOT NULL,
   task_name    VARCHAR(4)      NOT NULL,
   start_time   DATETIME        NOT NULL,
   end_time     DATETIME        NOT NULL,
   Status       VARCHAR(20)     NOT NULL,
   PRIMARY KEY (setid)
);

LOAD DATA LOCAL INFILE "/home/siva_sunku_gmail_com/kore/test_db/proc-data.csv"
INTO TABLE proc_status
COLUMNS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
ESCAPED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

#What is running currently ?
select * 
  from proc_status
 where setid = (select setid
       from proc_status 
      where now() >= start_time
        and now() <= end_time)
    ;
#What is next process ?
select *
from proc_status as p,
    (select setid
       from proc_status 
      where now() >= start_time
        and now() <= end_time ) as c
where p.setid = c.setid  + 1
  ;
#What is left for today ?
select * 
  from proc_status as p,    
       (select setid
          from proc_status
         where now() >= start_time
           and now() <= end_time ) as c 
 where p.setid > c.setid 
  and date(start_time) = date(now());
# What all for today/tmorrow/yday
select * 
  from proc_status
 where subdate(current_date,-1) = date(start_time)
