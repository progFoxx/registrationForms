#!/usr/bin/env python3
import cgi
import html
import pymysql

form = cgi.FieldStorage()
фамилия = form.getfirst("TEXT_1", "не задано")
имя = form.getfirst("TEXT_2", "не задано")
фамилия = html.escape(фамилия)
имя = html.escape(имя)
run = True
r = 0
while run == True:
    r += 1

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработка данных форм</title>
        </head>
        <body>""")

print("<h1>Обработка данных форм!</h1>")
print("<p>фамилия: {}</p>".format(фамилия))
print("<p>имя: {}</p>".format(имя))

print("""</body>
        </html>""")

