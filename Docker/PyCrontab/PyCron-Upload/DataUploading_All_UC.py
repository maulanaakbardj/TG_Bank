import pyTigerGraph as tg
import pandas as pd
from datetime import datetime
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
import numpy as np
import pytz


trx_uc4 = pd.read_csv('/app/UC04_Data1.csv', sep=";")
anb_uc4 = pd.read_csv('/app/UC04_NonBSIData.csv', sep=";")
cust_uc4 = pd.read_csv('/app/UC04_CustomerData.csv', sep=";")

trx_uc9=pd.read_csv("/app/Transactional_1_UC9.csv")
atm_uc9=pd.read_csv("/app/REF_ATM_Machine_1_UC9.csv")
ib_loc_uc9=pd.read_csv("/app/IBank_Trx_Location_1_UC9.csv")
ib_dev_uc9=pd.read_csv("/app/REF_IBank_Device_1_UC9.csv")
mob_loc_uc9=pd.read_csv("/app/Mobile_Trx_Location_1_UC9.csv")
mob_dev_uc9=pd.read_csv("/app/REF_Mobile_Device_1_UC9.csv")
mob_tel_uc9=pd.read_csv("/app/REF_Mobile_Telco_1_UC9.csv")
cust_uc9=pd.read_csv("/app/Customer1_UC9.csv")

credit_uc6=pd.read_csv("/app/credit.csv")


# Generate Random Transaction Datetime
def random_dates(start, end, n=10):
        start_date = start.value//10**9
        end_date = end.value//10**9
    
        return pd.to_datetime(np.random.randint(start_date, end_date,n),unit='s')

def random_dates1(start, end, n=30):
        start_date = start.value//10**9
        end_date = end.value//10**9
    
        return pd.to_datetime(np.random.randint(start_date, end_date,n),unit='s')


start = pd.to_datetime(datetime.now()+ relativedelta(hours=-1))
end = pd.to_datetime(datetime.now())
data_tgl1 = random_dates(start, end)
data_tgl2 = random_dates(start, end)
data_tgl3 = random_dates(start, end)
tgl_trx1 = pd.DataFrame(data_tgl1)
tgl_trx2 = pd.DataFrame(data_tgl2)
tgl_trx3 = pd.DataFrame(data_tgl3)
tgl_trx = pd.concat([tgl_trx1,tgl_trx2,tgl_trx3], axis=1)
tgl_trx.columns =['ATM_Datetime', 'Mobile_Datetime', 'IBank_Datetime']
trx_uc4['ATM_Trx_Datetime'] = tgl_trx['ATM_Datetime']
trx_uc4['Mobile_App_Trx_Datetime'] = tgl_trx['Mobile_Datetime']
trx_uc4['IBank_Trx_Datetime'] = tgl_trx['IBank_Datetime']

trx_uc9_now = datetime.now(pytz.timezone('Asia/Jakarta'))
current_uc9_trx = trx_uc9_now.strftime("%Y-%m-%d %H:%M:%S")


trx_uc9['ATM_Trx_Datetime'] = current_uc9_trx
trx_uc9['Mobile_App_Trx_Datetime'] = current_uc9_trx
trx_uc9['IBank_Trx_Datetime'] = current_uc9_trx


min_val = 5000000
max_val = 200000000

trx_uc9['ATM_Trx_Amount'] = trx_uc9['ATM_Trx_Amount'].apply(lambda x: np.random.randint(min_val, max_val))
trx_uc9['Mobile_App_Trx_Amount'] = trx_uc9['Mobile_App_Trx_Amount'] .apply(lambda x: np.random.randint(min_val, max_val))
trx_uc9['IBank_Trx_Amount'] = trx_uc9['IBank_Trx_Amount'].apply(lambda x: np.random.randint(min_val, max_val))

trx_uc4['ATM_Trx_Amount'] = trx_uc4['ATM_Trx_Amount'].apply(lambda x: np.random.randint(min_val, max_val))
trx_uc4['Mobile_App_Trx_Amount'] = trx_uc4['Mobile_App_Trx_Amount'] .apply(lambda x: np.random.randint(min_val, max_val))
trx_uc4['IBank_Trx_Amount'] = trx_uc4['IBank_Trx_Amount'].apply(lambda x: np.random.randint(min_val, max_val))

start1 = pd.to_datetime(datetime.now()+ relativedelta(days=-1))
end1 = pd.to_datetime(datetime.now())
data_tgl11 = random_dates1(start1, end1)
tgl_trx11 = pd.DataFrame(data_tgl11)
tgl_trx11 = pd.concat([tgl_trx11], axis=1)
tgl_trx11.columns =['Credit_Card_Trx_Datetime']
credit_uc6['Credit_Card_Trx_Datetime'] = tgl_trx11['Credit_Card_Trx_Datetime']
                 

trx_uc4 = trx_uc4.fillna(0)
# Change Data Type from String to Integer
trx_uc4['ATM_Trx_Code'] = trx_uc4['ATM_Trx_Code'].astype(np.int)
trx_uc4['ATM_Trx_ID'] = trx_uc4['ATM_Trx_ID'].astype(np.int64)
trx_uc4['Mobile_App_Trx_Code'] = trx_uc4['Mobile_App_Trx_Code'].astype(np.int64)
trx_uc4['Mobile_App_Trx_ID'] = trx_uc4['Mobile_App_Trx_ID'].astype(np.int64)
trx_uc4['IBank_Trx_Code'] = trx_uc4['IBank_Trx_Code'].astype(np.int64)
trx_uc4['IBank_Trx_ID'] = trx_uc4['IBank_Trx_ID'].astype(np.int64)

