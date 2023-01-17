import pyTigerGraph as tg
import sqlalchemy as db
import pandas as pd
import pymysql
from datetime import datetime
import pytz

conn = tg.TigerGraphConnection(host="http://172.16.2.79")
conn.graphname = "Graph_Practice_New"

Result_uc4 = conn.runInstalledQuery("UC04_QRY02_Multichannel1_Results")
Result_uc4 = Result_uc4[0]['Results']
df_uc4 = pd.json_normalize(Result_uc4)
Result1_uc4 = conn.runInstalledQuery("UC04_QRY03_Multichannel1_Customer")
Result1_uc4 = Result1_uc4[0]['Details']
df1_uc4 = pd.json_normalize(Result1_uc4)
# output_uc6a = conn.runInstalledQuery("UC6a_QRY2_GetVertexUC6a")
# df_uc6a = pd.json_normalize(output_uc6a[0]['trx'])
# output_uc6b = conn.runInstalledQuery("UC6b_QRY2_GetVertexUC6b")
# df_uc6b = pd.json_normalize(output_uc6b[0]['trx'])
output_uc9 = conn.runInstalledQuery("UC9_QRY2_GetVertexUC9")
df_uc9 = pd.json_normalize(output_uc9[0]['myUC9'])


df1_uc4 = df1_uc4.drop(["v_type", "v_id"], axis='columns')
df_uc4 = df_uc4.drop(["v_type", "v_id"], axis='columns')
# df_uc6a = df_uc6a.drop(["v_id","v_type"], axis='columns')
# df_uc6b = df_uc6b.drop(["v_id","v_type"], axis='columns')
df_uc9 = df_uc9.drop(["v_id","v_type"], axis='columns')

