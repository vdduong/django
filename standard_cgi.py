#!/usr/bin/python

import MySQLdb

print "Content-Type: text/html"
print
print "<html><head><title>Livres</title></head>"
print "<body>"
print "<h1>Livres</h1>"
print "<ul>"

connection = MySQLdb.connect(user='moi', passwd='laissezmoientrer',db='ma_base')
cursor = connection.cursor()
cursor.execute("SELECT nom FROM livres ORDER BY pub_name DESC LIMIT 10")
for row in cursor.fetchall():
  print "<li>%s</li>"% row[0]

print "</ul>"
print "</body></html>"

connection.close()
