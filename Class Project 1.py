import numpy as np
import pandas as pd
import os
import glob
import datetime as dt
import folium
from folium import plugins
import rasterio as rio
from rasterio.warp import calculate_default_transform, reproject, Resampling
import earthpy as et

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

# Create Newer Dataset (borough)
borough = []
for i in raw0['PULocationID']:
    if raw0.loc[0]['PULocationID'] == "200" or "240" or "220" or "241" or "136" or "235" or "119" or "247" or "168" or "174" or "18" or "94" or "169" or "69" or "159" or "167" or "47" or "20" or "59" or "78" or "147" or "126" or "60" or "31" or "254" or "259" or "81" or "3" or "32" or "185" or "242" or "248" or "212" or "213" or "250" or "182" or "51" or "184" or "183" or "199" or "208" or "58" or "46":
        borough.append('Bronx')
    elif raw0.loc[0]['PULocationID'] == "195" or "54" or "52" or "33" or "40" or "25" or "65" or "66" or "34" or "97" or "106" or "228" or "14" or "67" or "227" or "111" or "181" or "189" or "49" or "217" or "265" or "255" or "112" or "80" or "17" or "61" or "62" or "190" or "257" or "26" or "22" or "11" or "21" or "178" or "89" or "133" or "89" or "188" or "85" or "225" or "37" or "36" or "177" or "63" or "77" or "35" or "72" or "71" or "91" or "165" or "123" or "108" or "85" or "29" or "150" or "210" or "149" or "155" or "154" or "39" or "222" or "76":
        borough.append('Brooklyn')
    elif raw0.loc[0]['PULocationID'] == "153" or "128" or "127" or "243" or "120" or "244" or "116" or "42" or "152" or "166" or "41" or "74" or "194" or "24" or "151" or "238" or "43" or "75" or "236" or "263" or "262" or "237" or "141" or "140" or "143" or "142" or "50" or "48" or "163" or "230" or "161" or "162" or "229" or "202" or "246" or "68" or "100" or "186" or "90" or "164" or "234" or "170" or "107" or "137" or "224" or "158" or "249" or "113" or "114" or "79" or "4" or "125" or "211" or "144" or "148" or "232" or "231" or "45" or "13" or "261" or "12" or "88" or "87" or "209" or "45" or "104" or "105" or "103":
        borough.append('Manhattan')
    elif raw0.loc[0]['PULocationID'] == "27" or "2" or "201" or "117" or "86" or "132" or "124" or "180" or "216" or "10" or "218" or "219" or "203" or "139" or "205" or "215" or "197" or "258" or "96" or "134" or "130" or "215" or "205" or "38" or "191" or "122" or "28" or "102" or "198" or "134" or "19" or "101" or "64" or "175" or "89" or "121" or "135" or "192" or "9" or "16" or "73" or "171" or "15" or "252" or "53" or "92" or "253" or "93" or "95" or "196" or "160" or "157" or "226" or "145" or "146" or "193" or "179" or "8" or "7" or "223" or "207" or "260" or "83" or "82" or "138" or "70" or "173" or "56" or "57":
        borough.append('Queens')
    elif raw0.loc[0]['PULocationID'] == "44" or "204" or "84" or "5" or "99" or "109" or "110" or "176" or "172" or "214" or "118" or "23" or "156" or "187" or "251" or "245" or "206" or "115" or "221" or "6" or "214" or "172" or "276":
        borough.append('Staten')
    else:
        borough.append('N/A')
raw0['Borough'] = borough

