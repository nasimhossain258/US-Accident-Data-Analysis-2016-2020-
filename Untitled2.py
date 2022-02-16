#!/usr/bin/env python
# coding: utf-8

# # US Accident Data Analysis

# # # Data Downloading

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


df=pd.read_csv('US_Accidents_Dec20_updated.csv')
df


# In[4]:


df.info()

ask question and answer
1.are there more accident in warmer or colder areas?
2.which states has the number of accidents? -----
# In[5]:


df.describe()


# In[6]:


Missing_percentage=df.isna().sum().sort_values(ascending=False)/len(df)
Missing_percentage


# In[7]:


Missing_percentage[Missing_percentage !=0.].plot(kind='barh')


# the columns we do  not need

# In[8]:


df_delete = df.drop(['Number'], axis=1)


# In[9]:


Cities_by_accident = df.City.value_counts().sort_values(ascending=False)
Cities_by_accident


# In[10]:


Cities_by_accident[:25].plot(kind='barh',figsize=(20,10))


# In[11]:


cities =df.City.unique()
len(cities)


# In[12]:


sns.set_style("darkgrid")
sns.distplot(Cities_by_accident)


# In[13]:


high_accident_cities = Cities_by_accident[Cities_by_accident >= 1000]
low_accident_cities = Cities_by_accident[Cities_by_accident < 1000]


# In[14]:


len(high_accident_cities)/len(cities)


# In[15]:


sns.distplot(high_accident_cities,)


# In[16]:


sns.histplot(low_accident_cities, log_scale=True)


# # # Start Time

# In[17]:


df.Start_Time


# In[18]:


df.Start_Time = pd.to_datetime(df.Start_Time)
df.Start_Time


# ### Hour basis accidents

# In[19]:


sns.distplot(df.Start_Time.dt.hour, bins=24, kde=False, norm_hist=True)


# - High percentage of accidents occur 1PM to 6PM.
# - Probably people are in hurry or due to traffic
# - Next highest percentage is 6AM to 9AM

# ### Day basis Accidents

# In[20]:


sns.distplot(df.Start_Time.dt.dayofweek, bins=7, kde=False, norm_hist=True)


#  - Is the distrobution of accidents by hour the same on weekends as on weekdays

# In[21]:


sunday_start_time = df.Start_Time[df.Start_Time.dt.dayofweek==6 ]
sns.distplot(sunday_start_time.dt.hour, bins=24, kde=False, norm_hist=True)


# In[22]:


Monday_start_time = df.Start_Time[df.Start_Time.dt.dayofweek==0 ]
sns.distplot(Monday_start_time.dt.hour, bins=24, kde=False, norm_hist=True)


#  - On sundays the peak of accidents occur between 10AM to 11PM, unlike Weekdays

# ### Monthly basis Accidents 

# In[23]:


sns.distplot(df.Start_Time.dt.month, bins=12, kde=False, norm_hist=True)


#  - In general, most traffic fatalities occur in the summer and fall and that is the reason the vehicles goes slow. but in winter and in holidays the traffic is less than usual. And people drives faster and weekdays. That is the reason the most of the accidents occur between OCT to NOV but the in DEC it is the heighest  
# 

# ## Start Latitude and Longitude

# In[24]:


df.Start_Lat


# In[25]:


df.Start_Lng


# In[26]:


sample_df = df.sample(int(0.1 * len(df)))
sample_df 


# In[27]:


sns.scatterplot(x=sample_df.Start_Lng, y= sample_df.Start_Lat, size = 0.001)


# In[28]:


get_ipython().system('pip install folium')
import folium


# In[29]:


from folium import plugins
from folium.plugins import HeatMap


# In[30]:


sample_df = df.sample(int(0.001 * len(df))) 
lat_lon_pairs = list(zip(list(df.Start_Lat), list(df.Start_Lng)))


# ## sample dataset

# In[31]:


map1= folium.Map()
HeatMap(lat_lon_pairs[:100]).add_to(map1)
map1


# In[34]:


sample_df1 = df.sample(int(0.001 * len(df))) 
lat_lon_pairs1 = list(zip(list(sample_df1.Start_Lat), list(sample_df1.Start_Lng)))


# In[35]:


map2= folium.Map()
HeatMap(lat_lon_pairs1).add_to(map2)
map2


# In[32]:


zip(list(df.Start_Lat), list(df.Start_Lng))


# In[33]:


map= folium.Map()
HeatMap(zip(list(df.Start_Lat), list(df.Start_Lng))).add_to(map)
map


# In[ ]:





# # Smmary and Conclusion

# Insights:
#  * No Data for New York Althouth It is a big City.
#  * The number of accident per city decreases Exponentially.
#  * less than 3% of have more than 1000 yearly accidents.
#  * Over 1200 cities have reported just 1 accident