df_uc4.rename(columns = {'attributes.Account_Sender':'Account_Sender',
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

df1_uc4.rename(columns = {'attributes.Account_ID':'Account_ID',
                    'attributes.Customer_ID':'Customer_ID',
                    'attributes.KTP_ID':'KTP_ID',
                    'attributes.Full_Name':'Full_Name',
                    'attributes.Date_of_Birth':'Date_of_Birth',
                    'attributes.Gender':'Gender',
                    'attributes.Email_Address':'Email_Address'},
                    inplace = True)

# df_uc6a.rename(columns = {'attributes.Credit_Card_Trx_ID':'Credit_Card_Trx_ID',
#                      'attributes.Credit_Card_Trx_Code':'Credit_Card_Trx_Code',
#                      'attributes.Credit_Card_Trx_Type':'Credit_Card_Trx_Type',
#                      'attributes.Credit_Card_Trx_Amount':'Credit_Card_Trx_Amount',
#                     'attributes.Amount':'Amount',
#                      'attributes.Account_Credit_Card_ID':'Account_Credit_Card_ID',
#                      'attributes.Credit_Card_Trx_Datetime':'Credit_Card_Trx_Datetime',
#                      'attributes.EDC_Name':'EDC_Name',
#                      'attributes.EDC_City':'EDC_City',
#                      'attributes.EDC_Address':'EDC_Address',
#                      'attributes.User_Name':'User_Name',
#                      'attributes.User_Address':'User_Address',
#                      'attributes.User_Gender':'User_Gender',
#                      'attributes.User_BirthDate':'User_BirthDate',
#                      'attributes.User_KTP_ID':'User_KTP_ID'
#                     },
#                      inplace = True)


# df_uc6b.rename(columns = {'attributes.Credit_Card_Trx_ID':'Credit_Card_Trx_ID',
#                      'attributes.Credit_Card_Trx_Code':'Credit_Card_Trx_Code',
#                      'attributes.Credit_Card_Trx_Type':'Credit_Card_Trx_Type',
#                      'attributes.Credit_Card_Trx_Amount':'Credit_Card_Trx_Amount',
#                      'attributes.Account_Credit_Card_ID':'Account_Credit_Card_ID',
#                      'attributes.Credit_Card_Trx_Datetime':'Credit_Card_Trx_Datetime',
#                      'attributes.EDC_Name':'EDC_Name',
#                      'attributes.EDC_City':'EDC_City',
#                      'attributes.EDC_Address':'EDC_Address',
#                      'attributes.Operation_Time_Start':'EDC_Operation_Time_Start',
#                      'attributes.Operation_Time_End':'EDC_Operation_Time_End',                       
#                      'attributes.User_Name':'User_Name',
#                      'attributes.User_Address':'User_Address',
#                      'attributes.User_Gender':'User_Gender',
#                      'attributes.User_BirthDate':'User_BirthDate',
#                      'attributes.User_KTP_ID':'User_KTP_ID'
#                     },
#                      inplace = True)

df_uc9.rename(columns = {'attributes.Rekening_ID':'Rekening_ID',
                     'attributes.Total_Transaksi':'Total_Transaksi',
                     'attributes.ATM_Area_Location':'ATM_Area_Location',
                     'attributes.ATM_City':'ATM_City',
                     'attributes.ATM_Trx_Date':'ATM_Trx_Date',
                     'attributes.ATM_Latitude':'ATM_Latitude',
                     'attributes.ATM_Longitude':'ATM_Longitude',
                     'attributes.ATM_Trx_Amount':'ATM_Trx_Amount',
                     'attributes.Mobile_App_Area_Location':'Mobile_App_Area_Location',
                     'attributes.Mobile_App_City':'Mobile_App_City',
                     'attributes.Mobile_App_Trx_Date':'Mobile_App_Trx_Date',
                     'attributes.Mobile_App_Latitude':'Mobile_App_Latitude',
                     'attributes.Mobile_App_Longitude':'Mobile_App_Longitude',
                     'attributes.Mobile_App_Provider':'Mobile_App_Provider',
                     'attributes.Mobile_App_Device':'Mobile_App_Device',
                     'attributes.Mobile_App_Trx_Amount':'Mobile_App_Trx_Amount',
                     'attributes.Ibank_Area_Location':'Ibank_Area_Location',
                     'attributes.Ibank_Area_Location':'Ibank_Area_Location',
                     'attributes.Ibank_Device':'Ibank_Device',
                     'attributes.Ibank_Trx_Date':'Ibank_Trx_Date',
                     'attributes.Ibank_Latitude':'Ibank_Latitude',
                     'attributes.Ibank_Longitude':'Ibank_Longitude',
                     'attributes.Ibank_Provider':'Ibank_Provider',
                     'attributes.Ibank_Trx_Amount':'Ibank_Trx_Amount',
                     'attributes.User_Name':'User_Name',
                     'attributes.User_Address':'User_Address',
                     'attributes.User_Gender':'User_Gender',
                     'attributes.User_BirthDate':'User_BirthDate',
                     'attributes.User_KTP_ID':'User_KTP_ID',
                     'attributes.Customer_ID':'Customer_ID',
                     'attributes.Use_Case':'Use_Case'
                    },
                     inplace = True)


now = datetime.now(pytz.timezone('Asia/Jakarta'))
current_dateTime = now.strftime("%Y-%m-%d %H:%M")

df_uc4['Anomaly_Datetime'] = current_dateTime
# df_uc6a['Anomaly_timestamp'] = current_dateTime
# df_uc6b['Anomaly_timestamp'] = current_dateTime
df_uc9['Anomaly_timestamp'] = current_dateTime
df_uc9['Anomaly_timestamp'] = current_dateTime

engine = db.create_engine("mysql+pymysql://root:Password1234@172.16.11.222/Grafana") #masih mariadb local blom mariadb server
df_uc4.to_sql(name='UC04_Results', con=engine, if_exists = 'append', index=False)
df1_uc4.to_sql(name='UC04_Account_Details', con=engine, if_exists = 'replace', index=False)
# df_uc6a.to_sql(name='UC6a', con=engine, if_exists = 'append', index=False) #masukan data
# df_uc6b.to_sql(name='UC6b', con=engine, if_exists = 'append', index=False) #masukan data
df_uc9.to_sql(name='UC9', con=engine, if_exists = 'append', index=False) #masukan data

current = datetime.now(pytz.timezone('Asia/Jakarta'))
print("Vertex to Data Staging (Datetime) : " + str(current))
