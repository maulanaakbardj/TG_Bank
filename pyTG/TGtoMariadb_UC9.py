import pyTigerGraph as tg
import pandas as pd
import sqlalchemy as db
import pymysql


conn = tg.TigerGraphConnection(host="http://192.168.100.8")
conn.graphname = "Graph_Practice_New"
output = conn.runInstalledQuery("VertexUC_9")

df = pd.json_normalize(output[0]['myUC9'])
df = df.drop(["v_id","v_type"], axis='columns')

df.rename(columns = {'attributes.Rekening_ID':'Rekening_ID',
                     'attributes.Total_Transaksi':'Total_Transaksi',
                     'attributes.ATM_Area_Location':'ATM_Area_Location',
                     'attributes.ATM_City':'ATM_City',
                     'attributes.ATM_Trx_Date':'ATM_Trx_Date',
                     'attributes.ATM_Latitude':'ATM_Latitude',
                     'attributes.ATM_Longitude':'ATM_Longitude',
                     'attributes.Mobile_App_Area_Location':'Mobile_App_Area_Location',
                     'attributes.Mobile_App_City':'Mobile_App_City',
                     'attributes.Mobile_App_Trx_Date':'Mobile_App_Trx_Date',
                     'attributes.Mobile_App_Latitude':'Mobile_App_Latitude',
                     'attributes.Mobile_App_Longitude':'Mobile_App_Longitude',
                     'attributes.Mobile_App_Provider':'Mobile_App_Provider',
                     'attributes.Ibank_Area_Location':'Ibank_Area_Location',
                     'attributes.Ibank_Device':'Ibank_Device',
                     'attributes.Ibank_Trx_Date':'Ibank_Trx_Date',
                     'attributes.Ibank_Latitude':'Ibank_Latitude',
                     'attributes.Ibank_Longitude':'Ibank_Longitude',
                     'attributes.Ibank_Provider':'Ibank_Provider'},
                     inplace = True)

engine = db.create_engine("mysql+pymysql://root:password@localhost/dsuc")
df.to_sql(name='myUC9', con=engine, if_exists = 'append', index=False) 
