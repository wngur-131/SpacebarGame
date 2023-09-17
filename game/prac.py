import pymysql

db = pymysql.connect(
    host = "127.0.0.1",
    user = "root",
    password = "code.wngur131",
    db = "info",
    charset = "utf8mb4"
)
cursor = db.cursor()

# cursor.execute(
#     """CREATE TABLE info (
#         id int(10) AUTO_INCREMENT PRIMARY KEY,
#         class varchar(5),
#         name varchar(10),
#         score int(10) DEFAULT 0 
#         )"""
# )

# SQL = "INSERT INTO info (class, name, score) VALUES (%s, %s, %s)"
# cursor.execute(SQL, ("10309", "문주혁", 45))

SQL = "SELECT * FROM info"
cursor.execute(SQL)

res = cursor.fetchall()

for data in res:
    print(data[3])

db.commit()
db.close()