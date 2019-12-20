import pymysql
import django

print(django.get_version())
print("Content-Type: text/html\n")
print("<html><head><title>products</title></head>")
print("<body>")
print("<h1>products</h1>")
print("<ul>")

connection = pymysql.connect(user='root', passwd='root', db='examxx')
cursor = connection.cursor()
cursor.execute("SELECT username FROM et_user")

for row in cursor.fetchall():
    print("<li>%s</li>" % row[0])

print("</ul>")
print("</body></html>")

connection.close()