# Change Dataframe Data type according to vertex Data type
trx_uc4['Account_Debit_BSI_ID'] = trx_uc4['Account_Debit_BSI_ID'].astype(str)
trx_uc4['ATM_Card_ID'] = trx_uc4['ATM_Card_ID'].astype(str)
trx_uc4['ATM_Machine_ID'] = trx_uc4['ATM_Machine_ID'].astype(str)
trx_uc4['ATM_Trx_ID'] = trx_uc4['ATM_Trx_ID'].astype(str)
trx_uc4['ATM_Trx_Code'] = trx_uc4['ATM_Trx_Code'].astype(int)
trx_uc4['ATM_Trx_Type'] = trx_uc4['ATM_Trx_Type'].astype(str)
trx_uc4['ATM_Trx_Amount'] = trx_uc4['ATM_Trx_Amount'].astype(int)
trx_uc4['ATM_Trx_Datetime'] = trx_uc4['ATM_Trx_Datetime'].astype(str)
trx_uc4['ATM_Account_Debit_BSI_ID_Receiver'] = trx_uc4['ATM_Account_Debit_BSI_ID_Receiver'].astype(str)

trx_uc4['Mobile_App_ID'] = trx_uc4['Mobile_App_ID'].astype(str)
trx_uc4['Mobile_Location_ID'] = trx_uc4['Mobile_Location_ID'].astype(str)
trx_uc4['Mobile_App_Trx_ID'] = trx_uc4['Mobile_App_Trx_ID'].astype(str)
trx_uc4['Mobile_App_Trx_Code'] = trx_uc4['Mobile_App_Trx_Code'].astype(int)
trx_uc4['Mobile_App_Trx_Type'] = trx_uc4['Mobile_App_Trx_Type'].astype(str)
trx_uc4['Mobile_App_Trx_Amount'] = trx_uc4['Mobile_App_Trx_Amount'].astype(int)
trx_uc4['Mobile_App_Trx_Datetime'] = trx_uc4['Mobile_App_Trx_Datetime'].astype(str)
trx_uc4['Mobile_App_Account_Debit_BSI_ID_Receiver'] = trx_uc4['Mobile_App_Account_Debit_BSI_ID_Receiver'].astype(str)

trx_uc4['IBank_ID'] = trx_uc4['IBank_ID'].astype(str)
trx_uc4['IBank_IP_Address'] = trx_uc4['IBank_IP_Address'].astype(str)
trx_uc4['IBank_Trx_ID'] = trx_uc4['IBank_Trx_ID'].astype(str)
trx_uc4['IBank_Trx_Code'] = trx_uc4['IBank_Trx_Code'].astype(int)
trx_uc4['IBank_Trx_Type'] = trx_uc4['IBank_Trx_Type'].astype(str)
trx_uc4['IBank_Trx_Amount'] = trx_uc4['IBank_Trx_Amount'].astype(int)
trx_uc4['IBank_Trx_Datetime'] = trx_uc4['IBank_Trx_Datetime'].astype(str)
trx_uc4['IBank_Account_Debit_BSI_ID_Receiver'] = trx_uc4['IBank_Account_Debit_BSI_ID_Receiver'].astype(str)

cust_uc4['Account_Credit_BSI'] = cust_uc4['Account_Credit_BSI'].astype(str)
cust_uc4['User_KTP_ID'] = cust_uc4['User_KTP_ID'].astype(str)

#Replace all 0 with empty string
trx_uc4['ATM_Trx_ID'] = trx_uc4['ATM_Trx_ID'].astype(str).str.replace('^0$', '')
trx_uc4['ATM_Trx_Type'] = trx_uc4['ATM_Trx_Type'].astype(str).str.replace('^0$', '')
trx_uc4['ATM_Trx_Datetime'] = trx_uc4['ATM_Trx_Datetime'].astype(str).str.replace('^0$', '')
trx_uc4['ATM_Account_Debit_BSI_ID_Receiver'] = trx_uc4['ATM_Account_Debit_BSI_ID_Receiver'].astype(str).str.replace('^0.0$', '')
trx_uc4['ATM_Account_NonBSI_ID_Receiver'] = trx_uc4['ATM_Account_NonBSI_ID_Receiver'].astype(str).str.replace('^0$', '')

trx_uc4['Mobile_App_Trx_ID'] = trx_uc4['Mobile_App_Trx_ID'].astype(str).str.replace('^0$', '')
trx_uc4['Mobile_App_Trx_Type'] = trx_uc4['Mobile_App_Trx_Type'].astype(str).str.replace('^0$', '')
trx_uc4['Mobile_App_Trx_Datetime'] = trx_uc4['Mobile_App_Trx_Datetime'].astype(str).str.replace('^0$', '')
trx_uc4['Mobile_App_Account_Debit_BSI_ID_Receiver'] = trx_uc4['Mobile_App_Account_Debit_BSI_ID_Receiver'].astype(str).str.replace('^0.0$', '')
trx_uc4['Mobile_App_Account_NonBSI_ID_Receiver'] = trx_uc4['Mobile_App_Account_NonBSI_ID_Receiver'].astype(str).str.replace('^0$', '')

trx_uc4['IBank_Trx_ID'] = trx_uc4['IBank_Trx_ID'].astype(str).str.replace('^0$', '')
trx_uc4['IBank_Trx_Type'] = trx_uc4['IBank_Trx_Type'].astype(str).str.replace('^0$', '')
trx_uc4['IBank_Trx_Datetime'] = trx_uc4['IBank_Trx_Datetime'].astype(str).str.replace('^0$', '')
trx_uc4['IBank_Account_Debit_BSI_ID_Receiver'] = trx_uc4['IBank_Account_Debit_BSI_ID_Receiver'].astype(str).str.replace('^0.0$', '')
trx_uc4['IBank_Account_NonBSI_ID_Receiver'] = trx_uc4['Mobile_App_Account_NonBSI_ID_Receiver'].astype(str).str.replace('^0$', '')


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
credit_uc6['Credit_Card_Trx_Code']=credit_uc6['Credit_Card_Trx_Code'].astype(int)
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

# Change Dataframe Data type according to vertex Data type
trx_uc9['Account_Debit_BSI_ID'] = trx_uc9['Account_Debit_BSI_ID'].astype(str)
trx_uc9['ATM_Card_ID'] = trx_uc9['ATM_Card_ID'].astype(str)
trx_uc9['ATM_Machine_ID'] = trx_uc9['ATM_Machine_ID'].astype(str)
trx_uc9['ATM_Trx_ID'] = trx_uc9['ATM_Trx_ID'].astype(str)
trx_uc9['ATM_Trx_Code'] = trx_uc9['ATM_Trx_Code'].astype(int)
trx_uc9['ATM_Trx_Type'] = trx_uc9['ATM_Trx_Type'].astype(str)
trx_uc9['ATM_Trx_Amount'] = trx_uc9['ATM_Trx_Amount'].astype(int)
trx_uc9['ATM_Trx_Datetime'] = trx_uc9['ATM_Trx_Datetime'].astype(str)
# trx_uc9['ATM_Trx_Datetime'] = pd.to_datetime(trx_uc9['ATM_Trx_Datetime'], format='%Y-%m-%d %H:%M:%S')
trx_uc9['Account_Debit_BSI_ID_ATM_Receiver'] = trx_uc9['Account_Debit_BSI_ID_ATM_Receiver'].astype(str)
trx_uc9['Mobile_App_ID'] = trx_uc9['Mobile_App_ID'].astype(str)
trx_uc9['Mobile_Location_ID'] = trx_uc9['Mobile_Location_ID'].astype(str)
trx_uc9['Mobile_App_Trx_ID'] = trx_uc9['Mobile_App_Trx_ID'].astype(str)
trx_uc9['Mobile_App_Trx_Code'] = trx_uc9['Mobile_App_Trx_Code'].astype(int)
trx_uc9['Mobile_App_Trx_Type'] = trx_uc9['Mobile_App_Trx_Type'].astype(str)
trx_uc9['Mobile_App_Trx_Amount'] = trx_uc9['Mobile_App_Trx_Amount'].astype(int)
trx_uc9['Mobile_App_Trx_Datetime'] = trx_uc9['Mobile_App_Trx_Datetime'].astype(str)
# trx_uc9['Mobile_App_Trx_Datetime'] = pd.to_datetime(trx_uc9['Mobile_App_Trx_Datetime'], format='%Y-%m-%d %H:%M:%S')
trx_uc9['Account_Debit_BSI_ID_Mobile_Receiver'] = trx_uc9['Account_Debit_BSI_ID_Mobile_Receiver'].astype(str)
trx_uc9['IBank_ID'] = trx_uc9['IBank_ID'].astype(str)
trx_uc9['IBank_IP_Address'] = trx_uc9['IBank_IP_Address'].astype(str)
trx_uc9['IBank_Trx_ID'] = trx_uc9['IBank_Trx_ID'].astype(str)
trx_uc9['IBank_Trx_Code'] = trx_uc9['IBank_Trx_Code'].astype(int)
trx_uc9['IBank_Trx_Type'] = trx_uc9['IBank_Trx_Type'].astype(str)
trx_uc9['IBank_Trx_Amount'] = trx_uc9['IBank_Trx_Amount'].astype(int)
trx_uc9['IBank_Trx_Datetime'] = trx_uc9['IBank_Trx_Datetime'].astype(str)
# trx_uc9['IBank_Trx_Datetime'] = pd.to_datetime(trx_uc9['IBank_Trx_Datetime'], format='%Y-%m-%d %H:%M:%S')
trx_uc9['Account_Debit_BSI_ID_IBank_Receiver'] = trx_uc9['Account_Debit_BSI_ID_IBank_Receiver'].astype(str)

atm_uc9['ATM_Machine_ID'] = atm_uc9['ATM_Machine_ID'].astype(str)
atm_uc9['ATM_Brand'] = atm_uc9['ATM_Brand'].astype(str)
atm_uc9['ATM_Type'] = atm_uc9['ATM_Type'].astype(str)
atm_uc9['ATM_Operation_Code'] = atm_uc9['ATM_Operation_Code'].astype(str)
atm_uc9['ATM_Operation_Time'] = atm_uc9['ATM_Operation_Time'].astype(str)
atm_uc9['ATM_Operation_Time_Start'] = atm_uc9['ATM_Operation_Time_Start'].astype(str)
atm_uc9['ATM_Operation_Time_End'] = atm_uc9['ATM_Operation_Time_End'].astype(str)
atm_uc9['ATM_Name'] = atm_uc9['ATM_Name'].astype(str)
atm_uc9['ATM_Latitude'] = atm_uc9['ATM_Latitude'].astype(float)
atm_uc9['ATM_Longitude'] = atm_uc9['ATM_Longitude'].astype(float)
atm_uc9['ATM_City'] = atm_uc9['ATM_City'].astype(str)
atm_uc9['ATM_Area'] = atm_uc9['ATM_Area'].astype(str)
atm_uc9['ATM_Address'] = atm_uc9['ATM_Address'].astype(str)

ib_loc_uc9['IBank_Device_ID'] = ib_loc_uc9['IBank_Device_ID'].astype(str)
ib_loc_uc9['IBank_IP_Address'] = ib_loc_uc9['IBank_IP_Address'].astype(str)
ib_loc_uc9['IBank_IP_Address_Range1'] = ib_loc_uc9['IBank_IP_Address_Range1'].astype(str)
ib_loc_uc9['IBank_IP_Address_Range2'] = ib_loc_uc9['IBank_IP_Address_Range2'].astype(str)
ib_loc_uc9['IBank_Inet_Provider'] = ib_loc_uc9['IBank_Inet_Provider'].astype(str)
ib_loc_uc9['IBank_Inet_Location'] = ib_loc_uc9['IBank_Inet_Location'].astype(str)
ib_loc_uc9['IBank_Inet_Latitude'] = ib_loc_uc9['IBank_Inet_Latitude'].astype(float)
ib_loc_uc9['IBank_Inet_Longitude'] = ib_loc_uc9['IBank_Inet_Longitude'].astype(float)

ib_dev_uc9['IBank_Device_ID'] =ib_dev_uc9['IBank_Device_ID'].astype(str)
ib_dev_uc9['IBank_Device_Type'] =ib_dev_uc9['IBank_Device_Type'].astype(str)

mob_loc_uc9['Mobile_Trx_Location_ID'] = mob_loc_uc9['Mobile_Trx_Location_ID'].astype(str)
mob_loc_uc9['Mobile_Device_ID'] = mob_loc_uc9['Mobile_Device_ID'].astype(str)
mob_loc_uc9['Mobile_GPS_Latitude'] = mob_loc_uc9['Mobile_GPS_Latitude'].astype(float)
mob_loc_uc9['Mobile_GPS_Longitude'] = mob_loc_uc9['Mobile_GPS_Longitude'].astype(float)
mob_loc_uc9['Mobile_GPS_City'] = mob_loc_uc9['Mobile_GPS_City'].astype(str)
mob_loc_uc9['Mobile_GPS_Area'] = mob_loc_uc9['Mobile_GPS_Area'].astype(str)

mob_dev_uc9['Mobile_Device_ID'] = mob_dev_uc9['Mobile_Device_ID'].astype(str)
mob_dev_uc9['Mobile_Telco_ID'] = mob_dev_uc9['Mobile_Telco_ID'].astype(str)
mob_dev_uc9['Mobile_Device_Brand'] = mob_dev_uc9['Mobile_Device_Brand'].astype(str)
mob_dev_uc9['Mobile_Device_OS_Type'] = mob_dev_uc9['Mobile_Device_OS_Type'].astype(str)
mob_dev_uc9['Mobile_Device_OS_Version'] = mob_dev_uc9['Mobile_Device_OS_Version'].astype(str)

mob_tel_uc9['Mobile_Telco_ID'] = mob_tel_uc9['Mobile_Telco_ID'].astype(str)
mob_tel_uc9['Mobile_Telco_Name'] = mob_tel_uc9['Mobile_Telco_Name'].astype(str)

cust_uc9['Account_Debit_BSI_ID'] = cust_uc9['Account_Debit_BSI_ID'].astype(str)
cust_uc9['Customer_ID'] = cust_uc9['Customer_ID'].astype(str)
cust_uc9['User_Name'] = cust_uc9['User_Name'].astype(str)
cust_uc9['User_Address'] = cust_uc9['User_Address'].astype(str)
cust_uc9['User_Gender'] = cust_uc9['User_Gender'].astype(str)
cust_uc9['User_BirthDate'] = cust_uc9['User_BirthDate'].astype(str)
cust_uc9['User_KTP_ID'] = cust_uc9['User_KTP_ID'].astype(str)


conn = tg.TigerGraphConnection(host="http://172.16.2.79")
conn.graphname = "Graph_Practice_New"

# UPSERT VERTEX
## upsertVertexDataframe(df, vertexType, v_id=None, attributes=None)
### conn.upsertVertexDataframe(df=person, vertexType='person', v_id='name')

v_ATM_Trx = conn.upsertVertexDataFrame(trx_uc4, "V_ATM_Trx", "ATM_Trx_ID", attributes= {"ATM_Trx_ID": "ATM_Trx_ID", "ATM_Trx_Code":"ATM_Trx_Code","ATM_Trx_Type":"ATM_Trx_Type","ATM_Trx_Amount":"ATM_Trx_Amount","ATM_Trx_Datetime":"ATM_Trx_Datetime"})
print(str(v_ATM_Trx) + " V_ATM_Trx Upserted")
v_Mobile_App_Trx = conn.upsertVertexDataFrame(trx_uc4, "V_Mobile_App_Trx", "Mobile_App_Trx_ID", attributes= {"Mobile_App_Trx_ID": "Mobile_App_Trx_ID", "Mobile_App_Trx_Code":"Mobile_App_Trx_Code","Mobile_App_Trx_Type":"Mobile_App_Trx_Type","Mobile_App_Trx_Amount":"Mobile_App_Trx_Amount","Mobile_App_Trx_Datetime":"Mobile_App_Trx_Datetime"})
print(str(v_Mobile_App_Trx) + " V_Mobile_App_Trx Upserted")
v_IBank_Trx = conn.upsertVertexDataFrame(trx_uc4, "V_IBank_Trx", "IBank_Trx_ID", attributes= {"IBank_Trx_ID": "IBank_Trx_ID", "IBank_Trx_Code":"IBank_Trx_Code","IBank_Trx_Type":"IBank_Trx_Type","IBank_Trx_Amount":"IBank_Trx_Amount","IBank_Trx_Datetime":"IBank_Trx_Datetime"})
print(str(v_IBank_Trx) + " V_IBank_Trx Upserted")

