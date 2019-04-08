use employees;

-- For all the current running tasks & one after add 30min delay
update proc_status
   set end_time = date_add(end_time,interval 30 minute)
 where end_time > now()
   and date(end_time) = date(now())
 ;
update proc_status
   set start_time = date_add(start_time,interval 30 minute)
 where start_time > now()
   and date(start_time) = date(now())
 ;
