use employees;

-- Delay the current process by 30 mins. Push all next tasks by 30min
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
   set Status = ELT(1 + RAND()*2 ,'Disabled','Waiting','Waiting')
 where start_time > now()
 ;
