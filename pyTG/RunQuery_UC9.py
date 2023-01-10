import pyTigerGraph as tg 
from datetime import datetime
import pytz
conn = tg.TigerGraphConnection(host="http://172.16.11.223")
conn.graphname = "Team_Grafana"
runquery = conn.runInstalledQuery("UC9_QRY01_Multichannel3")
current_dateTime = datetime.now(pytz.timezone('Asia/Jakarta'))
print("Running Query (Datetime) : " + str(current_dateTime))
