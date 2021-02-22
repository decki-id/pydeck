import pyodbc
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, select, MetaData, Table, and_, text, update

# from panda import panda

app = Flask(__name__)
postgres = create_engine("postgresql://revota:r3vot4@localhost:5432/revota")
mssql = create_engine("mssql+pyodbc://revota:r3vot4@DBBLOODS-SHOP_v47")
app.config["SQLALCHEMY_DATABASE_URI"] = mssql
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
metadata = MetaData(bind=None)
db = SQLAlchemy(app)

# for driver in pyodbc.drivers():
#     print(driver)

# SET CLASS FOR CREATING NEW TABLE
# class dataTemp(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)

#     def __repr__(self):
#         return f"('{self.id}', '{self.username}', '{self.email}')"

# CREATE TABLE
# db.create_all()

# INSERT INTO TABLE
# admin = revotaUser(username="admin", email="admin@example.com")
# guest = revotaUser(username="guest", email="guest@example.com")
# db.session.add(admin)
# db.session.add(guest)
# db.session.commit()

# SELECT ALL FROM TABLE
# users = revotaUser.query.all()
# for u in users:
#     print(u)

# UPDATE EXISTING TABLE (PostgreSQL)
# table = Table("datatemp", metadata, autoload=True, autoload_with=postgres)
# statement = (
#     update(table).where(table.columns.saleqty == 75).values(salevalue="200000000")
# )
# connection = postgres.connect()
# connection.execute(statement)

# SELECT EXISTING TABLE (PostgreSQL)
# table = Table("datatemp", metadata, autoload=True, autoload_with=postgres)
# statement = select(
#     [
#         table.columns.saleqty,
#         table.columns.salevalue,
#         table.columns.inventoryqty,
#         table.columns.inventoryvalue,
#     ]
# )
# connection = postgres.connect()
# results = connection.execute(statement).fetchall()
# data = panda(results)
# print(results)

# SELECT EXISTING TABLE (SQL Server 2000)
# statement = "SELECT * FROM tCashier"
# connection = mssql.connect()
# results = connection.execute(statement).fetchall()
# data = panda(results)
# print(results)

# DROP TABLE
# revotaUser.__table__.drop(postgres)