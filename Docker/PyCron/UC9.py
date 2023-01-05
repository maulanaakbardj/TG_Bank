import pyTigerGraph as tg 
from datetime import datetime
import pytz
conn = tg.TigerGraphConnection(host="http://192.168.100.8")
conn.graphname = "Graph_Practice_New"
runquery = conn.runInstalledQuery("UC9_2Vertex")
parsR = (runquery)
current_dateTime = datetime.now(pytz.timezone('Asia/Jakarta'))
print(current_dateTime)
