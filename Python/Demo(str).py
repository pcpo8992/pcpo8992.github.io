import urllib.request
import gzip
import json
import sqlite3 as sqlcon

url = "http://data.taipei/youbike"
a = urllib.request.urlretrieve(url)
f = gzip.open(a[0], mode="rt", encoding="utf-8")
jdata = f.read()
f.close()
data = json.loads(jdata, encoding="utf-8")

listStation = []


for key, value in data["retVal"].items():
    sno = value["sno"]
    sna = value["sna"]
    tot = int(value["tot"])
    sbi = int(value["sbi"])
    bemp = int(value["bemp"])
    listStation.append((sno, sna, tot, sbi, bemp))


conn = sqlcon.connect(":memory:")

sql = conn.cursor()

sql.execute("""create table Station (
               sno text,
               sna text,
               tot real,
               sbi real,
               bemp real) """)

sql.executemany("insert into Station values (?, ?, ?, ?, ?)", listStation)

conn.commit()

print("success")

sqlcommand = sql.execute("select * from Station where tot > '100' order by sbi desc")

sqlData = sqlcommand.fetchall()

print("%2s %5s %3s %3s %3s"%("代碼", "車站", "總位數", "空位數", "可還數"))
for data in sqlData:
    for i in range(len(data)):
        print("%2s "%(data[i]), end="")
conn.close()



