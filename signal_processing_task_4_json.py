import pandas as pd
import numpy as np
import json;
from datetime import datetime
import matplotlib.pyplot as plt
#to open the json file
file=['Elga.json','mayukha.json','Prathibha.json','Sharika.json','Vishakh.json']
for i in range(len(file)):
    f = open(file[i])
# returns JSON object as 
# a dictionary
    dic = json.load(f)

#Question 2
    print(dic['captured_data'].keys())
    print(dic['captured_data']['hr'].keys())
    print(dic['captured_data']['slp'].keys())
    print(dic['captured_data']['act'].keys())
    print(dic['captured_data']['bat'].keys())
    print(dic['captured_data']['err'].keys())


# #print(len(dic['captured_data']['hr']['RR in ms']))
# #print(len(dic['captured_data']['hr']['HR in BPM']))
# #print(dic['captured_data']['hr']['RR in ms'])
# #print(dic['captured_data']['hr']['HR in BPM'])
# #print(type(dic['captured_data']['hr']['RR in ms']))
# #print(type(dic['captured_data']['hr']['HR in BPM']))
    time_in_millis=dic['captured_data']['hr']['RR in ms']
    bpm=dic['captured_data']['hr']['HR in BPM']

# # Python code to get the Cumulative sum of a list
    new_list=[]
    j=0
    for i in range(0,len(time_in_millis)):
        j+=time_in_millis[i]
        new_list.append(j)

    milli_second=new_list[-1]
    print(milli_second)
    print(dic['Start_date_time'])
    start_date_time=dic['Start_date_time']

    date_str = start_date_time
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
    import seaborn as sns
    from matplotlib import pyplot as plt

    plt.figure(figsize=(15,8))
    sns.scatterplot(data=temp, x="cumtime", y="bpm")
    plt.show()

#Question 3
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
        filtered_x.append(x)
        filtered_y.append(y)

    plt.show()
    li=sum(filtered_y,[])
    print(li)
# import pdb;pdb.set_trace()
    import scipy.signal as signal
    import matplotlib.pyplot as plt
    filter_order=4
    cutoff_frequency=0.05
    B, A= signal.butter(filter_order,cutoff_frequency,output='ba')
    filtered_signal=signal.filtfilt(B,A,li)
    # import pdb;pdb.set_trace()
    lit=li[-3:-1]
    print(lit)
    filtered_signal=np.append(filtered_signal,lit)
    print(len(filtered_signal))
    print(len(filtered_x))
    print(len(filtered_y))
    print(len(li))
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




# pt.scatter(time_in_millis,dic['captured_data']['hr']['HR in BPM'],color = 'red')
#print(len(time_in_millis),len(dic['captured_data']['act']['step count']))
#print(len(time_in_millis),len(dic['captured_data']['act']['step count'][:len(time_in_millis)-1]))
#print(len(time_in_millis),len(dic['captured_data']['hr']['HR in BPM']))
#print(len(time_in_millis[:len(dic['captured_data']['act']['step count'])-1]))
#print(dic['captured_data']['act']['step count'])
#print(dic['captured_data']['hr']['HR in BPM'])
#print(dic['captured_data']['act']['step count'])
