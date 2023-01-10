import pyTigerGraph as tg
import pandas as pd
from datetime import datetime
import pytz

trx_uc9=pd.read_csv("/app/Transactional_1_UC9.csv")
atm_uc9=pd.read_csv("/app/REF_ATM_Machine_1_UC9.csv")
ib_loc_uc9=pd.read_csv("/app/IBank_Trx_Location_1_UC9.csv")
ib_dev_uc9=pd.read_csv("/app/REF_IBank_Device_1_UC9.csv")
mob_loc_uc9=pd.read_csv("/app/Mobile_Trx_Location_1_UC9.csv")
mob_dev_uc9=pd.read_csv("/app/REF_Mobile_Device_1_UC9.csv")
mob_tel_uc9=pd.read_csv("/app/REF_Mobile_Telco_1_UC9.csv")
cust_uc9=pd.read_csv("/app/Customer1_UC9.csv")


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


conn = tg.TigerGraphConnection(host="http://172.16.11.223")
conn.graphname = "Team_Grafana"

# UPSERT VERTEX
## upsertVertexDataframe(df, vertexType, v_id=None, attributes=None)
### conn.upsertVertexDataframe(df=person, vertexType='person', v_id='name')

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

current_dateTime = datetime.now(pytz.timezone('Asia/Jakarta'))
print("Uploading data Success (Datetime) : " + str(current_dateTime))
