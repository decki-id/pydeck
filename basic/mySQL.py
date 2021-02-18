import mysql.connector


# CONNECT TO MYSQL
mydb = mysql.connector.connect(
    host="127.0.0.1", user="root", password="", database="db-lastproject"
)
# print(mydb)


mycursor = mydb.cursor()


# CREATE DATABASE
# mycursor.execute("CREATE DATABASE pydeck")


# SHOW ALL DATABASES
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#     print(x)


# CREATE TABLE
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")


# SHOW ALL TABLES
# mycursor.execute("SHOW TABLES")
# for y in mycursor:
#     print(y)


# ADD/MODIFY COLUMN IN TABLE
# mycursor.execute("ALTER TABLE customers MODIFY COLUMN id INT NOT NULL AUTO_INCREMENT")


# ADD PRIMARY KEY/CONSTRAINT TO TABLE
# mycursor.execute("ALTER TABLE customers ADD PRIMARY KEY (id)")


# DROP TABLE
# mycursor.execute("DROP TABLE customers")


# INSERT 1 DATA TO DATABASE
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# value = ("Dinda Aulia", "Bogor")
# mycursor.execute(sql, value)
# mydb.commit()
# print(mycursor.lastrowid, "is inserted successfully.")


# INSERT MULTIPLE DATA TO DATABASE
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# value = [
#     ("Choerul Sofyan Muhammad Falih", "Buah Batu"),
#     ("Tio Dinar", "Rancaekek"),
#     ("Jaka Panduga Rusmana", "Cimahi"),
# ]
# mycursor.executemany(sql, value)
# mydb.commit()
# print(mycursor.rowcount, "are inserted successfully.")


# UPDATE DATA IN TABLE
# mycursor.execute("UPDATE customers SET id = 1 WHERE name = 'Decki Herdiawan Soepandi'")
# mydb.commit()
# print(mycursor.rowcount, "record(s) affected.")


# SELECT DATA FROM TABLE
# mycursor.execute("SELECT * FROM tickets")
# myresult = mycursor.fetchall()
# for z in myresult:
#     print(z)