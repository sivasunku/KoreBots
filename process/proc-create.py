#This creates the data in csv format processName,TaskName,Starttime,EndTime,Status
# time will be min +1
# All other will be random from List
import random
import datetime

#Data Feed
procList = ['ProcessA','ProcessB','ProcessC','ProcessD']
taskList = ['Task1','Task2','Task3','Task4']
statusList = ['Running','Waiting','Disabled']

#Start time in "CCYY-MM-DD HH:MM:SS"
stime = "2019-04-02 00:00:00"
etime = "2019-04-05 23:59:00"
step = datetime.timedelta(minutes = 30)
dt_stime = datetime.datetime.strptime(stime,'%Y-%m-%d %H:%M:%S')
dt_etime = datetime.datetime.strptime(etime,'%Y-%m-%d %H:%M:%S')

comma = ","
procNo = 0
setId = 1
while dt_stime < dt_etime:
  #result.append(dt.strftime('%Y-%m-%d %H:%M:%S'))
  proc = procList[procNo]
  N = random.randint(1,4)
  for i in range(N):
    task = taskList[i]
    start = dt_stime
    end   = dt_stime + step
    status = statusList[random.randint(0,2)]
    record = str(setId) + comma + proc + comma + task + comma + start.strftime('%Y-%m-%d %H:%M:%S')  + comma
    record = record + end.strftime('%Y-%m-%d %H:%M:%S') + comma  + status
    print(record)
    dt_stime = end
  procNo += 1
  procNo = procNo % len(procList)
  setId += 1
