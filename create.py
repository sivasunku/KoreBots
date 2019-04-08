#This creates the data in csv format processName,TaskName,Starttime,EndTime,Status
# time will be min +1
# All other will be random from List
import random
import datetime

#Data Feed
procList = ['Equities_Daily','Equities_Monthly','Equities_Incremental','Equities_PostClose','Equities_Nightly']
taskList = ['PriceBand Changes','Reconciliation','BhavCopy','BlockDeals','SettlementStats','Ledger']
statusList = ['Disabled','Complete','Failure','Running','Waiting']
#A Process Starts at every hour from 9:00 in the morning daily & each task 2 mins to complete till 20:00 Hrs
# for that day

#Start time in "CCYY-MM-DD HH:MM:SS"
daily_stime = "01:00:00"
daily_etime = "20:00:00"
sdate = "2019-04-04"
edate = "2019-04-06"
step = datetime.timedelta(minutes = 10)
dt_stime = datetime.datetime.strptime(sdate + " " + daily_stime,'%Y-%m-%d %H:%M:%S')
dt_etime = datetime.datetime.strptime(edate + " " + daily_etime,'%Y-%m-%d %H:%M:%S')

comma = ","
procNo = 0
setId = 1
while dt_stime < dt_etime:
  #result.append(dt.strftime('%Y-%m-%d %H:%M:%S'))
  proc = procList[procNo]
  for i in range(len(taskList)):
    task = taskList[i]
    start = dt_stime
    end   = dt_stime + step
    status = statusList[random.randint(0,2)]
    record = str(setId) + comma + proc + comma + task + comma + start.strftime('%Y-%m-%d %H:%M:%S')  + comma
    record = record + end.strftime('%Y-%m-%d %H:%M:%S') + comma  + status
    print(record)
    dt_stime = end
  #Adjust the start time for next batch to nearest 2Hr
  procNo += 1
  procNo = procNo % len(procList)
  setId += 1
  #dt_stime = end.replace(minute=0) + datetime.timedelta(hours=1)
  if dt_stime.time() > datetime.datetime.strptime(daily_etime,"%H:%M:%S").time():
     dt_stime =  start.replace(hour=1,minute=0) + datetime.timedelta(days=1)
