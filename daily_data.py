
import pymysql as MySQLdb
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import locale
import time



db = MySQLdb.connect("ip","user","password","db_names" )
cursor = db.cursor()

query="SELECT * FROM kanal"
cursor.execute(query)

kanallar = cursor.fetchall()

kanal_list=[]
for i in kanallar:
    kanal_list.append(i[0])



locale.setlocale(locale.LC_ALL, "")
moment = datetime.now()
tarih = moment.strftime("%Y-%m-%d")
yesterday = datetime.today() - timedelta(days=1)
dun = yesterday.strftime("%Y-%m-%d")



for i in kanal_list:

    videolar=[]
    query=f"SELECT videoID FROM data where kanal_ID= '{i}' ORDER BY tarih"
    df = pd.read_sql(query, con=db)
    videolar = df["videoID"].unique()  
    '''
    cursor.execute(query)
    for j in cursor.fetchall():
        videolar.append(j[0])
    '''
    print(len(videolar))

    sayac = 0
    for x in videolar:
        sayac =sayac+ 1
        video_izlenme=[]
        video_begenme=[]
        video_begenmeme=[]
        video_yorum=[]
        video_tarih=[]

        query=f"SELECT * FROM data where videoID= '{x}' AND (tarih='{dun}' OR tarih='{tarih}')  ORDER BY tarih"
        cursor.execute(query)
        for j in cursor.fetchall():

            video_izlenme.append(j[3])
            video_begenme.append(j[4])
            video_begenmeme.append(j[5])
            video_yorum.append(j[6])
            video_tarih.append(j[9])

        


        for j in range(1,len(video_yorum)):
            a2 = video_izlenme[j]
            b2 = video_izlenme[j-1]
            izlenme= a2-b2

            a2 = video_begenme[j]
            b2 = video_begenme[j-1]
            begenme = a2-b2

            a2 = video_begenmeme[j]
            b2 = video_begenmeme[j-1]
            begenmeme = a2-b2

            a2 = video_yorum[j]
            b2 = video_yorum[j-1]
            yorum = a2-b2

            query = f"insert into gunluk(data_videoID,kanal_ID,goruntulenme,begenme,begenmeme,yorum,tarih) values ('{x}','{i}',{izlenme},{begenme},{begenmeme},{yorum},'{video_tarih[j]}')"
            cursor.execute(query)

            print(x)
        db.commit()
            
cursor.close()

db.close()