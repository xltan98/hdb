#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask


# In[2]:


import joblib


# In[3]:


app = Flask(__name__)


# In[4]:


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
            Floor Area: {floor_area_sqm}
            Lease Commense Date: {lease_commence_date} 
            Remaining Lease: {Remaining_lease_updated}
            The property is valued at {str(pred[0])} """
        
        return(render_template("index.html",results="s"))
    else:
        return(render_template("index.html",results="Loading..."))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




