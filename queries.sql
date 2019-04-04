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

