use employees;

-- For all the past update with random 
update proc_status
   set Status = ELT(1 + RAND() *2 , 'Disabled','Complete','Failure')
 where end_time < now()
 ;

-- For all current ones 'running'
update proc_status
   set Status = 'Running'
 where start_time <= now()
   and end_time >= now()
 ;

-- For all future ones random of 'Disabled,Waiting'
update proc_status
   set Status = ELT(1 + RAND()*2 ,'Waiting','Waiting','Waiting')
 where start_time > now()
 ;
