import MySQLdb


db = MySQLdb.connect(host="35.161.154.86",
			user="root",
			passwd="dong8036",
			db="maestro_basic")	

cur = db.cursor()

cur.execute("SELECT * FROM SCHOOL")

for row in cur.fetchall():
	print row[0]
	print row[1]

db.close()

