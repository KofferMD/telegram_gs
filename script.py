import mysql.connector

db = mysql.connector.connect(
    user='root',
    password='root',
    port='8889',
    database='work'
)

print(db)



# db = mysql.connector.connect(
#     user='root',
#     password='root',
#     port='8899',
#     database='work'
# )

