import pandas as pd
import numpy as np
import json;
from datetime import datetime
import matplotlib.pyplot as plt
import scipy.signal as signal
import seaborn as sns

'''to open the json file'''
file=['Elga.json','mayukha.json','Prathibha.json','Sharika.json','Vishakh.json']
for i in range(len(file)):
    f = open(file[i])
    dic = json.load(f)

#Question 2
    print(dic['captured_data'].keys())
    print(dic['captured_data']['hr'].keys())
    print(dic['captured_data']['slp'].keys())
    print(dic['captured_data']['act'].keys())
    print(dic['captured_data']['bat'].keys())
    print(dic['captured_data']['err'].keys())

    time_in_millis=dic['captured_data']['hr']['RR in ms']
    bpm=dic['captured_data']['hr']['HR in BPM']

    '''Python code to get the Cumulative sum of a list'''
    new_list_time=[]
    j=0
    for i in range(0,len(time_in_millis)):
        j+=time_in_millis[i]
        new_list_time.append(j)

    milli_second=new_list_time[-1]
    print(milli_second)
    print(dic['Start_date_time'])
    start_date_time=dic['Start_date_time']
    date_str = start_date_time

    '''Conversion of UTC to IST'''
    str(date_str).replace('+00:00', 'Z')
    time_object = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ')
    time_obj = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ').time() 
    print(time_object)  
    print(time_obj)
    print(type(time_obj))
    Seconds=(milli_second/1000)
    print(type(Seconds))

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
    plt.figure(figsize=(15,8))
    sns.scatterplot(data=temp, x="cumtime", y="bpm")
    plt.show()

#Question 3
    '''Heart rate has been colored if the step count is above 5'''
    step_count=dic['captured_data']['act']['step count']
    print(type(step_count))
    print(len(step_count))
    new_list_time=np.array(new_list_time)/1000 #to seconds
    bpm=np.array(bpm)
    new_step_count=step_count[0:int(new_list_time[-1]/10)]
    print(len(new_step_count))
    for i in range(1,len(new_step_count)):
        x=new_list_time[(new_list_time > i* 10) & (new_list_time <= (i+1)* 10)].tolist()
        y=bpm[(new_list_time > i* 10) & (new_list_time <= (i+1)* 10)].tolist()
        if new_step_count[i]>5:
            plt.plot(x,y,color="red")
        else:
            plt.plot(x,y,color="blue")

    plt.show()
    '''To filter the above signal'''
    filter_order=12
    cutoff_frequency=0.05
    B, A= signal.butter(filter_order,cutoff_frequency,output='ba')
    filtered_signal=signal.filtfilt(B,A,bpm)
    print(len(filtered_signal))
    for i in range(1,len(new_step_count)):
        x=new_list_time[(new_list_time > i* 10) & (new_list_time <= (i+1)* 11)]
        y=filtered_signal[(new_list_time > i* 10) & (new_list_time <= (i+1)* 11)]
        if new_step_count[i]>5:
            plt.plot(x,y,color="red")
        else:
            plt.plot(x,y,color="blue")
    plt.show()

    '''To Plot the Step count using ticks'''
    ticks=dic['captured_data']['act']['ticks']
    print(len(ticks))
    print(type(ticks))
    int_tick_list=[] #interger values of ticks
    for i in range(len(ticks)):
        tick_int=int(ticks[i])
        int_tick_list.append(tick_int)
    print(len(int_tick_list))
    sample=np.array(int_tick_list)/512
    print(sample)
    cumulative = sample.cumsum().tolist()
    tickdf = pd.DataFrame(sample,columns = ['time_in_sec'])
    tickdf['delta'] = pd.to_timedelta(tickdf["time_in_sec"], unit="S")
    tickdf['cumsum'] = tickdf['delta'].cumsum()
    tickdf['reference'] = ist_dt
    tickdf['cumtime'] = tickdf['reference'] + tickdf['cumsum']
    tickdf['stepcount'] = dic['captured_data']['act']['step count']
    plt.figure(figsize=(15,8))
    sns.scatterplot(data=tickdf, x="cumtime", y="stepcount")
    plt.show()