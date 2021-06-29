#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 23:44:16 2021

@author: Richard
"""

import os
import pandas as pd
import math
import csv


# https://data.giss.nasa.gov/cgi-bin/gistemp/stdata_find_v4.cgi?lat=44.2500&lon=-76.5000&ds=14&dt=1
# above link is used for fetching kingston data using NASA data, there are missing and wrong data point
# in each station, I stitched multiple station data to compose the complete data points from 1880 to now
# 


date_range_dict = {}
for i in range(1880,2022):
    for j in range(1,13):
        # print(i,j)
        key = str(i)+'-'+str(j).zfill(2)
        # print(key)
        date_range_dict[key]=''

nasa_path = r'/Users/Richard/Desktop/Queens_MFIT/867/a2/station (1).csv'
nasa_df = pd.read_csv(nasa_path)
drop_list = ['D-J-F',	'M-A-M',	'J-J-A',	'S-O-N',	'metANN']
nasa_df = nasa_df.drop(drop_list,axis = 1)


nasa_df = nasa_df.set_index(['YEAR'])
header_dict = {
    'JAN':'01',
    'FEB':'02',
    'MAR':'03',
    'APR':'04',
    'MAY':'05',
    'JUN':'06',
    'JUL':'07',
    'AUG':'08',
    'SEP':'09',
    'OCT':'10',
    'NOV':'11',
    'DEC':'12'
    }
nasa_df = nasa_df.rename(columns=header_dict)
temp_list = []
for key in header_dict:
    temp_list.append(header_dict[key])

for i,row in nasa_df.iterrows():
    for key in temp_list:
        print(str(i)+'-'+key,row[key])
        temp_key = str(i)+'-'+key
        if row[key]!=999.9:
            date_range_dict[temp_key] = row[key]
            
            
canada_path = r'/Users/Richard/Desktop/Queens_MFIT/867/a2/en_climate_monthly_ON_6104146_1930-1996_P1M.csv'
            
canada_df = pd.read_csv(canada_path)           

remove_col = ["Longitude (x)","Latitude (y)","Station Name","Climate ID","Date/Time","Mean Max Temp (°C)","Mean Max Temp Flag","Mean Min Temp (°C)","Mean Min Temp Flag","Mean Temp Flag","Extr Max Temp (°C)","Extr Max Temp Flag","Extr Min Temp (°C)","Extr Min Temp Flag","Total Rain (mm)","Total Rain Flag","Total Snow (cm)","Total Snow Flag","Total Precip (mm)","Total Precip Flag","Snow Grnd Last Day (cm)","Snow Grnd Last Day Flag","Dir of Max Gust (10's deg)","Dir of Max Gust Flag","Spd of Max Gust (km/h)","Spd of Max Gust Flag"]
            
canada_df = canada_df.drop(remove_col,axis = 1)       
            
for i,row in canada_df.iterrows():
    temp_key = str(int(row['Year'])) + '-' + str(int(row['Month'])).zfill(2)
    print(temp_key)
    print(row["Mean Temp (°C)"])
    if not math.isnan(row["Mean Temp (°C)"]):
        if date_range_dict[temp_key] == '':
            date_range_dict[temp_key] = row["Mean Temp (°C)"]
            
for key in date_range_dict:
    if date_range_dict[key] =='':
        print(key)
            

def process_nasa(file_path,date_range_dict):
    nasa_df = pd.read_csv(file_path)
    drop_list = ['D-J-F',	'M-A-M',	'J-J-A',	'S-O-N',	'metANN']
    nasa_df = nasa_df.drop(drop_list,axis = 1)
    
    
    nasa_df = nasa_df.set_index(['YEAR'])
    header_dict = {
        'JAN':'01',
        'FEB':'02',
        'MAR':'03',
        'APR':'04',
        'MAY':'05',
        'JUN':'06',
        'JUL':'07',
        'AUG':'08',
        'SEP':'09',
        'OCT':'10',
        'NOV':'11',
        'DEC':'12'
        }
    nasa_df = nasa_df.rename(columns=header_dict)
    temp_list = []
    for key in header_dict:
        temp_list.append(header_dict[key])
    
    for i,row in nasa_df.iterrows():
        for key in temp_list:
            # print(str(i)+'-'+key,row[key])
            temp_key = str(i)+'-'+key
            if row[key]!=999.9 and date_range_dict[temp_key]=='':
                date_range_dict[temp_key] = row[key]
    return date_range_dict

nasa_path2 = r'/Users/Richard/Desktop/Queens_MFIT/867/a2/station (2).csv'


date_range_dict_new = process_nasa(nasa_path2,date_range_dict)

for key in date_range_dict_new:
    if date_range_dict_new[key] == '':
        print(key)



nasa_path3 = r'/Users/Richard/Desktop/Queens_MFIT/867/a2/station (3).csv'

date_range_dict_new2 = process_nasa(nasa_path3,date_range_dict_new)

for key in date_range_dict_new2:
    if date_range_dict_new[key] == '':
        print(key)
        
nasa_path4 = r'/Users/Richard/Desktop/Queens_MFIT/867/a2/station (4).csv'   

date_range_dict_new2 = process_nasa(nasa_path4,date_range_dict_new2)

for key in date_range_dict_new2:
    if date_range_dict_new[key] == '':
        print(key)    
        
nasa_path5 = r'/Users/Richard/Desktop/Queens_MFIT/867/a2/station (5).csv'   

date_range_dict_new2 = process_nasa(nasa_path5,date_range_dict_new2)

for key in date_range_dict_new2:
    if date_range_dict_new[key] == '':
        print(key)  
        
        
        
        
nasa_path6 = r'/Users/Richard/Desktop/Queens_MFIT/867/a2/station (6).csv'   

date_range_dict_new2 = process_nasa(nasa_path6,date_range_dict_new2)

for key in date_range_dict_new2:
    if date_range_dict_new[key] == '':
        print(key) 
        
        
nasa_path7 = r'/Users/Richard/Desktop/Queens_MFIT/867/a2/station (7).csv'   

date_range_dict_new2 = process_nasa(nasa_path7,date_range_dict_new2)

for key in date_range_dict_new2:
    if date_range_dict_new[key] == '':
        print(key) 

header = ['year-month','temp']
output = [header]

for key in date_range_dict_new2:
    temp_row = [key,date_range_dict_new2[key]]
    output.append(temp_row)
    
output_file = r'/Users/Richard/Desktop/Queens_MFIT/867/a2/kingston_weather.csv'  
with open(output_file,'w') as csvfile:
    writer = csv.writer(csvfile)
    for row in output:
        writer.writerow(row)
