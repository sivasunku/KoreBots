#Given details of employee given name
  select *
    from employees
  where emp_no = '10008';

#Get employee drawing max salary
  select * 
  from employees 
  where emp_no = (select emp_no from salaries where salary = (select max(salary) from salaries)); 

#Get employee drawing min salary
  select * 
  from employees 
  where emp_no = (select emp_no from salaries where salary = (select max(salary) from salaries)); 

#Get number of employees per department
select a.dept_no,a.dept_name,b.counts
  from departments as a, (select dept_no, count(emp_no) as counts from dept_emp group by dept_no) as b
 where a.dept_no = b.dept_no;

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

