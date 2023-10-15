#!/usr/bin/env python
# coding: utf-8

# **Question 1: Use ffinance to Extract Stock Data**

# In[ ]:


get_ipython().system('pip install yfinance==0.1.67')
get_ipython().system('mamba install bs4==4.10.0 -y')
get_ipython().system('pip install nbformat==4.2.0')


# In[7]:


import yfinance as yf
import pandas as pd


# In[8]:


import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# In[16]:


tesla= yf.Ticker("TSLA")


# In[15]:


tesla_data = tesla.history(period="max")


# In[ ]:





# In[17]:


tesla_data.reset_index(inplace=True)
tesla_data.head(5)


# **Question 2: Use Webscrapping to Extract Tesla Revenue Data**

# In[18]:


url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
html_data = requests.get(url).text


# In[19]:


soup = BeautifulSoup(html_data, "html5lib")
print(soup.prettify())


# In[20]:


tesla_revenue = pd.DataFrame(columns = ["Date","Revenue"])

for table in soup.find_all('table'):
    if table.find('th').getText().startswith("Tesla Quarterly Revenue"):
        for row in table.find("tbody").find_all("tr"):
            col = row.find_all("td")
            if len(col) != 2: continue
            Date = col[0].text
            Revenue = col[1].text.replace("$","").replace(",","")
               
            tesla_revenue = tesla_revenue.append({"Date":Date, "Revenue":Revenue}, ignore_index=True)


# In[22]:


tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(',|\$',"")


# In[23]:


#remove NaN values
tesla_revenue.dropna(axis=0, how='all', subset=['Revenue']) 
#remove empty string values
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""] 


# In[24]:


tesla_revenue.tail(5)


# **Question 3: Use fyfinance to Extract Stock Data**

# In[ ]:


get_ipython().system('pip install yfinance==0.1.67')
get_ipython().system('mamba install bs4==4.10.0 -y')
get_ipython().system('pip install nbformat==4.2.0')


# In[38]:


import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# In[42]:


GameStop=yf.Ticker("GME")


# In[43]:


gme_data = GameStop.history(period="max")


# In[44]:


gme_data.reset_index(inplace=True)
gme_data.head(5)


# **Question4: Use Webscrapping to Extract GME Revenue Data**

# In[53]:


url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
html_data = requests.get(url).text


# In[ ]:


soup=BeautifulSoup(html_data, "html5lib")
print(soup.prettify())


# In[55]:


gme_revenue=pd.DataFrame(columns = ["Date","Revenue"])

for table in soup.find_all('table'):
    if table.find('th').getText().startswith("GameStop Quarterly Revenue"):
        for row in table.find("tbody").find_all("tr"):
            col=row.find_all("td")
            if len(col) != 2: continue
            Date=col[0].text
            Revenue=col[1].text.replace("$","").replace(",","")
               
            gme_revenue = gme_revenue.append({"Date":Date, "Revenue":Revenue}, ignore_index=True)


# In[56]:


gme_revenue.tail(5)


# **Question 5: Plot Tela Stock Graph**

# In[74]:


tesla= yf.Ticker("TSLA")
tesla_data = tesla.history(period="max")


# In[73]:


import plotly.graph_objects as go
from plotly.subplots import make_subplots
import yfinance as yf
import pandas as pd

tesla_data = yf.download("TSLA", start="2020-01-01", end="2021-09-30", progress=False)
tesla_revenue = yf.download("TSLA", start="2020-01-01", end="2021-09-30", progress=False)
tesla_data.reset_index(inplace=True)
tesla_revenue.reset_index(inplace=True)

def make_graph(tesla_data, tesla_revenue, stock):
    fig = make_subplots(rows=2, cols=1, 
                        shared_xaxes=True, 
                        subplot_titles=("Historical Share Price", "Historical Revenue"), 
                        vertical_spacing=.3)
    
    stock_data_specific = tesla_data[tesla_data.Date <= '2021-06-14']
    revenue_data_specific = tesla_revenue[tesla_revenue.Date <= '2021-04-30']
    
    fig.add_trace(go.Scatter(
        x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True),
        y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), 
                             y=revenue_data_specific.Volume.astype("float"),
                             name="Volume"), row=2, col=1)
    
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    
    fig.update_layout(showlegend=False,
                      height=900,
                      title=stock,
                      xaxis_rangeslider_visible=True)
    
    fig.show()
    
make_graph(tesla_data, tesla_revenue, 'Tesla stock Data')


# In[ ]:





# **Question 6: Plot Gamestock Graph**

# In[71]:


make_graph(gme_data, gme_revenue, 'GameStop')


# In[77]:


import plotly.graph_objects as go
from plotly.subplots import make_subplots
import yfinance as yf
import pandas as pd

gme_data = yf.download("TSLA", start="2020-01-01", end="2021-09-30", progress=False)
gme_revenue = yf.download("TSLA", start="2020-01-01", end="2021-09-30", progress=False)
gme_data.reset_index(inplace=True)
gme_revenue.reset_index(inplace=True)

def make_graph(gme_data, gme_revenue, stock):
    fig = make_subplots(rows=2, cols=1, 
                        shared_xaxes=True, 
                        subplot_titles=("Historical Share Price", "Historical Revenue"), 
                        vertical_spacing=.3)
    
    stock_data_specific = gme_data[gme_data.Date <= '2021-06-14']
    revenue_data_specific = gme_revenue[gme_revenue.Date <= '2021-04-30']
    
    fig.add_trace(go.Scatter(
        x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True),
        y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), 
                             y=revenue_data_specific.Volume.astype("float"),
                             name="Volume"), row=2, col=1)
    
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    
    fig.update_layout(showlegend=False,
                      height=900,
                      title=stock,
                      xaxis_rangeslider_visible=True)
    
    fig.show()
    
make_graph(gme_data, gme_revenue, 'GameStop stock Data')


# In[ ]:




