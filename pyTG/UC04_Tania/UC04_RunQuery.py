# 
import pyTigerGraph as tg

# 
conn = tg.TigerGraphConnection(host="http://35.228.83.191", username="tigergraph", password="tigergraph")
conn.graphname = "GRAPH_PRACTICE2"
Result = conn.runInstalledQuery("UC04_QRY01_Multichannel1")




