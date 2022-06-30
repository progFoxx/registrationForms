#!/usr/bin/env python3
import cgi
import random
import time
from sqlite3Work import *


form = cgi.FieldStorage()
text1 = form.getfirst("TEXT_1", "не задано")
text2 = form.getfirst("TEXT_2", "не задано")
idf = random.randint(0,99999999)


clientInfo = (idf,text1,text2,"11^23")

cur.execute("INSERT INTO Clients VALUES(?, ?, ?, ?);",clientInfo)
conn.commit()


print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработка данных форм</title>
        </head>
        <body>""")

print("<h1>Обработка данных форм!</h1>")
print("<p>Id: {}</p>".format(idf))
print("<p>имя: {}</p>".format(text1))
print("<p>фамилия: {}</p>".format(text2))
print("""</body>
        </html>""")