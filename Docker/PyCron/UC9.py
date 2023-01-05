import pyTigerGraph as tg
import pytz
from datetime import datetime

now = datetime.now()
localtz = pytz.timezone('Asia/Jakarta')
date_aware_la = localtz.localize(now).strftime("%Y-%m-%d %H:%M:%S")

conn = tg.TigerGraphConnection(host="http://192.168.100.8") # Maul Ip
conn.graphname = "Graph_Practice_New"
runquery = conn.runInstalledQuery("UC9_2Vertex")

print("successful date:", date_aware_la)
