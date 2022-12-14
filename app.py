#!/usr/bin/env python
# coding: utf-8

# In[11]:


from flask import Flask


# In[12]:


import joblib


# In[13]:


app = Flask(__name__)


# In[14]:


from flask import request, render_template

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        Year = request.form.get("Year")
        floor_area_sqm = request.form.get("floor_area_sqm")
        lease_commence_date = request.form.get("lease_commence_date")
        Remaining_lease_updated = request.form.get("Remaining_lease_updated")
        
        model1 = joblib.load("randomforest.joblib")
        pred = model1.predict([[Year,floor_area_sqm,lease_commence_date,Remaining_lease_updated]])
        s = f""" Your requested property is: 
            Year: {Year}
            floor_area_sqm: {floor_area_sqm}
            Floor Area (sqm): {floor_area}
            lease_commence_date: {lease_commence_date} 
            The property is valued at {str(pred[0])} """
        
        return(render_template("index.html",results="s"))
    else:
        return(render_template("index.html",results="Loading..."))


# In[15]:


if __name__ == "__main__":
    app.run()


# In[ ]:




