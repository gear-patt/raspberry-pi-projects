import http.client

conn = http.client.HTTPConnection("www.uci.edu")
conn.request("GET", "/")
r = conn.getresponse()
print(r.status, r.reason)
data = r.read()
print(data)
conn.close()