v_Account_Debit_BSI = conn.upsertVertexDataFrame(trx_uc4, "V_Account_Debit_BSI", "Account_Debit_BSI_ID", attributes= {"Account_ID":"Account_Debit_BSI_ID"})
print(str(v_Account_Debit_BSI) + " V_Account_Debit_BSI Upserted")

## If your Dataframe has receiver account value use this
v_Account_Debit_BSI = conn.upsertVertexDataFrame(trx_uc4, "V_Account_Debit_BSI", "ATM_Account_Debit_BSI_ID_Receiver", attributes= {"Account_ID":"ATM_Account_Debit_BSI_ID_Receiver"})
print(str(v_Account_Debit_BSI) + " V_Account_Debit_BSI Upserted")
v_Account_Debit_BSI = conn.upsertVertexDataFrame(trx_uc4, "V_Account_Debit_BSI", "Mobile_App_Account_Debit_BSI_ID_Receiver", attributes= {"Account_ID":"Mobile_App_Account_Debit_BSI_ID_Receiver"})
print(str(v_Account_Debit_BSI) + " V_Account_Debit_BSI Upserted")
v_Account_Debit_BSI = conn.upsertVertexDataFrame(trx_uc4, "V_Account_Debit_BSI", "IBank_Account_Debit_BSI_ID_Receiver", attributes= {"Account_ID":"IBank_Account_Debit_BSI_ID_Receiver"})
print(str(v_Account_Debit_BSI) + " V_Account_Debit_BSI Upserted")

v_Account_NonBSI = conn.upsertVertexDataFrame(anb_uc4, "V_Account_NonBSI", "Account_NonBSI", attributes={"NonBSI_Account_ID":"Account_NonBSI", "NonBSI_Account_Bank_Name":"NonBSI_Account_Bank_Name"})
print(str(v_Account_NonBSI) + " V_Account_NonBSI Upserted")
v_Customer = conn.upsertVertexDataFrame(cust_uc4, "V_Customer", "Customer_ID", attributes={"Customer_ID":"Customer_ID", "User_Name":"User_Name", "User_Address":"User_Address", "User_Gender":"User_Gender", "User_BirthDate":"User_BirthDate", "User_KTP_ID":"User_KTP_ID"})
print(str(v_Customer) + " v_Customer Upserted")


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

v_atm = conn.upsertVertexDataFrame(atm_uc9, "V_ATM_Machine", "ATM_Machine_ID", attributes= {"ATM_Machine_ID": "ATM_Machine_ID", "ATM_Brand":"ATM_Brand", "ATM_Type":"ATM_Type", "ATM_Operation_Code":"ATM_Operation_Code", "ATM_Operation_Time":"ATM_Operation_Time", "ATM_Operation_Time_Start":"ATM_Operation_Time_Start", "ATM_Operation_Time_End":"ATM_Operation_Time_End", "ATM_Operation_Time_End":"ATM_Operation_Time_End","ATM_Name": "ATM_Name","ATM_Latitude":"ATM_Latitude", "ATM_Longitude":"ATM_Longitude", "ATM_City":"ATM_City", "ATM_Area":"ATM_Area", "ATM_Address":"ATM_Address"})
print(str(v_atm) + " V_ATM_Machine VERTICES Upserted")
v_Mobile_Telco = conn.upsertVertexDataFrame(mob_tel_uc9, "V_Mobile_Telco", "Mobile_Telco_ID", attributes= {"Mobile_Telco_ID": "Mobile_Telco_ID", "Mobile_Telco_Name":"Mobile_Telco_Name"})
print(str(v_Mobile_Telco) + " V_Mobile_Telco VERTICES Upserted")
v_IBank_Device = conn.upsertVertexDataFrame(ib_dev_uc9, "V_IBank_Device", "IBank_Device_ID", attributes= {"IBank_Device_ID": "IBank_Device_ID", "IBank_Device_Type":"IBank_Device_Type"})
print(str(v_IBank_Device) + " V_IBank_Device VERTICES Upserted")
v_Mobile_Trx_Location = conn.upsertVertexDataFrame(mob_loc_uc9, "V_Mobile_Trx_Location", "Mobile_Trx_Location_ID", attributes= {"Mobile_Location_ID": "Mobile_Trx_Location_ID", "Mobile_GPS_Latitude":"Mobile_GPS_Latitude","Mobile_GPS_Longitude": "Mobile_GPS_Longitude", "Mobile_GPS_City":"Mobile_GPS_City", "Mobile_GPS_Area":"Mobile_GPS_Area"})
print(str(v_Mobile_Trx_Location) + " V_Mobile_Trx_Location VERTICES Upserted")
v_Mobile_Device = conn.upsertVertexDataFrame(mob_dev_uc9, "V_Mobile_Device", "Mobile_Device_ID", attributes= {"Mobile_Device_ID": "Mobile_Device_ID", "Mobile_Device_Brand":"Mobile_Device_Brand","Mobile_Device_OS_Type":"Mobile_Device_OS_Type","Mobile_Device_OS_Version":"Mobile_Device_OS_Version"})
print(str(v_Mobile_Device) + " V_Mobile_Device VERTICES Upserted")
v_IBank_Trx_Location = conn.upsertVertexDataFrame(ib_loc_uc9, "V_IBank_Trx_Location", "IBank_IP_Address", attributes= {"IBank_IP_Address": "IBank_IP_Address", "IBank_Inet_Location":"IBank_Inet_Location","IBank_IP_Address_Range1":"IBank_IP_Address_Range1","IBank_IP_Address_Range2":"IBank_IP_Address_Range2","IBank_Inet_Provider":"IBank_Inet_Provider", "IBank_Inet_Latitude":"IBank_Inet_Latitude", "IBank_Inet_Longitude":"IBank_Inet_Longitude"})
print(str(v_IBank_Trx_Location) + " V_IBank_Trx_Location VERTICES Upserted")
v_ATM_Trx = conn.upsertVertexDataFrame(trx_uc9, "V_ATM_Trx", "ATM_Trx_ID", attributes= {"ATM_Trx_ID": "ATM_Trx_ID", "ATM_Trx_Code":"ATM_Trx_Code","ATM_Trx_Type":"ATM_Trx_Type","ATM_Trx_Amount":"ATM_Trx_Amount","ATM_Trx_Datetime":"ATM_Trx_Datetime"})
print(str(v_ATM_Trx) + " V_ATM_Trx Upserted")
v_Mobile_App_Trx = conn.upsertVertexDataFrame(trx_uc9, "V_Mobile_App_Trx", "Mobile_App_Trx_ID", attributes= {"Mobile_App_Trx_ID": "Mobile_App_Trx_ID", "Mobile_App_Trx_Code":"Mobile_App_Trx_Code","Mobile_App_Trx_Type":"Mobile_App_Trx_Type","Mobile_App_Trx_Amount":"Mobile_App_Trx_Amount","Mobile_App_Trx_Datetime":"Mobile_App_Trx_Datetime"})
print(str(v_Mobile_App_Trx) + " V_Mobile_App_Trx Upserted")
v_IBank_Trx = conn.upsertVertexDataFrame(trx_uc9, "V_IBank_Trx", "IBank_Trx_ID", attributes= {"IBank_Trx_ID": "IBank_Trx_ID", "IBank_Trx_Code":"IBank_Trx_Code","IBank_Trx_Type":"IBank_Trx_Type","IBank_Trx_Amount":"IBank_Trx_Amount","IBank_Trx_Datetime":"IBank_Trx_Datetime"})
print(str(v_IBank_Trx) + " V_IBank_Trx Upserted")
v_Account_Debit_BSI = conn.upsertVertexDataFrame(trx_uc9, "V_Account_Debit_BSI", "Account_Debit_BSI_ID", attributes= {"Account_ID":"Account_Debit_BSI_ID"})
print(str(v_Account_Debit_BSI) + " V_Account_Debit_BSI Upserted")
v_Customer = conn.upsertVertexDataFrame(cust_uc9, "V_Customer", "Customer_ID", attributes= {"Customer_ID":"Customer_ID","User_Name":"User_Name","User_Address":"User_Address","User_Gender":"User_Gender","User_BirthDate":"User_BirthDate","User_KTP_ID":"User_KTP_ID"})
print(str(v_Customer) + " V_Customer")

