from bdb import set_trace
from turtle import color
import pandas as pd
import numpy as np
import json;
from datetime import datetime
import matplotlib.pyplot as pt
import matplotlib.dates


#to open the json file
f = open('Elga.json')
# returns JSON object as 
# a dictionary
dic = json.load(f)

#hour to seconds conversion
def convertToSeconds(hours, minutes, seconds):
  return int(hours) * 60 * 60 + int(minutes) * 60 + int(seconds)

#convert seconds to hours
def convert(seconds):
    min, sec = divmod(seconds, 60)
    hour, min = divmod(min, 60)
    return '%d:%02d:%02d' % (hour, min, sec)
     


#Question 2
print(dic['captured_data'].keys())
print(dic['captured_data']['hr'].keys())
print(dic['captured_data']['slp'].keys())
print(dic['captured_data']['act'].keys())
print(dic['captured_data']['bat'].keys())
print(dic['captured_data']['err'].keys())


#print(len(dic['captured_data']['hr']['RR in ms']))
#print(len(dic['captured_data']['hr']['HR in BPM']))
#print(dic['captured_data']['hr']['RR in ms'])
#print(dic['captured_data']['hr']['HR in BPM'])
#print(type(dic['captured_data']['hr']['RR in ms']))
#print(type(dic['captured_data']['hr']['HR in BPM']))
time_in_millis=dic['captured_data']['hr']['RR in ms']
bpm=dic['captured_data']['hr']['HR in BPM']
print(len(bpm))
# Python code to get the Cumulative sum of a list
new_list=[]
j=0
for i in range(0,len(time_in_millis)):
    j+=time_in_millis[i]
    new_list.append(j)

milli_second=new_list[-1]
print(milli_second)
print(dic['Start_date_time'])
start_date_time=dic['Start_date_time']
print(dic['session_finish_time'])
session_finish_time=dic['session_finish_time']
date_str = start_date_time
str(date_str).replace('+00:00', 'Z')
time_object = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ')
time_obj = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ').time() 
print(time_object)  
print(time_obj)
print(type(time_obj))
end_str = session_finish_time
str(end_str).replace('+00:00', 'Z')
end_object = datetime.strptime(end_str, '%Y-%m-%dT%H:%M:%SZ')
end_obj = datetime.strptime(end_str, '%Y-%m-%dT%H:%M:%SZ').time() 
print(end_object)  
print(end_obj)
print(type(end_obj))



temp = pd.DataFrame(time_in_millis,columns = ['time_in_ms'])
from datetime import datetime, timezone
import pytz
local = pytz.timezone("UTC")
local_dt = local.localize(time_object, is_dst=None)
utc_dt = local_dt.astimezone(pytz.utc)
ist_dt = local_dt.astimezone(pytz.timezone('Asia/Kolkata'))
utc_dt,ist_dt
temp['delta'] = pd.to_timedelta(temp["time_in_ms"], unit="ms")
temp['cumsum'] = temp['delta'].cumsum()
temp['reference'] = ist_dt
temp['cumtime'] = temp['reference'] + temp['cumsum']
temp['bpm'] = bpm
import seaborn as sns
from matplotlib import pyplot as plt

# plt.figure(figsize=(15,8))
# sns.scatterplot(data=temp, x="cumtime", y="bpm")
# plt.show()

# utc_dic=dic.astimezone(datetime.timezone.utc)
# print(utc_dic)
# from datetime import datetime, timedelta


# n_sec=1
# date = time_obj + timedelta(seconds=n_sec)
# print(date)

# string=str(time_obj)
# hours, minutes, secondss= string.split(':')
# converted_seconds=convertToSeconds(hours,minutes,secondss)
# # print(a)

# seconds=str(milli_second/1000)
# seconds=milli_second/1000
# # print(seconds)
# print(type(seconds))
# new_seconds=seconds+converted_seconds
# print("Seconds",new_seconds)

# import datetime
# utc_time=datetime.datetime.fromtimestamp(new_seconds).strftime('%Y-%m-%d %H:%M:%S')
# print(utc_time)
# from datetime import datetime
# new_utctime = datetime.strptime(utc_time, '%Y-%m-%d %H:%M:%S').time()
# print(new_utctime)

# pt.scatter(new_utctime,dic['captured_data']['hr']['HR in BPM'],color = 'red')