borough1 = []
for i in raw1['PULocationID']:
    if raw1.loc[0]['PULocationID'] == "200" or "240" or "220" or "241" or "136" or "235" or "119" or "247" or "168" or "174" or "18" or "94" or "169" or "69" or "159" or "167" or "47" or "20" or "59" or "78" or "147" or "126" or "60" or "31" or "254" or "259" or "81" or "3" or "32" or "185" or "242" or "248" or "212" or "213" or "250" or "182" or "51" or "184" or "183" or "199" or "208" or "58" or "46":
        borough1.append('Bronx')
    elif raw1.loc[0]['PULocationID'] == "195" or "54" or "52" or "33" or "40" or "25" or "65" or "66" or "34" or "97" or "106" or "228" or "14" or "67" or "227" or "111" or "181" or "189" or "49" or "217" or "265" or "255" or "112" or "80" or "17" or "61" or "62" or "190" or "257" or "26" or "22" or "11" or "21" or "178" or "89" or "133" or "89" or "188" or "85" or "225" or "37" or "36" or "177" or "63" or "77" or "35" or "72" or "71" or "91" or "165" or "123" or "108" or "85" or "29" or "150" or "210" or "149" or "155" or "154" or "39" or "222" or "76":
        borough1.append('Brooklyn')
    elif raw1.loc[0]['PULocationID'] == "153" or "128" or "127" or "243" or "120" or "244" or "116" or "42" or "152" or "166" or "41" or "74" or "194" or "24" or "151" or "238" or "43" or "75" or "236" or "263" or "262" or "237" or "141" or "140" or "143" or "142" or "50" or "48" or "163" or "230" or "161" or "162" or "229" or "202" or "246" or "68" or "100" or "186" or "90" or "164" or "234" or "170" or "107" or "137" or "224" or "158" or "249" or "113" or "114" or "79" or "4" or "125" or "211" or "144" or "148" or "232" or "231" or "45" or "13" or "261" or "12" or "88" or "87" or "209" or "45" or "104" or "105" or "103":
        borough1.append('Manhattan')
    elif raw1.loc[0]['PULocationID'] == "27" or "2" or "201" or "117" or "86" or "132" or "124" or "180" or "216" or "10" or "218" or "219" or "203" or "139" or "205" or "215" or "197" or "258" or "96" or "134" or "130" or "215" or "205" or "38" or "191" or "122" or "28" or "102" or "198" or "134" or "19" or "101" or "64" or "175" or "89" or "121" or "135" or "192" or "9" or "16" or "73" or "171" or "15" or "252" or "53" or "92" or "253" or "93" or "95" or "196" or "160" or "157" or "226" or "145" or "146" or "193" or "179" or "8" or "7" or "223" or "207" or "260" or "83" or "82" or "138" or "70" or "173" or "56" or "57":
        borough1.append('Queens')
    elif raw1.loc[0]['PULocationID'] == "44" or "204" or "84" or "5" or "99" or "109" or "110" or "176" or "172" or "214" or "118" or "23" or "156" or "187" or "251" or "245" or "206" or "115" or "221" or "6" or "214" or "172" or "276":
        borough1.append('Staten')
    else:
        borough1.append('N/A')
raw1['Borough'] = borough1

# Save as Newer CSV Files (Done for Faster Results)
raw0.to_csv('2019_clean_new.csv', index=False, encoding='utf-8-sig')
raw1.to_csv('2020_clean_new.csv', index=False, encoding='utf-8-sig')


# Use Newer Datasets (comment out previous code)
raw0 = pd.read_csv('2019_clean_new.csv')
raw1 = pd.read_csv('2020_clean_new.csv')

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
all_freq0 = pd.crosstab(index=raw0['time_of_day'], columns=raw0['borough'], margins=True)
print(all_freq0)

# Frequency Table for All by Time of Day (2020)
all_freq1 = pd.crosstab(index=raw1['time_of_day'], columns=raw1['borough'], margins=True)
print(all_freq1)

# Frequency Table for Uber by Time of Day (2019)
uber_freq0 = pd.crosstab(index=uber0['time_of_day'], columns=uber0['borough'])
print(uber_freq0)

# Frequency Table for Uber by Time of Day (2020)
uber_freq1 = pd.crosstab(index=uber1['time_of_day'], columns=uber1['borough'])
print(uber_freq1)

# Frequency Table for Lyft by Time of Day (2019)
lyft_freq0 = pd.crosstab(index=lyft0['time_of_day'], columns=lyft0['borough'])
print(lyft_freq0)

# Frequency Table for Lyft by Time of Day (2020)
lyft_freq1 = pd.crosstab(index=lyft1['time_of_day'], columns=lyft1['borough'])
print(lyft_freq1)

# Frequency Table for Via by Time of Day (2019)
via_freq0 = pd.crosstab(index=via0['time_of_day'], columns=via0['borough'])
print(via_freq0)

# Frequency Table for Via by Time of Day (2020)
via_freq1 = pd.crosstab(index=via1['time_of_day'], columns=via1['borough'])
print(via_freq1)

# Frequency Table for Juno by Time of Day (2019)
juno_freq0 = pd.crosstab(index=juno0['time_of_day'], columns=juno0['borough'])
print(juno_freq0)

# Frequency Table for Juno by Time of Day (2020)
juno_freq1 = pd.crosstab(index=juno1['time_of_day'], columns=juno1['borough'])
print(juno_freq1)

# Map
staten = folium.Map(location=[40.5795, -74.1502], tiles = 'Stamen Terrain')

# Staten Marker
folium.Marker(
    location=[40.5795, -74.1502],
    popup='Frequency Number ',
    icon=folium.Icon()
).add_to(staten)

# Bronx Marker
folium.Marker(
    location=[40.8448, -73.8648],
    popup='Frequency Number ',
    icon=folium.Icon()
).add_to(staten)

# Manhattan Marker
folium.Marker(
    location=[40.7831, -73.9712],
    popup='Frequency Number ',
    icon=folium.Icon()
).add_to(staten)

# Queens Marker
folium.Marker(
    location=[40.7282, -73.7949],
    popup='Frequency Number ',
    icon=folium.Icon()
).add_to(staten)

# Brooklyn Marker
folium.Marker(
    location=[40.6782, -73.9442],
    popup='Frequency Number ',
    icon=folium.Icon()
).add_to(staten)