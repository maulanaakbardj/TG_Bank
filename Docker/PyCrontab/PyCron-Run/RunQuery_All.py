import pyTigerGraph as tg 
from datetime import datetime
import pytz

conn = tg.TigerGraphConnection(host="http://172.16.2.79")
conn.graphname = "Graph_Practice_New"
Result_uc4 = conn.runInstalledQuery("UC04_QRY01_Multichannel1")
runquery_uc9 = conn.runInstalledQuery("UC9_QRY01_Multichannel3")
runquery1_uc6 = conn.runInstalledQuery("UC6_QRY01_TransactionsMoreThan100Million")
runquery2_uc6 = conn.runInstalledQuery("UC6_QRY02_TransactionsOutsideOperationalHours")




current_dateTime = datetime.now(pytz.timezone('Asia/Jakarta'))
print("Running Query (Datetime) : " + str(current_dateTime))