#Question 3
# import pdb; pdb.set_trace()
import matplotlib.pyplot as plt
step_count=dic['captured_data']['act']['step count']
print(type(step_count))
print(len(step_count))
new_list=np.array(new_list)/1000
bpm=np.array(bpm)
new=step_count[0:int(new_list[-1]/10)]
print(len(new))
# import scipy.signal as signal
# import matplotlib.pyplot as plt
# filter_order=4
# cutoff_frequency=0.05
# B, A= signal.butter(filter_order,cutoff_frequency,output='ba')
# filtered_signal=signal.filtfilt(B,A,new)

# x=new_list[(new_list > i* 10) & (new_list <= (i+1)* 10)]
# y=bpm[(new_list > i* 10) & (new_list <= (i+1)* 10)]
filtered_x=[]
filtered_y=[]
for i in range(len(new)):
  x=new_list[(new_list > i* 10) & (new_list <= (i+1)* 10)].tolist()
  y=bpm[(new_list > i* 10) & (new_list <= (i+1)* 10)].tolist()
  # import pdb;pdb.set_trace()
  # plt.plot(new_list[(new_list > i* 10) & (new_list <= (i+1)* 10)],bpm[(new_list > i* 10) & (new_list <= (i+1)* 10)])
  if new[i]>5:
    plt.plot(x,y,color="red")
  else:
    plt.plot(x,y,color="blue")
  # filtered_x.append(x)
  # filtered_y.append(y)

plt.show()
li=sum(filtered_y,[])
# print(li)
# import pdb;pdb.set_trace()
import scipy.signal as signal
import matplotlib.pyplot as plt
filter_order=10
cutoff_frequency=0.05
B, A= signal.butter(filter_order,cutoff_frequency,output='ba')
filtered_signal=signal.filtfilt(B,A,bpm)
# import pdb;pdb.set_trace()
# lit=li[-3:-1]
# print(lit)
# import pdb;pdb.set_trace()
# filtered_signal=np.append(filtered_signal,lit)
print(filtered_signal)
print(len(filtered_signal))
# print(len(filtered_x))
# print(len(filtered_y))
# print(len(li))
for i in range(len(new)):
  x=new_list[(new_list > i* 10) & (new_list <= (i+1)* 10)]
  y=filtered_signal[(new_list > i* 10) & (new_list <= (i+1)* 10)]
  # import pdb;pdb.set_trace()
  # plt.plot(new_list[(new_list > i* 10) & (new_list <= (i+1)* 10)],bpm[(new_list > i* 10) & (new_list <= (i+1)* 10)])
  if new[i]>5:
    plt.plot(x,y,color="red")
  else:
    plt.plot(x,y,color="blue")
# plt.plot(filtered_signal)

plt.show()
# f0 = 1000.0  # Frequency to be removed from signal (Hz)
# Q = 30.0  # Quality factor
# fs=20000
# w0 = f0/(fs/2)  # Normalized Frequency
# # Design notch filter
# b, a = signal.iirnotch(w0, Q)
# zi = signal.lfilter_zi(b, a)
# z, _ = signal.lfilter(b, a, y, zi=zi*y[0])
# z2, _ = signal.lfilter(b, a, z, zi=zi*z[0])
# y1 = signal.filtfilt(b, a, y)
# plt.plot(x,y1)
# plt.show()

'''To Plot the Step count'''
ticks=dic['captured_data']['act']['ticks']
print(len(ticks))
print(type(ticks))
int_tick_list=[] #interger values of ticks
for i in range(len(ticks)):
  tick_int=int(ticks[i])
  int_tick_list.append(tick_int)
print(len(int_tick_list))
# int_tick_list.insert(0,0)
# tick_difference_list=[]
# for i in range(len(int_tick_list)):
  # tick_difference=int_tick_list[i]-int_tick_list[i-1]
  # tick_difference_list.append(int_tick_list[i]-int_tick_list[i-1])
# print(len(tick_difference_list))
# print(tick_difference_list)
tick_diff_list = []
for x, y in zip(int_tick_list[0::], int_tick_list[1::]):
  tick_diff_list.append(y-x)
print(tick_diff_list)
      
sample=np.array(tick_diff_list)/512
print(sample)
cumulative = sample.cumsum().tolist()
print(cumulative)
