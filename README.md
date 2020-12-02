# What is it ?

  

This code obtains daily data by comparing the daily statistics data of the videos. After obtaining the data, it adds the data to the table named 'gunluk'.

![enter image description here](https://github.com/MrSipahi/Youtube_daily_data/blob/main/photo/daily.PNG?raw=true)

# How does it work


For this code to work, there must be a table named 'data' in the database. It takes statistical data from this table.

![enter image description here](https://github.com/MrSipahi/Youtube_daily_data/blob/main/photo/data.PNG?raw=true)

  
The code compares the day it was found and the previous day.

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

 

