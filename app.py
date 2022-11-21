#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask


# In[2]:


import joblib


# In[3]:


app = Flask(__name__)


# In[ ]:


from flask import request,render_template

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        area = float(request.form.get("area"))
        print(area)
        year =float(request.form.get("year"))
        print(year)

        model = joblib.load("randomforest.joblib")
        r1 = model.predict([[price]])
       
        return(render_template("index.html",result=r1))
    else:
        return(render_template("index.html",result ="waiting"))

