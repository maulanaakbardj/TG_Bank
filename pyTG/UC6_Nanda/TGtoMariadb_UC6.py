#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pyTigerGraph as tg
import sqlalchemy as db
import pandas as pd
import pymysql
from datetime import datetime
import pytz

conn = tg.TigerGraphConnection(host="http://172.16.11.223")
conn.graphname = "Team_Grafana"

output_uc6a = conn.runInstalledQuery("UC6a_QRY2_GetVertexUC6a")

df_uc6a = pd.json_normalize(output_uc6a[0]['myUC6a'])
df_uc6a = df_uc6a.drop(["v_id","v_type"], axis='columns')

df_uc6a.rename(columns = {'attributes.Credit_Card_Trx_ID':'Credit_Card_Trx_ID',
                     'attributes.Credit_Card_Trx_Code':'Credit_Card_Trx_Code',
                     'attributes.Credit_Card_Trx_Type':'Credit_Card_Trx_Type',
                     'attributes.Credit_Card_Trx_Amount':'Credit_Card_Trx_Amount',
                    'attributes.Amount':'Amount',
                     'attributes.Account_Credit_Card_ID':'Account_Credit_Card_ID',
                     'attributes.Credit_Card_Trx_Datetime':'Credit_Card_Trx_Datetime',
                     'attributes.EDC_Name':'EDC_Name',
                     'attributes.EDC_City':'EDC_City',
                     'attributes.EDC_Address':'EDC_Address',
                     'attributes.User_Name':'User_Name',
                     'attributes.User_Address':'User_Address',
                     'attributes.User_Gender':'User_Gender'
                     'attributes.User_BirthDate':'User_BirthDate',
                     'attributes.User_KTP_ID':'User_KTP_ID'
                    },
                     inplace = True)


df_uc6a = df_uc6a[["Credit_Card_Trx_ID","Credit_Card_Trx_Code","Credit_Card_Trx_Type","Credit_Card_Trx_Amount","Amount",
                   "Account_Credit_Card_ID","Credit_Card_Trx_Datetime",
                   "EDC_Name","EDC_City","EDC_Address",
                   "User_Name","User_Address","User_Gender","User_BirthDate","User_KTP_ID"]]


output_uc6b = conn.runInstalledQuery("UC6b_QRY2_GetVertexUC6b")

df_uc6b = pd.json_normalize(output_uc6b[0]['myUC6b'])
df_uc6b = df_uc6b.drop(["v_id","v_type"], axis='columns')

df_uc6b.rename(columns = {'attributes.Credit_Card_Trx_ID':'Credit_Card_Trx_ID',
                     'attributes.Credit_Card_Trx_Code':'Credit_Card_Trx_Code',
                     'attributes.Credit_Card_Trx_Type':'Credit_Card_Trx_Type',
                     'attributes.Credit_Card_Trx_Amount':'Credit_Card_Trx_Amount',
                     'attributes.Account_Credit_Card_ID':'Account_Credit_Card_ID',
                     'attributes.Credit_Card_Trx_Datetime':'Credit_Card_Trx_Datetime',
                     'attributes.EDC_Name':'EDC_Name',
                     'attributes.EDC_City':'EDC_City',
                     'attributes.EDC_Address':'EDC_Address',
                     'attributes.EDC_Operation_Time_Start':'EDC_Operation_Time_Start',
                     'attributes.EDC_Operation_Time_End':'EDC_Operation_Time_End',                       
                     'attributes.User_Name':'User_Name',
                     'attributes.User_Address':'User_Address',
                     'attributes.User_Gender':'User_Gender'
                     'attributes.User_BirthDate':'User_BirthDate',
                     'attributes.User_KTP_ID':'User_KTP_ID'
                    },
                     inplace = True)

df_uc6b = df_uc6b[["Credit_Card_Trx_ID","Credit_Card_Trx_Code","Credit_Card_Trx_Type","Credit_Card_Trx_Amount",
                   "Account_Credit_Card_ID","Credit_Card_Trx_Datetime",
                   "EDC_Name","EDC_City","EDC_Address","EDC_Operation_Time_Start","EDC_Operation_Time_End",
                   "User_Name","User_Address","User_Gender","User_BirthDate","User_KTP_ID"]]


now1 = datetime.now(pytz.timezone('Asia/Jakarta'))
current_dateTime1 = now1.strftime("%Y-%m-%d %H:%M")
df_uc6a['Anomaly_timestamp'] = current_dateTime1

now2 = datetime.now(pytz.timezone('Asia/Jakarta'))
current_dateTime2 = now2.strftime("%Y-%m-%d %H:%M")
df_uc6b['Anomaly_timestamp'] = current_dateTime2

engine = db.create_engine("mysql+pymysql://root:password@192.168.100.8/Grafana") // masih mariadb local blom mariadb server
df_uc6a.to_sql(name='UC6a', con=engine, if_exists = 'append', index=False) #masukan data
df_uc6b.to_sql(name='UC6b', con=engine, if_exists = 'append', index=False) #masukan data

current = datetime.now(pytz.timezone('Asia/Jakarta'))
print("Vertex to Data Staging (Datetime) : " + str(current))

