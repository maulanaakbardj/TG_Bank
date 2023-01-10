# 
import pyTigerGraph as tg
import pandas as pd
from datetime import datetime
import numpy as np
import pytz
from dateutil.relativedelta import relativedelta
from datetime import datetime
import warnings
warnings.filterwarnings("ignore")

# 
trx = pd.read_csv('UC04_TrxData/UC04_Data3.csv', sep=";")
anb = pd.read_csv('UC04_NonBSIData.csv', sep=";")
cust = pd.read_csv('UC04_CustomerData.csv', sep=";")

# 
trx.info()

# 
trx = trx.fillna(0)

# 
# Generate Random Transaction Datetime
def random_dates(start, end, n=10):
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
trx['ATM_Trx_Datetime'] = tgl_trx['ATM_Datetime']
trx['Mobile_App_Trx_Datetime'] = tgl_trx['Mobile_Datetime']
trx['IBank_Trx_Datetime'] = tgl_trx['IBank_Datetime']

# 
# Change Data Type from String to Integer
trx['ATM_Trx_Code'] = trx['ATM_Trx_Code'].astype(np.int64)
trx['ATM_Trx_ID'] = trx['ATM_Trx_ID'].astype(np.int64)
trx['Mobile_App_Trx_Code'] = trx['Mobile_App_Trx_Code'].astype(np.int64)
trx['Mobile_App_Trx_ID'] = trx['Mobile_App_Trx_ID'].astype(np.int64)
trx['IBank_Trx_Code'] = trx['IBank_Trx_Code'].astype(np.int64)
trx['IBank_Trx_ID'] = trx['IBank_Trx_ID'].astype(np.int64)

# 
# Change Dataframe Data type according to vertex Data type
trx['Account_Debit_BSI_ID'] = trx['Account_Debit_BSI_ID'].astype(str)
trx['ATM_Card_ID'] = trx['ATM_Card_ID'].astype(str)
trx['ATM_Machine_ID'] = trx['ATM_Machine_ID'].astype(str)
trx['ATM_Trx_ID'] = trx['ATM_Trx_ID'].astype(str)
trx['ATM_Trx_Code'] = trx['ATM_Trx_Code'].astype(int)
trx['ATM_Trx_Type'] = trx['ATM_Trx_Type'].astype(str)
trx['ATM_Trx_Amount'] = trx['ATM_Trx_Amount'].astype(int)
trx['ATM_Trx_Datetime'] = trx['ATM_Trx_Datetime'].astype(str)
trx['ATM_Account_Debit_BSI_ID_Receiver'] = trx['ATM_Account_Debit_BSI_ID_Receiver'].astype(str)

trx['Mobile_App_ID'] = trx['Mobile_App_ID'].astype(str)
trx['Mobile_Location_ID'] = trx['Mobile_Location_ID'].astype(str)
trx['Mobile_App_Trx_ID'] = trx['Mobile_App_Trx_ID'].astype(str)
trx['Mobile_App_Trx_Code'] = trx['Mobile_App_Trx_Code'].astype(int)
trx['Mobile_App_Trx_Type'] = trx['Mobile_App_Trx_Type'].astype(str)
trx['Mobile_App_Trx_Amount'] = trx['Mobile_App_Trx_Amount'].astype(int)
trx['Mobile_App_Trx_Datetime'] = trx['Mobile_App_Trx_Datetime'].astype(str)
trx['Mobile_App_Account_Debit_BSI_ID_Receiver'] = trx['Mobile_App_Account_Debit_BSI_ID_Receiver'].astype(str)

trx['IBank_ID'] = trx['IBank_ID'].astype(str)
trx['IBank_IP_Address'] = trx['IBank_IP_Address'].astype(str)
trx['IBank_Trx_ID'] = trx['IBank_Trx_ID'].astype(str)
trx['IBank_Trx_Code'] = trx['IBank_Trx_Code'].astype(int)
trx['IBank_Trx_Type'] = trx['IBank_Trx_Type'].astype(str)
trx['IBank_Trx_Amount'] = trx['IBank_Trx_Amount'].astype(int)
trx['IBank_Trx_Datetime'] = trx['IBank_Trx_Datetime'].astype(str)
trx['IBank_Account_Debit_BSI_ID_Receiver'] = trx['IBank_Account_Debit_BSI_ID_Receiver'].astype(str)

cust['Account_Credit_BSI'] = cust['Account_Credit_BSI'].astype(str)
cust['User_KTP_ID'] = cust['User_KTP_ID'].astype(str)

