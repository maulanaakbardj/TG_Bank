# 
import pyTigerGraph as tg

conn = tg.TigerGraphConnection(host="http://35.228.83.191", username="tigergraph", password="tigergraph")
conn.graphname = "GRAPH_PRACTICE2"
#conn.apiToken = conn.getToken(conn.createSecret())
#test = conn.apiToken
#test

# 
Result = conn.runInstalledQuery("UC04_QRY02_Multichannel1_Results")
Result = Result[0]['Results']
Result

# 
import pandas as pd
df = pd.json_normalize(Result)
df

# 
df = df.drop(["v_type", "v_id"], axis='columns')

# 
from datetime import datetime
import time

df['Anomaly_Datetime'] = pd.to_datetime(datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M"))

# 
df.rename(columns = {'attributes.Account_Sender':'Account_Sender',
                    'attributes.Account_Receiver':'Account_Receiver',
                    'attributes.ATM_Trx_ID':'ATM_Trx_ID',
                    'attributes.ATM_Trx_Amount':'ATM_Trx_Amount',
                    'attributes.ATM_Trx_Datetime':'ATM_Trx_Datetime',
                    'attributes.Mobile_Trx_ID':'Mobile_Trx_ID',
                    'attributes.Mobile_Trx_Amount':'Mobile_Trx_Amount',
                    'attributes.Mobile_Trx_Datetime':'Mobile_Trx_Datetime',
                    'attributes.IBank_Trx_ID':'IBank_Trx_ID',
                    'attributes.IBank_Trx_Amount':'IBank_Trx_Amount',
                    'attributes.IBank_Trx_Datetime':'IBank_Trx_Datetime',
                    'attributes.Total_Transaction':'Total_Transaction',
                    'attributes.Anomaly_Datetime':'Anomaly_Datetime',
                    'attributes.Use_Case':'Use_Case'},
                    inplace = True)

# 
df.head()

#  [markdown]
# Account Details

# 
Result1 = conn.runInstalledQuery("UC04_QRY03_Multichannel1_Customer")
Result1 = Result1[0]['Details']
Result1

# 
import pandas as pd
df1 = pd.json_normalize(Result1)
df1

# 
df1 = df1.drop(["v_type", "v_id"], axis='columns')

# 
df1.head()

# 
df1.rename(columns = {'attributes.Account_ID':'Account_ID',
                    'attributes.Customer_ID':'Customer_ID',
                    'attributes.KTP_ID':'KTP_ID',
                    'attributes.Full_Name':'Full_Name',
                    'attributes.Date_of_Birth':'Date_of_Birth',
                    'attributes.Gender':'Gender',
                    'attributes.Email_Address':'Email_Address'},
                    inplace = True)

# 
df1.head()

#  [markdown]
# Connect to MariaDB

# 
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:root@localhost/uc04_data')

# 
sql = pd.read_sql_table("results",engine)
sql

# 
df.to_sql(name='results', con=engine, if_exists = 'append', index=False)

# 
sql1 = pd.read_sql_table("account_details",engine)
sql1

# 
df1.to_sql(name='account_details', con=engine, if_exists = 'replace', index=False)


