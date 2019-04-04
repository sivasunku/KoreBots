from flask import Flask, jsonify
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Siva@1234'
app.config['MYSQL_DATABASE_DB'] = 'employees'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)
# Normal starting
@app.route('/')
def help():
    str1 = "For Specific employee details choose - /employeeDetails/empno"
    str2 = "For employee drawing max salary - /employeeDetails/maxSal"
    str3 = "For employee drawing max salary - /employeeDetails/minSal" 
    str4 = "For  count of employees in each department - /employeeDetails/deptCount"
    str5 = "For Process /process/current"
    nl = "\n"
    return str1 + nl + str2 + nl + str3 + nl + str4 + nl + str5 + nl

# Details of employee
@app.route('/employeeDetails/<empid>',methods=['GET'])
def getEmployee(empid):
    cur = mysql.connect().cursor()
    query = "select * from employees where emp_no = " + empid
    cur.execute(query)
    r = [dict((cur.description[i][0], value)
              for i, value in enumerate(row)) for row in cur.fetchall()]
    return jsonify({'myCollection' : r})

# Max Salary
@app.route('/employeeDetails/maxSal',methods=['GET'])
def getMaxSal():
    cur = mysql.connect().cursor()
    query = "select * from employees \
              where emp_no = (select emp_no from salaries where salary = (select max(salary) from salaries));"
    cur.execute(query)
    r = [dict((cur.description[i][0], value)
              for i, value in enumerate(row)) for row in cur.fetchall()]
    return jsonify({'myCollection' : r})

# Min Salary
@app.route('/employeeDetails/minSal',methods=['GET'])
def getMinSal():
    cur = mysql.connect().cursor()
    query = "select * from employees \
              where emp_no = (select emp_no from salaries where salary = (select min(salary) from salaries));"
    cur.execute(query)
    r = [dict((cur.description[i][0], value)
              for i, value in enumerate(row)) for row in cur.fetchall()]
    return jsonify({'myCollection' : r})

# department Counts
@app.route('/employeeDetails/deptCount',methods=['GET'])
def getDeptCount():
    cur = mysql.connect().cursor()
    query = """select dept_name,grp.*  
               from ( (select dept_no,gender,count(*) 
                         from ( (select de.*,gender 
                                   from  dept_emp as de  
                                        ,employees as e  
                                  where de.emp_no = e.emp_no) as base) 
                        group by dept_no,gender) as grp), departments as d 
               where d.dept_no = grp.dept_no; """
    cur.execute(query)
    r = [dict((cur.description[i][0], value)
              for i, value in enumerate(row)) for row in cur.fetchall()]
    #return jsonify('myCollection' : r})
    return jsonify(r)

# department Salaries
@app.route('/employeeDetails/deptCost',methods=['GET'])
def getDeptCost():
    cur = mysql.connect().cursor()
    query = """select dept_name,grp.*  
               from ( (select dept_no,FORMAT(sum(salary),0) as SalarySum
                         from ( (select de.*,salary
                                   from  dept_emp as de  
                                        ,employees as e  
                                        ,salaries as sal
                                  where de.emp_no = e.emp_no
                                    and sal.emp_no = e.emp_no LIMIT 200) as base ) 
                        group by dept_no) as grp), departments as d 
               where d.dept_no = grp.dept_no;
    """

    cur.execute(query)
    r = [dict((cur.description[i][0], value)
              for i, value in enumerate(row)) for row in cur.fetchall()]
    #return jsonify('myCollection' : r})
    return jsonify(r)
####################################################################################################
# Process Related APIs
####################################################################################################

#Get Current task - Only particular task, not the process
@app.route('/process/Subtask',methods=['GET'])
def getProcessSubtask():
    cur = mysql.connect().cursor()
    query = """
      select *
        from proc_status
       where now() >= start_time
         and now() <= end_time
      ;
    """
    cur.execute(query)
    r = [dict((cur.description[i][0], value)
              for i, value in enumerate(row)) for row in cur.fetchall()]
    return jsonify({'myCollection' : r})

#Get Current Process - This gets the whole process subtask is part of
@app.route('/process/ProcessState',methods=['GET'])
def getProcessProcessStatus():
    cur = mysql.connect().cursor()
    query = """select *
  from proc_status
 where setid = (select setid
       from proc_status
      where now() >= start_time
        and now() <= end_time)
    ;
    """
    cur.execute(query)
    r = [dict((cur.description[i][0], value)
              for i, value in enumerate(row)) for row in cur.fetchall()]
    return jsonify(r)

#Get Current Process - This gets the whole process subtask is part of
@app.route('/process/ProcessNext',methods=['GET'])
def getProcessNext():
    cur = mysql.connect().cursor()
    query = """
      select *
        from proc_status as p,
            (select setid
               from proc_status
              where now() >= start_time
                and now() <= end_time ) as c
       where p.setid = c.setid  + 1
      ;
    """
    cur.execute(query)
    r = [dict((cur.description[i][0], value)
              for i, value in enumerate(row)) for row in cur.fetchall()]
    return jsonify(r)

#Schedule of today/yesterday/tomorrow/given date
@app.route('/process/schedule/<when>',methods=['GET'])
def getProcessSchedule(when):
    cur = mysql.connect().cursor()
    reqDate = "date(now())"
    if (when == 'tomorrow'):
      reqDate = "subdate(current_date,-1)"
    elif (when == 'yesterday'):
      reqDate = "subdate(current_date,1)"
    elif (when == 'today'):
      reqDate = "date(now())"
    else:
      reqDate = "date('" + when + "')"
    query = """
      select *
        from proc_status
       where date(start_time) = """ + reqDate + ";"
    print("query  Here", query) 
    cur.execute(query)
    r = [dict((cur.description[i][0], value)
              for i, value in enumerate(row)) for row in cur.fetchall()]
    return jsonify(r)



if __name__ == '__main__':
    app.run(debug = False,host = '0.0.0.0')
