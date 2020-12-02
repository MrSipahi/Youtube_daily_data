# What is it ?

  

This program, compare daily static datas and take result for the daily data. Than program will add in the named table 'gunluk'

![enter image description here](https://github.com/MrSipahi/Youtube_daily_data/blob/main/photo/daily.PNG?raw=true)

# How does it work

If you will use this program, there must be a table named 'data' because this program must take statistics data so, you must add 'data'

![enter image description here](https://github.com/MrSipahi/Youtube_daily_data/blob/main/photo/data.PNG?raw=true)

  
This program compore today and yesterday.

    locale.setlocale(locale.LC_ALL,  "")
    moment = datetime.now()    
    tarih = moment.strftime("%Y-%m-%d")
    yesterday = datetime.today()  -  timedelta(days=1)
    dun = yesterday.strftime("%Y-%m-%d")

SQL Query:

    query=f"SELECT * FROM data where videoID= '{x}' AND (tarih='{dun}' OR tarih='{tarih}') ORDER BY tarih"

    cursor.execute(query)

#  Technologies

 - [Mysql](https://www.mysql.com/)
 - [Python](https://www.python.org/)
 - [Pandas](https://pypi.org/project/pandas/)

 

