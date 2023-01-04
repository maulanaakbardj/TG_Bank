import pyTigerGraph as tg 
conn = tg.TigerGraphConnection(host="http://localhost")
conn.graphname = "Graph_Practice_New"
runquery = conn.runInstalledQuery("UC9_2Vertex")
parsR = (runquery)
print(parsR)
