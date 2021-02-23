import numpy as np
import pandas as pd
import os
import glob
import datetime as dt

# Set Working Directory
os.chdir('/Users/Rickrockdaboss/Documents/ECON 5763 Economic Analytics/Project 1 Data')

# Combine CSV Files
"""
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
"""

# Export to New CSV
"""combined_csv.to_csv('fhvhv_tripdata_2020.csv', index=False, encoding='utf-8-sig')"""
"""
# Open Datasets & Convert Objects to Datetime
raw0 = pd.read_csv('fhvhv_tripdata_2019.csv')
raw0['pickup_datetime'] = pd.to_datetime(raw0['pickup_datetime']).dt.time
raw0['dropoff_datetime'] = pd.to_datetime(raw0['dropoff_datetime']).dt.time
raw1 = pd.read_csv('fhvhv_tripdata_2020.csv')
raw1['pickup_datetime'] = pd.to_datetime(raw1['pickup_datetime']).dt.time
raw1['dropoff_datetime'] = pd.to_datetime(raw1['dropoff_datetime']).dt.time

# Create New Column Time of Day (the condition does not work)
time_of_day0 = []

for time in raw0['pickup_datetime']:
    if dt.datetime.strptime('00:00:00', '%H:%M:%S').time() <= time <= dt.datetime.strptime('05:59:59', '%H:%M:%S').time():
        time_of_day0.append('late night')
    elif dt.datetime.strptime('06:00:00', '%H:%M:%S').time() <= time <= dt.datetime.strptime('11:59:59', '%H:%M:%S').time():
        time_of_day0.append('morning')
    elif dt.datetime.strptime('12:00:00', '%H:%M:%S').time() <= time <= dt.datetime.strptime('17:59:59', '%H:%M:%S').time():
        time_of_day0.append('afternoon')
    elif dt.datetime.strptime('18:00:00', '%H:%M:%S').time() <= time <= dt.datetime.strptime('23:59:59', '%H:%M:%S').time():
        time_of_day0.append('evening')
    else:
        time_of_day0.append('N/A')

raw0['time_of_day'] = time_of_day0

time_of_day1 = []

for time in raw1['pickup_datetime']:
    if dt.datetime.strptime('00:00:00', '%H:%M:%S').time() <= time <= dt.datetime.strptime('05:59:59', '%H:%M:%S').time():
        time_of_day1.append('late night')
    elif dt.datetime.strptime('06:00:00', '%H:%M:%S').time() <= time <= dt.datetime.strptime('11:59:59', '%H:%M:%S').time():
        time_of_day1.append('morning')
    elif dt.datetime.strptime('12:00:00', '%H:%M:%S').time() <= time <= dt.datetime.strptime('17:59:59', '%H:%M:%S').time():
        time_of_day1.append('afternoon')
    elif dt.datetime.strptime('18:00:00', '%H:%M:%S').time() <= time <= dt.datetime.strptime('23:59:59', '%H:%M:%S').time():
        time_of_day1.append('evening')
    else:
        time_of_day1.append('N/A')

raw1['time_of_day'] = time_of_day1

# Save as New CSV Files (Done for Faster Results)
raw0.to_csv('2019_clean.csv', index=False, encoding='utf-8-sig')
raw1.to_csv('2020_clean.csv', index=False, encoding='utf-8-sig')
"""
# Use New Datasets (comment out previous code)
raw0 = pd.read_csv('2019_clean.csv')
raw1 = pd.read_csv('2020_clean.csv')

# Split Data by Company
uber0 = raw0[raw0['hvfhs_license_num'] == 'HV0003']
lyft0 = raw0[raw0['hvfhs_license_num'] == 'HV0005']
via0 = raw0[raw0['hvfhs_license_num'] == 'HV0004']
juno0 = raw0[raw0['hvfhs_license_num'] == 'HV0002']

uber1 = raw1[raw1['hvfhs_license_num'] == 'HV0003']
lyft1 = raw1[raw1['hvfhs_license_num'] == 'HV0005']
via1 = raw1[raw1['hvfhs_license_num'] == 'HV0004']
juno1 = raw1[raw1['hvfhs_license_num'] == 'HV0002']

# Frequency Table for All by Time of Day (2019)
all_freq0 = pd.crosstab(index=raw0['hvfhs_license_num'], columns=raw0['time_of_day'], margins=True)
print(all_freq0)

# Frequency Table for All by Time of Day (2020)
all_freq1 = pd.crosstab(index=raw1['hvfhs_license_num'], columns=raw1['time_of_day'], margins=True)
print(all_freq1)

# Frequency Table for Uber by Time of Day (2019)
uber_freq0 = pd.crosstab(index=uber0['hvfhs_license_num'], columns=uber0['time_of_day'])
print(uber_freq0)

# Frequency Table for Uber by Time of Day (2020)
uber_freq1 = pd.crosstab(index=uber1['hvfhs_license_num'], columns=uber1['time_of_day'])
print(uber_freq1)

# Frequency Table for Lyft by Time of Day (2019)
lyft_freq0 = pd.crosstab(index=lyft0['hvfhs_license_num'], columns=lyft0['time_of_day'])
print(lyft_freq0)

# Frequency Table for Lyft by Time of Day (2020)
lyft_freq1 = pd.crosstab(index=lyft1['hvfhs_license_num'], columns=lyft1['time_of_day'])
print(lyft_freq1)

# Frequency Table for Via by Time of Day (2019)
via_freq0 = pd.crosstab(index=via0['hvfhs_license_num'], columns=via0['time_of_day'])
print(via_freq0)

# Frequency Table for Via by Time of Day (2020)
via_freq1 = pd.crosstab(index=via1['hvfhs_license_num'], columns=via1['time_of_day'])
print(via_freq1)

# Frequency Table for Juno by Time of Day (2019)
juno_freq0 = pd.crosstab(index=juno0['hvfhs_license_num'], columns=juno0['time_of_day'])
print(juno_freq0)

# Frequency Table for Juno by Time of Day (2020)
juno_freq1 = pd.crosstab(index=juno1['hvfhs_license_num'], columns=juno1['time_of_day'])
print(juno_freq1)