## If your Dataframe has receiver account value use this
# v_Account_Debit_BSI = conn.upsertVertexDataFrame(trx_uc9, "V_Account_Debit_BSI", "Account_Debit_BSI_ID_ATM_Receiver", attributes= {"Account_ID":"Account_Debit_BSI_ID_ATM_Receiver"})
# print(str(v_Account_Debit_BSI) + " V_Account_Debit_BSI Upserted")
# v_Account_Debit_BSI = conn.upsertVertexDataFrame(trx_uc9, "V_Account_Debit_BSI", "Account_Debit_BSI_ID_Mobile_Receiver", attributes= {"Account_ID":"Account_Debit_BSI_ID_Mobile_Receiver"})
# print(str(v_Account_Debit_BSI) + " V_Account_Debit_BSI Upserted")
# v_Account_Debit_BSI = conn.upsertVertexDataFrame(trx_uc9, "V_Account_Debit_BSI", "Account_Debit_BSI_ID_IBank_Receiver", attributes= {"Account_ID":"Account_Debit_BSI_ID_IBank_Receiver"})
# print(str(v_Account_Debit_BSI) + " V_Account_Debit_BSI Upserted")


# UPSERT EDGE
## upsertEdgesDataframe(df, sourceVertexType, edgeType, targetVertexType, from_id=None, to_id=None, attributes=None)

e_ATM_Send = conn.upsertEdgeDataFrame (trx_uc4, "V_Account_Debit_BSI", "E_ATM_Send", "V_ATM_Trx", from_id="Account_Debit_BSI_ID", to_id="ATM_Trx_ID", attributes={})
print(str(e_ATM_Send) + " E_ATM_Send EDGES Upserted")
e_ATM_Receive = conn.upsertEdgeDataFrame (trx_uc4, "V_ATM_Trx", "E_ATM_Receive", "V_Account_Debit_BSI", from_id="ATM_Trx_ID", to_id="ATM_Account_Debit_BSI_ID_Receiver", attributes={})
print(str(e_ATM_Receive) + " E_ATM_Receive EDGES Upserted")
e_ATM_Receive_Account_NonBSI = conn.upsertEdgeDataFrame (trx_uc4, "V_ATM_Trx", "E_ATM_Receive_AccountNonBSI", "V_Account_NonBSI", from_id="ATM_Trx_ID", to_id="ATM_Account_NonBSI_ID_Receiver", attributes={})
print(str(e_ATM_Receive_Account_NonBSI) + " E_ATM_Receive_Account_NonBSI EDGES Upserted")
e_Use_Machine = conn.upsertEdgeDataFrame (trx_uc4, "V_ATM_Trx", "E_Use_Machine", "V_ATM_Machine", from_id="ATM_Trx_ID", to_id="ATM_Machine_ID", attributes={})
print(str(e_Use_Machine) + " E_Use_Machine EDGES Upserted")
e_Use_ATM_Card = conn.upsertEdgeDataFrame (trx_uc4, "V_ATM_Trx", "E_Use_ATM_Card", "V_ATM_Card_REF", from_id="ATM_Trx_ID", to_id="ATM_Card_ID", attributes={})
print(str(e_Use_ATM_Card) + " E_Use_ATM_Card EDGES Upserted")
e_Owns_ATM_Card = conn.upsertEdgeDataFrame (trx_uc4, "V_Account_Debit_BSI", "E_Owns_ATM_Card", "V_ATM_Card_REF", from_id="Account_Debit_BSI_ID", to_id="ATM_Card_ID", attributes={})
print(str(e_Owns_ATM_Card) + " E_Owns_ATM_Card")

