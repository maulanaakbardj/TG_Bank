#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pyTigerGraph as tg 
from datetime import datetime
import pytz
conn = tg.TigerGraphConnection(host="http://172.16.11.223")
conn.graphname = "Team_Grafana"

runquery1 = conn.runInstalledQuery("UC6_QRY01_TransactionsMoreThan100Million")
current_dateTime1 = datetime.now(pytz.timezone('Asia/Jakarta'))
print("Running Query (Datetime) : " + str(current_dateTime1))

runquery2 = conn.runInstalledQuery("UC6_QRY02_TransactionsOutsideOperationalHours")
current_dateTime2 = datetime.now(pytz.timezone('Asia/Jakarta'))
print("Running Query (Datetime) : " + str(current_dateTime2))

