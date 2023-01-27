#!/usr/bin/env python
# coding: utf-8

# Python Assignment - Geetha Kaliyappa

# ! pip install psycopg2-binary - Required installing of this Library for connecting with PostgreSQL Server

# In[8]:


import pandas as pd
import numpy as np
import time
get_ipython().run_line_magic('matplotlib', 'inline')

import warnings
warnings.filterwarnings('ignore')


# In[2]:


import psycopg2 as ps
conn = ps.connect(
    host="devtradingsagedb-do-user-12481132-0.b.db.ondigitalocean.com",
    port="25060",
    dbname="defaultdb",
    user="doadmin",
    password="AVNS_AZ-3Q1oUpp9WnsReBBX")


# In[3]:


df = pd.read_sql_query("select * from test_assignment", con=conn)


# In[4]:


df.head(5)


# <u>Step-by-step Algorithm:</u>
# 
# - So, the two dates will be entered by the user
# - We need to see all the strikes for those two dates
# - Then, get PE OI and CE OI for each strike
# - Then, calculate the difference between respective PE OI and CE OI for each strike for that dates
# - Then, convert the output to a DataFrame

# So, on a given day, we have 121 Strikes for each CE and PE. among the Total count of 242 (121 * 2 = 242)
# 
# So for 2 given dates, we will get 121 differences of Open Interest for each CE and PE

# In[20]:


def diff_cal(date1, date2):
    df1 = df[df['date'] == date1]
    df2 = df[df['date'] == date2] 
    
    strike_list1 = list(df1['strike'].unique())
    strike_list2 = list(df2['strike'].unique())
    
    if set(strike_list1) == set(strike_list2):
        print("We have same Strikes for" , date1 , "&" , date2)
        print("\nLoading...")
        CE1=[]
        PE1=[]
        CE2=[]
        PE2=[]
        for i in strike_list1:
            x1=int(df1[(df1['strike'] == i) & (df1['instrument_type'] == "CE")]['oi'])
            CE1.append(x1)
    
            y1=int(df1[(df1['strike'] == i) & (df1['instrument_type'] == "PE")]["oi"])
            PE1.append(y1)
    
            x2=int(df2[(df2['strike'] == i) & (df2['instrument_type'] == "CE")]['oi'])
            CE2.append(x2)
    
            y2=int(df2[(df2['strike'] == i) & (df2['instrument_type'] == "PE")]["oi"])
            PE2.append(y2)
            
        CE_Diff=[]                 #Calculating CE OI Difference and appending to the empty list CE_Diff
        for i,j in zip(CE1,CE2):
            CE_Diff.append(i-j)
        
        PE_Diff=[]                 #Calculating PE OI Difference and appending to the empty list PE_Diff
        for i,j in zip(PE1,PE2):
            PE_Diff.append(i-j)
        
        time.sleep(3)
            
        print("\nCE & PE OI Difference have been Obtained Successfully..!!! ")
        
        output=pd.DataFrame(strike_list1, columns = ['Strike']) #Creating a Dataframe with one columns
        output['CE OI Difference'] = CE_Diff                    #Adding another column to the above dataframe
        output['PE OI Difference'] = PE_Diff                    #Adding another column to the above dataframe
        pd.set_option('display.max_rows', None)                 #Displaying all rows in the dataframe
        return output                                           #returning the output dataframe to the user
    else:
        print("We don't have equal Strikes for date1 & date2") 
        print("Aborting Operation")


# In[21]:


#Invoking the above created function

#User should enter Old Date followed by New Date in YYYY-MM-DD format.

#Example: diff_cal("YYYY-MM-DD", "YYYY-MM-DD")


Latest_Date="2023-01-02"
Prior_Date="2023-01-03"

diff_cal(Latest_Date,Prior_Date)


# # The End