e_Mobile_Send = conn.upsertEdgeDataFrame (trx_uc4, "V_Account_Debit_BSI", "E_Mobile_Send", "V_Mobile_App_Trx", from_id="Account_Debit_BSI_ID", to_id="Mobile_App_Trx_ID", attributes={})
print(str(e_Mobile_Send) + " E_Mobile_Send EDGES Upserted")
e_Mobile_Receive = conn.upsertEdgeDataFrame (trx_uc4, "V_Mobile_App_Trx", "E_Mobile_Receive", "V_Account_Debit_BSI", from_id="Mobile_App_Trx_ID", to_id="Mobile_App_Account_Debit_BSI_ID_Receiver", attributes={})
print(str(e_Mobile_Receive) + " E_Mobile_Receive EDGES Upserted")
e_Mobile_Receive_AccountNonBSI = conn.upsertEdgeDataFrame (trx_uc4, "V_Mobile_App_Trx", "E_Mobile_App_Receive_AccountNonBSI", "V_Account_NonBSI", from_id="Mobile_App_Trx_ID", to_id="Mobile_App_Account_NonBSI_ID_Receiver", attributes={})
print(str(e_Mobile_Receive_AccountNonBSI) + " E_Mobile_Receive_AccountNonBSI EDGES Upserted")
e_Mobile_Trx_Loc = conn.upsertEdgeDataFrame (trx_uc4, "V_Mobile_App_Trx", "E_Mobile_Trx_Loc", "V_Mobile_Trx_Location", from_id="Mobile_App_Trx_ID", to_id="Mobile_Location_ID", attributes={})
print(str(e_Mobile_Trx_Loc) + " E_Mobile_Trx_Loc EDGES Upserted")
e_Use_Mobile_App = conn.upsertEdgeDataFrame (trx_uc4, "V_Mobile_App_Trx", "E_Use_Mobile_App", "V_Mobile_App_REF", from_id="Mobile_App_Trx_ID", to_id="Mobile_App_ID", attributes={})
print(str(e_Use_Mobile_App) + " E_Use_Mobile_App EDGES Upserted")
e_Owns_Mobile_App = conn.upsertEdgeDataFrame (trx_uc4, "V_Account_Debit_BSI", "E_Owns_Mobile_App", "V_Mobile_App_REF", from_id="Account_Debit_BSI_ID", to_id="Mobile_App_ID", attributes={})
print(str(e_Owns_ATM_Card) + " E_Owns_Mobile_App EDGES Upserted")

e_IBank_Send = conn.upsertEdgeDataFrame (trx_uc4, "V_Account_Debit_BSI", "E_IBank_Send", "V_IBank_Trx", from_id="Account_Debit_BSI_ID", to_id="IBank_Trx_ID", attributes={})
print(str(e_IBank_Send) + " E_IBank_Send EDGES Upserted")
e_IBank_Receive = conn.upsertEdgeDataFrame (trx_uc4, "V_IBank_Trx", "E_IBank_Receive", "V_Account_Debit_BSI", from_id="IBank_Trx_ID", to_id="IBank_Account_Debit_BSI_ID_Receiver", attributes={})
print(str(e_IBank_Receive) + " E_IBank_Receive EDGES Upserted")
e_IBank_Receive_AccountNonBSI = conn.upsertEdgeDataFrame (trx_uc4, "V_IBank_Trx", "E_IBank_Receive_AccountNonBSI", "V_Account_NonBSI", from_id="IBank_Trx_ID", to_id="IBank_Account_NonBSI_ID_Receiver", attributes={})
print(str(e_IBank_Receive_AccountNonBSI) + " E_IBank_Receive_AccountNonBSI EDGES Upserted")
e_IBank_Trx_Loc = conn.upsertEdgeDataFrame (trx_uc4, "V_IBank_Trx", "E_IBank_Trx_Loc", "V_IBank_Trx_Location", from_id="IBank_Trx_ID", to_id="IBank_IP_Address", attributes={})
print(str(e_IBank_Trx_Loc) + " E_IBank_Trx_Loc EDGES Upserted")
e_Use_IBank = conn.upsertEdgeDataFrame (trx_uc4, "V_IBank_Trx", "E_Use_IBank", "V_IBank_REF", from_id="Mobile_App_Trx_ID", to_id="IBank_ID", attributes={})
print(str(e_Use_IBank) + " E_Use_IBank EDGES Upserted")
e_Owns_IBank = conn.upsertEdgeDataFrame (trx_uc4, "V_Account_Debit_BSI", "E_Owns_IBank", "V_IBank_REF", from_id="Account_Debit_BSI_ID", to_id="IBank_ID", attributes={})
print(str(e_Owns_IBank) + " E_Owns_IBank Upserted")

e_Has_Debit_Account = conn.upsertEdgeDataFrame (cust_uc4, "V_Customer", "E_Has_Debit_Account", "V_Account_Debit_BSI", from_id="Customer_ID", to_id="Account_Debit_BSI", attributes={})
print(str(e_Has_Debit_Account) + " E_Has_Debit_Account EDGES Upserted")


