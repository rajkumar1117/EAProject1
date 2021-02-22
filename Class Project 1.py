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

# Open Dataset & Convert Object to Datetime (fix this perhaps split up date and time)
raw0 = pd.read_csv('fhvhv_tripdata_2019.csv')
raw0['pickup_datetime'] = pd.to_datetime(raw0['pickup_datetime']).dt.time
raw0['dropoff_datetime'] = pd.to_datetime(raw0['dropoff_datetime']).dt.time
"""
print(raw0.dtypes)
print(raw0['pickup_datetime'].head())
"""

# Create New Column Time of Day (the condition does not work)
raw0['Time_of_Day'] = np.where(dt.datetime.strptime('00:00:00', '%H:%M:%S').time() <= raw0.iloc[0]['pickup_datetime'] <= dt.datetime.strptime('05:59:59', '%H:%M:%S').time(), 'late night',
                               np.where(dt.datetime.strptime('06:00:00', '%H:%M:%S').time() <= raw0.iloc[0]['pickup_datetime'] <= dt.datetime.strptime('11:59:59', '%H:%M:%S').time(), 'morning',
                                        np.where(dt.datetime.strptime('12:00:00', '%H:%M:%S').time() <= raw0.iloc[0]['pickup_datetime'] <= dt.datetime.strptime('17:59:59', '%H:%M:%S').time(), 'afternoon',
                                                 'evening')))
"""
raw0['Time_of_Day'] = np.where(dt.datetime.strptime('06:00:00', '%H:%M:%S').time() <= raw0.iloc[0]['pickup_datetime']
                               <= dt.datetime.strptime('11:59:59', '%H:%M:%S').time(),
                               'morning', 'NaN')
raw0['Time_of_Day'] = np.where(dt.datetime.strptime('12:00:00', '%H:%M:%S').time() <= raw0.iloc[0]['pickup_datetime']
                               <= dt.datetime.strptime('17:59:59', '%H:%M:%S').time(),
                               'afternoon', 'NaN')
raw0['Time_of_Day'] = np.where(dt.datetime.strptime('18:00:00', '%H:%M:%S').time() <= raw0.iloc[0]['pickup_datetime']
                               <= dt.datetime.strptime('23:59:59', '%H:%M:%S').time(),
                               'evening', 'NaN')
"""

# Split Data by Company
uber = raw0[raw0['hvfhs_license_num'] == 'HV0003']
lyft = raw0[raw0['hvfhs_license_num'] == 'HV0005']
via = raw0[raw0['hvfhs_license_num'] == 'HV0004']
juno = raw0[raw0['hvfhs_license_num'] == 'HV0002']
print(uber.head())
# Frequency Table for All by Time of Day (2019)
"""
all_freq = pd.crosstab(index=raw0['hvfhs_license_num'],
                        columns=raw0['Time_of_Day'],
                        margins=True)
all_freq
"""
"""
# Frequency Table for Uber by Time of Day (2019)
uber_freq = pd.crosstab(index=uber['hvfhs_license_num'], columns=uber['Time_of_Day'])
print(uber_freq)

# Frequency Table for Lyft by Time of Day (2019)
lyft_freq = pd.crosstab(index=lyft['hvfhs_license_num'], columns=uber['Time_of_Day'])
print(lyft_freq)

# Frequency Table for Via by Time of Day (2019)
via_freq = pd.crosstab(index=via['hvfhs_license_num'], columns=uber['Time_of_Day'])
print(via_freq)

# Frequency Table for Juno by Time of Day (2019)
juno_freq = pd.crosstab(index=juno['hvfhs_license_num'], columns=uber['Time_of_Day'])
print(juno_freq)
"""