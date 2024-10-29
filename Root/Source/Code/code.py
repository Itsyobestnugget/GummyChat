
import os
import google.generativeai as genai
import libsql_experimental as libsql

#Setting apikey and configuring
url = 'libsql://smiley-itsyobestnugget.turso.io'
auth_token = 'eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJhIjoicnciLCJpYXQiOjE3Mjg1ODA5ODQsImlkIjoiZTU1OGM0ZjQtOTc0YS00MzIzLWIzOGMtMzFhODU0Mzc2YWNlIn0.-mc2F574pt3LESYe4quTez0qGUtorNvfiANc2sMx_kHj9K3XBJx28mj80Sh-5hqAPNdCe2jPZvxml3EZoCjKBg'

conn = libsql.connect("hello.db", sync_url=url, auth_token=auth_token)
conn.sync()
conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER);")
conn.execute("INSERT INTO users(id) VALUES (1);")
conn.commit()

print(conn.execute("select * from users").fetchall())