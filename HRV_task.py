import json;
import nolds
from numpy import extract
import numpy as np
import matplotlib.pyplot as plt
# from hrv_analysis_mod.extract_features import _get_freq_psd_from_nn_intervals
# from hrv_analysis_mod.extract_features import get_poincare_plot_features
from preprocessing import remove_outliers,remove_ectopic_beats,is_outlier,_remove_outlier_karlsson,_remove_outlier_acar,interpolate_nan_values,get_nn_intervals,is_valid_sample
from extract_features import get_time_domain_features, get_geometrical_features, get_frequency_domain_features, _get_freq_psd_from_nn_intervals, _create_time_info, _create_interpolation_time, _get_features_from_psd, get_csi_cvi_features, get_poincare_plot_features, DFA, get_sampen
from plot import plot_timeseries, plot_distrib, plot_psd, plot_poincare
#to open the json file
f = open('Elga.json')
# returns JSON object as 
# a dictionary
dic = json.load(f)
next_rr_interval=rr_intervals=dic['captured_data']['hr']['RR in ms']
bpm=dic['captured_data']['hr']['HR in BPM']

rem_outliers = remove_outliers(rr_intervals)
print(rem_outliers)

remove_ectopicbeats = remove_ectopic_beats(rr_intervals)
print(remove_ectopicbeats)


for i in range(len(rr_intervals)):
  outliers=is_outlier(i,i)
print(outliers)

karlsson = _remove_outlier_karlsson(rr_intervals)
print(karlsson)
print(type(karlsson))
karlsson_list = list(karlsson)
print(type(karlsson_list))


remove_outlieracar = _remove_outlier_acar(rr_intervals)
print(remove_outlieracar)


interpolatenan_values = interpolate_nan_values(rr_intervals)
print(interpolatenan_values)

nn_intervals = get_nn_intervals(rr_intervals)
print(nn_intervals)


for tup in range(len(karlsson_list)):
  karlsson_tup = is_valid_sample(rr_intervals,tup)
  print(karlsson_tup)
   
time_features = get_time_domain_features(remove_ectopicbeats)
print(time_features)

geo_features = get_geometrical_features(remove_ectopicbeats)
print(geo_features)

freq_features = get_frequency_domain_features(remove_ectopicbeats)
print(freq_features)

freq_psd = _get_freq_psd_from_nn_intervals(remove_ectopicbeats)
print(freq_psd)
print(type(freq_psd))
time_freq_psd_list = list(freq_psd)
print(type(time_freq_psd_list))
print(time_freq_psd_list)


time_info = _create_time_info(remove_ectopicbeats)
print(time_info)

interpolation_time = _create_interpolation_time(remove_ectopicbeats)
print(interpolation_time)

feat = _get_features_from_psd(remove_ectopicbeats,time_freq_psd_list)
print(feat)

csi = get_csi_cvi_features(remove_ectopicbeats)
print(csi)

poincare = get_poincare_plot_features(remove_ectopicbeats)
print(poincare)

dfa = DFA(remove_ectopicbeats)
print(dfa)

sampen = get_sampen(remove_ectopicbeats)
print(sampen)


timeseries = plot_timeseries(remove_ectopicbeats)
plt.show()

distrib = plot_distrib(remove_ectopicbeats)
plt.show()

psd = plot_psd(remove_ectopicbeats)
plt.show()

poincare = plot_poincare(remove_ectopicbeats)
plt.show()

poincare = plot_poincare(remove_ectopicbeats)
plt.show()