# 
#Replace all 0 with empty string
trx['ATM_Trx_ID'] = trx['ATM_Trx_ID'].astype(str).str.replace('^0$', '')
trx['ATM_Trx_Type'] = trx['ATM_Trx_Type'].astype(str).str.replace('^0$', '')
trx['ATM_Trx_Datetime'] = trx['ATM_Trx_Datetime'].astype(str).str.replace('^0$', '')
trx['ATM_Account_Debit_BSI_ID_Receiver'] = trx['ATM_Account_Debit_BSI_ID_Receiver'].astype(str).str.replace('^0.0$', '')
trx['ATM_Account_NonBSI_ID_Receiver'] = trx['ATM_Account_NonBSI_ID_Receiver'].astype(str).str.replace('^0$', '')

trx['Mobile_App_Trx_ID'] = trx['Mobile_App_Trx_ID'].astype(str).str.replace('^0$', '')
trx['Mobile_App_Trx_Type'] = trx['Mobile_App_Trx_Type'].astype(str).str.replace('^0$', '')
trx['Mobile_App_Trx_Datetime'] = trx['Mobile_App_Trx_Datetime'].astype(str).str.replace('^0$', '')
trx['Mobile_App_Account_Debit_BSI_ID_Receiver'] = trx['Mobile_App_Account_Debit_BSI_ID_Receiver'].astype(str).str.replace('^0.0$', '')
trx['Mobile_App_Account_NonBSI_ID_Receiver'] = trx['Mobile_App_Account_NonBSI_ID_Receiver'].astype(str).str.replace('^0$', '')

trx['IBank_Trx_ID'] = trx['IBank_Trx_ID'].astype(str).str.replace('^0$', '')
trx['IBank_Trx_Type'] = trx['IBank_Trx_Type'].astype(str).str.replace('^0$', '')
trx['IBank_Trx_Datetime'] = trx['IBank_Trx_Datetime'].astype(str).str.replace('^0$', '')
trx['IBank_Account_Debit_BSI_ID_Receiver'] = trx['IBank_Account_Debit_BSI_ID_Receiver'].astype(str).str.replace('^0.0$', '')
trx['IBank_Account_NonBSI_ID_Receiver'] = trx['Mobile_App_Account_NonBSI_ID_Receiver'].astype(str).str.replace('^0$', '')

# 
conn = tg.TigerGraphConnection(host="http://35.228.83.191")
conn.graphname = "GRAPH_PRACTICE2"

# 
# UPSERT VERTEX
## upsertVertexDataframe(df, vertexType, v_id=None, attributes=None)
### conn.upsertVertexDataframe(df=person, vertexType='person', v_id='name')
v_ATM_Trx = conn.upsertVertexDataFrame(trx, "V_ATM_Trx", "ATM_Trx_ID", attributes= {"ATM_Trx_ID": "ATM_Trx_ID", "ATM_Trx_Code":"ATM_Trx_Code","ATM_Trx_Type":"ATM_Trx_Type","ATM_Trx_Amount":"ATM_Trx_Amount","ATM_Trx_Datetime":"ATM_Trx_Datetime"})
print(str(v_ATM_Trx) + " V_ATM_Trx Upserted")
v_Mobile_App_Trx = conn.upsertVertexDataFrame(trx, "V_Mobile_App_Trx", "Mobile_App_Trx_ID", attributes= {"Mobile_App_Trx_ID": "Mobile_App_Trx_ID", "Mobile_App_Trx_Code":"Mobile_App_Trx_Code","Mobile_App_Trx_Type":"Mobile_App_Trx_Type","Mobile_App_Trx_Amount":"Mobile_App_Trx_Amount","Mobile_App_Trx_Datetime":"Mobile_App_Trx_Datetime"})
print(str(v_Mobile_App_Trx) + " V_Mobile_App_Trx Upserted")
v_IBank_Trx = conn.upsertVertexDataFrame(trx, "V_IBank_Trx", "IBank_Trx_ID", attributes= {"IBank_Trx_ID": "IBank_Trx_ID", "IBank_Trx_Code":"IBank_Trx_Code","IBank_Trx_Type":"IBank_Trx_Type","IBank_Trx_Amount":"IBank_Trx_Amount","IBank_Trx_Datetime":"IBank_Trx_Datetime"})
print(str(v_IBank_Trx) + " V_IBank_Trx Upserted")

v_Account_Debit_BSI = conn.upsertVertexDataFrame(trx, "V_Account_Debit_BSI", "Account_Debit_BSI_ID", attributes= {"Account_ID":"Account_Debit_BSI_ID"})
print(str(v_Account_Debit_BSI) + " V_Account_Debit_BSI Upserted")

## If your Dataframe has receiver account value use this
v_Account_Debit_BSI = conn.upsertVertexDataFrame(trx, "V_Account_Debit_BSI", "ATM_Account_Debit_BSI_ID_Receiver", attributes= {"Account_ID":"ATM_Account_Debit_BSI_ID_Receiver"})
print(str(v_Account_Debit_BSI) + " V_Account_Debit_BSI Upserted")
v_Account_Debit_BSI = conn.upsertVertexDataFrame(trx, "V_Account_Debit_BSI", "Mobile_App_Account_Debit_BSI_ID_Receiver", attributes= {"Account_ID":"Mobile_App_Account_Debit_BSI_ID_Receiver"})
print(str(v_Account_Debit_BSI) + " V_Account_Debit_BSI Upserted")
v_Account_Debit_BSI = conn.upsertVertexDataFrame(trx, "V_Account_Debit_BSI", "IBank_Account_Debit_BSI_ID_Receiver", attributes= {"Account_ID":"IBank_Account_Debit_BSI_ID_Receiver"})
print(str(v_Account_Debit_BSI) + " V_Account_Debit_BSI Upserted")

v_Account_NonBSI = conn.upsertVertexDataFrame(anb, "V_Account_NonBSI", "Account_NonBSI", attributes={"NonBSI_Account_ID":"Account_NonBSI", "NonBSI_Account_Bank_Name":"NonBSI_Account_Bank_Name"})
print(str(v_Account_NonBSI) + " V_Account_NonBSI Upserted")
v_Customer = conn.upsertVertexDataFrame(cust, "V_Customer", "Customer_ID", attributes={"Customer_ID":"Customer_ID", "User_Name":"User_Name", "User_Address":"User_Address", "User_Gender":"User_Gender", "User_BirthDate":"User_BirthDate", "User_KTP_ID":"User_KTP_ID"})
print(str(v_Customer) + " v_Customer Upserted")

# 
# UPSERT EDGE
## upsertEdgesDataframe(df, sourceVertexType, edgeType, targetVertexType, from_id=None, to_id=None, attributes=None)
e_ATM_Send = conn.upsertEdgeDataFrame (trx, "V_Account_Debit_BSI", "E_ATM_Send", "V_ATM_Trx", from_id="Account_Debit_BSI_ID", to_id="ATM_Trx_ID", attributes={})
print(str(e_ATM_Send) + " E_ATM_Send EDGES Upserted")
e_ATM_Receive = conn.upsertEdgeDataFrame (trx, "V_ATM_Trx", "E_ATM_Receive", "V_Account_Debit_BSI", from_id="ATM_Trx_ID", to_id="ATM_Account_Debit_BSI_ID_Receiver", attributes={})
print(str(e_ATM_Receive) + " E_ATM_Receive EDGES Upserted")
e_ATM_Receive_Account_NonBSI = conn.upsertEdgeDataFrame (trx, "V_ATM_Trx", "E_ATM_Receive_AccountNonBSI", "V_Account_NonBSI", from_id="ATM_Trx_ID", to_id="ATM_Account_NonBSI_ID_Receiver", attributes={})
print(str(e_ATM_Receive_Account_NonBSI) + " E_ATM_Receive_Account_NonBSI EDGES Upserted")
e_Use_Machine = conn.upsertEdgeDataFrame (trx, "V_ATM_Trx", "E_Use_Machine", "V_ATM_Machine", from_id="ATM_Trx_ID", to_id="ATM_Machine_ID", attributes={})
print(str(e_Use_Machine) + " E_Use_Machine EDGES Upserted")
e_Use_ATM_Card = conn.upsertEdgeDataFrame (trx, "V_ATM_Trx", "E_Use_ATM_Card", "V_ATM_Card_REF", from_id="ATM_Trx_ID", to_id="ATM_Card_ID", attributes={})
print(str(e_Use_ATM_Card) + " E_Use_ATM_Card EDGES Upserted")
e_Owns_ATM_Card = conn.upsertEdgeDataFrame (trx, "V_Account_Debit_BSI", "E_Owns_ATM_Card", "V_ATM_Card_REF", from_id="Account_Debit_BSI_ID", to_id="ATM_Card_ID", attributes={})
print(str(e_Owns_ATM_Card) + " E_Owns_ATM_Card")

