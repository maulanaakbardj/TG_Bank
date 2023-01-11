#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyTigerGraph as tg
import pandas as pd
from datetime import datetime
import pytz

credit_uc6=pd.read_csv("/app/credit.csv")

# Change Dataframe Data type according to vertex Data type
credit_uc6['Customer_ID']=credit_uc6['Customer_ID'].astype(str)
credit_uc6['User_Name']=credit_uc6['User_Name'].astype(str)
credit_uc6['User_Address']=credit_uc6['User_Address'].astype(str)
credit_uc6['User_Gender']=credit_uc6['User_Gender'].astype(str)
credit_uc6['User_BirthDate']=credit_uc6['User_BirthDate'].astype(str)
credit_uc6['User_KTP_ID']=credit_uc6['User_KTP_ID'].astype(str)
credit_uc6['User_Name']=credit_uc6['User_Name'].astype(str)

credit_uc6['Account_Credit_Card_ID']=credit_uc6['Account_Credit_Card_ID'].astype(str)

credit_uc6['Credit_Card_Trx_ID']=credit_uc6['Credit_Card_Trx_ID'].astype(str)
credit_uc6['Credit_Card_Trx_Code']=credit_uc6['Credit_Card_Trx_Code'].astype(str)
credit_uc6['Credit_Card_Trx_Type']=credit_uc6['Credit_Card_Trx_Type'].astype(str)
credit_uc6['Credit_Card_Trx_Amount']=credit_uc6['Credit_Card_Trx_Amount'].astype(int)
credit_uc6['Credit_Card_Trx_Datetime']=credit_uc6['Credit_Card_Trx_Datetime'].astype(str)

credit_uc6['EDC_ID']=credit_uc6['EDC_ID'].astype(str)
credit_uc6['EDC_Brand']=credit_uc6['EDC_Brand'].astype(str)
credit_uc6['EDC_Type']=credit_uc6['EDC_Type'].astype(str)
credit_uc6['EDC_Operation_Time']=credit_uc6['EDC_Operation_Time'].astype(str)
credit_uc6['EDC_Operation_Time_Start']=credit_uc6['EDC_Operation_Time_Start'].astype(str)
credit_uc6['EDC_Operation_Time_End']=credit_uc6['EDC_Operation_Time_End'].astype(str)
credit_uc6['EDC_Country']=credit_uc6['EDC_Country'].astype(str)
credit_uc6['EDC_City']=credit_uc6['EDC_City'].astype(str)
credit_uc6['EDC_Area']=credit_uc6['EDC_Area'].astype(str)
credit_uc6['EDC_City']=credit_uc6['EDC_City'].astype(str)
credit_uc6['EDC_Address']=credit_uc6['EDC_Address'].astype(str)

conn = tg.TigerGraphConnection(host="http://172.16.11.223")
conn.graphname = "Team_Grafana"

v_Customer = conn.upsertVertexDataFrame(credit_uc6, "V_Customer", "Customer_ID", 
                                        attributes= {"Customer_ID": "Customer_ID", 
                                                     "User_Name":"User_Name", 
                                                     "User_Address":"User_Address", 
                                                     "User_Gender":"User_Gender", 
                                                     "User_BirthDate":"User_BirthDate",  
                                                     "User_KTP_ID":"User_KTP_ID"})
print(str(v_Customer) + " V_Customer VERTICES Upserted")

v_Account_Credit_BSI = conn.upsertVertexDataFrame(credit_uc6, "V_Account_Credit_BSI", "Account_Credit_Card_ID", 
                                        attributes= {"Account_Credit_Card_ID": "Account_Credit_Card_ID"})
print(str(v_Account_Credit_BSI) + "V_Account_Credit_BSI VERTICES Upserted")

v_Credit_Card_Trx = conn.upsertVertexDataFrame(credit_uc6, "V_Credit_Card_Trx", "Credit_Card_Trx_ID", 
                                        attributes= {"Credit_Card_Trx_ID": "Credit_Card_Trx_ID", 
                                                     "Credit_Card_Trx_Code":"Credit_Card_Trx_Code", 
                                                     "Credit_Card_Trx_Type":"Credit_Card_Trx_Type", 
                                                     "Credit_Card_Trx_Amount":"Credit_Card_Trx_Amount",
                                                     "Credit_Card_Trx_Datetime":"Credit_Card_Trx_Datetime"})
print(str(v_Credit_Card_Trx) + " V_Credit_Card_Trx VERTICES Upserted")

v_EDC_Device = conn.upsertVertexDataFrame(credit_uc6, "V_EDC_Device", "EDC_ID", 
                                        attributes= {"EDC_ID": "EDC_ID", 
                                                     "EDC_Brand":"EDC_Brand", 
                                                     "EDC_Type":"EDC_Type",
                                                     "EDC_Operation_Time":"EDC_Operation_Time",
                                                     "EDC_Operation_Time_Start":"EDC_Operation_Time_Start",
                                                     "EDC_Operation_Time_End":"EDC_Operation_Time_End",
                                                     "EDC_Name":"EDC_Name", 
                                                     "EDC_Country":"EDC_Country",
                                                     "EDC_City":"EDC_City",
                                                     "EDC_Area":"EDC_Area",
                                                     "EDC_Address":"EDC_Address"})
print(str(v_EDC_Device) + " V_EDC_Device VERTICES Upserted")



e_Has_Credit_Account = conn.upsertEdgeDataFrame (credit_uc6, "V_Customer", 
                                             "E_Has_Credit_Account", 
                                             "V_Account_Credit_BSI", 
                                             from_id="Customer_ID", 
                                             to_id="Account_Credit_Card_ID", attributes={})
print(str(e_Has_Credit_Account) + " E_Has_Credit_Account EDGES Upserted")

e_Credit_Send = conn.upsertEdgeDataFrame (credit_uc6, "V_Account_Credit_BSI", 
                                             "E_Credit_Send", 
                                             "V_Credit_Card_Trx", 
                                             from_id="Account_Credit_Card_ID", 
                                             to_id="Credit_Card_Trx_ID", attributes={})
print(str(e_Credit_Send) + " E_Credit_Send EDGES Upserted")

e_Has_EDC_Device = conn.upsertEdgeDataFrame (credit_uc6, "V_Credit_Card_Trx", 
                                             "E_Has_EDC_Device", 
                                             "V_EDC_Device", 
                                             from_id="Credit_Card_Trx_ID", 
                                             to_id="EDC_ID", attributes={})
print(str(e_Has_EDC_Device) + " E_Has_EDC_Device EDGES Upserted")

current_dateTime = datetime.now(pytz.timezone('Asia/Jakarta'))
print("Uploading data Success (Datetime) : " + str(current_dateTime))

