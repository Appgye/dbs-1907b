#!/usr/bin/env python
# coding: utf-8

# In[21]:


from flask import Flask, request, render_template


# In[22]:


import joblib


# In[23]:


app = Flask(__name__)


# In[24]:


__name__


# In[25]:


@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        rates = float(request.form.get("rates"))
        model1 = joblib.load("regression")
        r1 = model1.predict([[rates]])
        model2 = joblib.load("regression")
        r2 = model2.predict([[rates]])
        return(render_template("index.html", result1 = r1, result2 = r1))
    else:
        return(render_template("index.html", result1 = "WAITING", result2 = "WAITING"))


# In[ ]:


if __name__ == "__main__":
    app.run()

