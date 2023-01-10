import pyTigerGraph as tg
import sqlalchemy as db
import pymysql
from datetime import datetime
import pytz

conn = tg.TigerGraphConnection(host="http://172.16.11.223")
conn.graphname = "Team_Grafana"

output_uc9 = conn.runInstalledQuery("UC9_QRY2_GetVertexUC9")
import pandas as pd
df_uc9 = pd.json_normalize(output_uc9[0]['myUC9'])
df_uc9 = df_uc9.drop(["v_id","v_type"], axis='columns')

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


df_uc9['Anomaly_timestamp'] = current_dateTime

engine = db.create_engine("mysql+pymysql://root:password@192.168.100.8/Grafana") // masih mariadb local blom mariadb server
df_uc9.to_sql(name='UC9', con=engine, if_exists = 'append', index=False) #masukan data

current = datetime.now(pytz.timezone('Asia/Jakarta'))
print("Vertex to Data Staging (Datetime) : " + str(current))