e_Mobile_Send = conn.upsertEdgeDataFrame (trx, "V_Account_Debit_BSI", "E_Mobile_Send", "V_Mobile_App_Trx", from_id="Account_Debit_BSI_ID", to_id="Mobile_App_Trx_ID", attributes={})
print(str(e_Mobile_Send) + " E_Mobile_Send EDGES Upserted")
e_Mobile_Receive = conn.upsertEdgeDataFrame (trx, "V_Mobile_App_Trx", "E_Mobile_Receive", "V_Account_Debit_BSI", from_id="Mobile_App_Trx_ID", to_id="Mobile_App_Account_Debit_BSI_ID_Receiver", attributes={})
print(str(e_Mobile_Receive) + " E_Mobile_Receive EDGES Upserted")
e_Mobile_Receive_AccountNonBSI = conn.upsertEdgeDataFrame (trx, "V_Mobile_App_Trx", "E_Mobile_App_Receive_AccountNonBSI", "V_Account_NonBSI", from_id="Mobile_App_Trx_ID", to_id="Mobile_App_Account_NonBSI_ID_Receiver", attributes={})
print(str(e_Mobile_Receive_AccountNonBSI) + " E_Mobile_Receive_AccountNonBSI EDGES Upserted")
e_Mobile_Trx_Loc = conn.upsertEdgeDataFrame (trx, "V_Mobile_App_Trx", "E_Mobile_Trx_Loc", "V_Mobile_Trx_Location", from_id="Mobile_App_Trx_ID", to_id="Mobile_Location_ID", attributes={})
print(str(e_Mobile_Trx_Loc) + " E_Mobile_Trx_Loc EDGES Upserted")
e_Use_Mobile_App = conn.upsertEdgeDataFrame (trx, "V_Mobile_App_Trx", "E_Use_Mobile_App", "V_Mobile_App_REF", from_id="Mobile_App_Trx_ID", to_id="Mobile_App_ID", attributes={})
print(str(e_Use_Mobile_App) + " E_Use_Mobile_App EDGES Upserted")
e_Owns_Mobile_App = conn.upsertEdgeDataFrame (trx, "V_Account_Debit_BSI", "E_Owns_Mobile_App", "V_Mobile_App_REF", from_id="Account_Debit_BSI_ID", to_id="Mobile_App_ID", attributes={})
print(str(e_Owns_ATM_Card) + " E_Owns_Mobile_App EDGES Upserted")

e_IBank_Send = conn.upsertEdgeDataFrame (trx, "V_Account_Debit_BSI", "E_IBank_Send", "V_IBank_Trx", from_id="Account_Debit_BSI_ID", to_id="IBank_Trx_ID", attributes={})
print(str(e_IBank_Send) + " E_IBank_Send EDGES Upserted")
e_IBank_Receive = conn.upsertEdgeDataFrame (trx, "V_IBank_Trx", "E_IBank_Receive", "V_Account_Debit_BSI", from_id="IBank_Trx_ID", to_id="IBank_Account_Debit_BSI_ID_Receiver", attributes={})
print(str(e_IBank_Receive) + " E_IBank_Receive EDGES Upserted")
e_IBank_Receive_AccountNonBSI = conn.upsertEdgeDataFrame (trx, "V_IBank_Trx", "E_IBank_Receive_AccountNonBSI", "V_Account_NonBSI", from_id="IBank_Trx_ID", to_id="IBank_Account_NonBSI_ID_Receiver", attributes={})
print(str(e_IBank_Receive_AccountNonBSI) + " E_IBank_Receive_AccountNonBSI EDGES Upserted")
e_IBank_Trx_Loc = conn.upsertEdgeDataFrame (trx, "V_IBank_Trx", "E_IBank_Trx_Loc", "V_IBank_Trx_Location", from_id="IBank_Trx_ID", to_id="IBank_IP_Address", attributes={})
print(str(e_IBank_Trx_Loc) + " E_IBank_Trx_Loc EDGES Upserted")
e_Use_IBank = conn.upsertEdgeDataFrame (trx, "V_IBank_Trx", "E_Use_IBank", "V_IBank_REF", from_id="Mobile_App_Trx_ID", to_id="IBank_ID", attributes={})
print(str(e_Use_IBank) + " E_Use_IBank EDGES Upserted")
e_Owns_IBank = conn.upsertEdgeDataFrame (trx, "V_Account_Debit_BSI", "E_Owns_IBank", "V_IBank_REF", from_id="Account_Debit_BSI_ID", to_id="IBank_ID", attributes={})
print(str(e_Owns_IBank) + " E_Owns_IBank Upserted")

e_Has_Debit_Account = conn.upsertEdgeDataFrame (cust, "V_Customer", "E_Has_Debit_Account", "V_Account_Debit_BSI", from_id="Customer_ID", to_id="Account_Debit_BSI", attributes={})
print(str(e_Has_Debit_Account) + " E_Has_Debit_Account EDGES Upserted")

# 