e_Located_Mobile = conn.upsertEdgeDataFrame ( mob_loc_uc9, "V_Mobile_Trx_Location", "E_Located_Mobile", "V_Mobile_Device", from_id="Mobile_Trx_Location_ID", to_id="Mobile_Device_ID", attributes={})
print(str(e_Located_Mobile) + " E_Located_Mobile EDGES Upserted")
e_Use_Mobile_Telco = conn.upsertEdgeDataFrame ( mob_dev_uc9, "V_Mobile_Device", "E_Use_Mobile_Telco", "V_Mobile_Telco", from_id="Mobile_Device_ID", to_id="Mobile_Telco_ID", attributes={})
print(str(e_Use_Mobile_Telco) + " E__Use_Mobile_Telco EDGES Upserted")
e_Use_Device = conn.upsertEdgeDataFrame ( ib_loc_uc9, "V_IBank_Trx_Location", "E_Use_Device", "V_IBank_Device", from_id="IBank_IP_Address", to_id="IBank_Device_ID", attributes={})
print(str(e_Use_Device) + " E_Use_Device EDGES Upserted")
e_ATM_Send = conn.upsertEdgeDataFrame (trx_uc9, "V_Account_Debit_BSI", "E_ATM_Send", "V_ATM_Trx", from_id="Account_Debit_BSI_ID", to_id="ATM_Trx_ID", attributes={})
print(str(e_ATM_Send) + " E_ATM_Send EDGES Upserted")
e_Use_Machine = conn.upsertEdgeDataFrame (trx_uc9, "V_ATM_Trx", "E_Use_Machine", "V_ATM_Machine", from_id="ATM_Trx_ID", to_id="ATM_Machine_ID", attributes={})
print(str(e_Use_Machine) + " E_Use_Machine EDGES Upserted")
e_Use_ATM_Card = conn.upsertEdgeDataFrame (trx_uc9, "V_ATM_Trx", "E_Use_ATM_Card", "V_ATM_Card_REF", from_id="ATM_Trx_ID", to_id="ATM_Card_ID", attributes={})
print(str(e_Use_ATM_Card) + " E_Use_ATM_Card EDGES Upserted")
e_Owns_ATM_Card = conn.upsertEdgeDataFrame (trx_uc9, "V_Account_Debit_BSI", "E_Owns_ATM_Card", "V_ATM_Card_REF", from_id="Account_Debit_BSI_ID", to_id="ATM_Card_ID", attributes={})
print(str(e_Owns_ATM_Card) + " E_Owns_ATM_Card")
e_Mobile_Send = conn.upsertEdgeDataFrame (trx_uc9, "V_Account_Debit_BSI", "E_Mobile_Send", "V_Mobile_App_Trx", from_id="Account_Debit_BSI_ID", to_id="Mobile_App_Trx_ID", attributes={})
print(str(e_Mobile_Send) + " E_Mobile_Send EDGES Upserted")
e_Mobile_Trx_Loc = conn.upsertEdgeDataFrame (trx_uc9, "V_Mobile_App_Trx", "E_Mobile_Trx_Loc", "V_Mobile_Trx_Location", from_id="Mobile_App_Trx_ID", to_id="Mobile_Location_ID", attributes={})
print(str(e_Mobile_Trx_Loc) + " E_Mobile_Trx_Loc EDGES Upserted")
e_Use_Mobile_App = conn.upsertEdgeDataFrame (trx_uc9, "V_Mobile_App_Trx", "E_Use_Mobile_App", "V_Mobile_App_REF", from_id="Mobile_App_Trx_ID", to_id="Mobile_App_ID", attributes={})
print(str(e_Use_Mobile_App) + " E_Use_Mobile_App EDGES Upserted")
e_Owns_Mobile_App = conn.upsertEdgeDataFrame (trx_uc9, "V_Account_Debit_BSI", "E_Owns_Mobile_App", "V_Mobile_App_REF", from_id="Account_Debit_BSI_ID", to_id="Mobile_App_ID", attributes={})
print(str(e_Owns_ATM_Card) + " E_Owns_Mobile_App")
e_IBank_Send = conn.upsertEdgeDataFrame (trx_uc9, "V_Account_Debit_BSI", "E_IBank_Send", "V_IBank_Trx", from_id="Account_Debit_BSI_ID", to_id="IBank_Trx_ID", attributes={})
print(str(e_IBank_Send) + " E_IBank_Send EDGES Upserted")
e_IBank_Trx_Loc = conn.upsertEdgeDataFrame (trx_uc9, "V_IBank_Trx", "E_IBank_Trx_Loc", "V_IBank_Trx_Location", from_id="IBank_Trx_ID", to_id="IBank_IP_Address", attributes={})
print(str(e_IBank_Trx_Loc) + " E_IBank_Trx_Loc EDGES Upserted")
e_Use_IBank = conn.upsertEdgeDataFrame (trx_uc9, "V_IBank_Trx", "E_Use_IBank", "V_IBank_REF", from_id="Mobile_App_Trx_ID", to_id="IBank_ID", attributes={})
print(str(e_Use_IBank) + " E_Use_IBank EDGES Upserted")
e_Owns_IBank = conn.upsertEdgeDataFrame (trx_uc9, "V_Account_Debit_BSI", "E_Owns_IBank", "V_IBank_REF", from_id="Account_Debit_BSI_ID", to_id="IBank_ID", attributes={})
print(str(e_Owns_IBank) + " E_Owns_IBank Upserted")
e_Has_Debit_Account = conn.upsertEdgeDataFrame (cust_uc9, "V_Customer", "E_Has_Debit_Account", "V_Account_Debit_BSI", from_id="Customer_ID", to_id="Account_Debit_BSI_ID", attributes={})
print(str(e_Has_Debit_Account) + " E_Has_Debit_Account")

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
