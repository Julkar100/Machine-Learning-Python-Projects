
# coding: utf-8

# In[ ]:


"""
hello this is the code for battery charging and discharging

"""


# In[10]:


battery=10
tocharge=100-battery

time=5 #in hours to charge the whole battery from 0 to 100
"""
time increases by some factor so that in the end the time increases as the charge 
reaches to complete

just taking as sample 
we have to take the ratio and multiply it with the average time taken
"""


# In[13]:


ttocharge=(time/100)*tocharge
print(ttocharge)


# In[55]:


def chargingTime(battery):
    tocharge=100-battery
    ttocharge=(time/100)*tocharge
    hour=int(ttocharge)
    minutes=int(ttocharge%1*60)
    print(str(hour)+"hour and "+str(minutes)+" minutes")


# In[35]:


time=3


# In[64]:


chargingTime(battery=90)

