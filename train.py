#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split  #to split dataset into training and testing data
from sklearn import metrics
import pickle

import pandas as pd


# In[2]:


data=pd.read_csv('covid.csv')


# In[3]:


data.dtypes


# In[4]:


x=data[['fever','cough','fatigue','loss_smell_taste','nasal_congestion','red_eyes','sore_throat','headache','muscle_pain','skin_rash','vomiting','diarrhea','breathing_issue','loss_apetite','chest_pain','age']]
y=data['covid_level']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)


# In[5]:


rf = RandomForestClassifier(n_estimators=40)
rf.fit(x_train, y_train)
print(rf.score(x_test, y_test))


# In[6]:


z=rf.predict(x_test)
z


# In[ ]:
pickle.dump(rf, open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))



