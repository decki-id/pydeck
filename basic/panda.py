import pandas as pd
import os
import json
from pandas.io.json import json_normalize


# def panda(results):
# PANDAS DATAFRAME PostgreSQL
# df = {
#     "Sale Quantity": [results[0][0], results[1][0], results[2][0], results[3][0]],
#     "Sale Value": [results[0][1], results[1][1], results[2][1], results[3][1]],
#     "Inventory Quantity": [
#         results[0][2],
#         results[1][2],
#         results[2][2],
#         results[3][2],
#     ],
#     "Inventory Value": [results[0][3], results[1][3], results[2][3], results[3][3]],
# }
# show = pd.DataFrame(df, index=["Quarter1", "Quarter2", "Quarter3", "Quarter4"])

# PANDAS DATAFRAME SQL Server 2000
# df = {
#     "No. Trans": [results[0][0], results[1][0], results[2][0], results[3][0]],
#     "Date Trans": [results[0][1], results[1][1], results[2][1], results[3][1]],
#     "Type Trans": [
#         results[0][2],
#         results[1][2],
#         results[2][2],
#         results[3][2],
#     ],
#     "Notes": [results[0][3], results[1][3], results[2][3], results[3][3]],
#     "User ID": [results[0][4], results[1][4], results[2][4], results[3][4]],
# }
# pd.set_option("display.max_colwidth", None)
# show = pd.DataFrame(df)
# return show

# PANDAS SERIES
# series = {
#     "Sale Quantity": results[0][0],
#     "Sale Value": results[0][1],
#     "Inventory Quantity": results[0][2],
#     "Inventory Value": results[0][3],
# }
# show = pd.Series(series)
# print(show)

# READ CSV
# csv = pd.read_csv(
#     os.path.join(
#         os.path.dirname(__file__),
#         "D:/Projects/TRAVICS STARCROSS/#Docs/StarcrossBangka_tColour.csv",
#     ),
#     names=["Old Rows", "Content", "New Rows"],
#     sep=";",
#     header=None,
# )
# pd.set_option("display.max_rows", None)
# print(csv)
# print(csv.to_string())
# print(csv.head())
# print(csv.tail())
# print(csv.info())

# READ JSON CONDITIONAL (CONVERT THE FILE TO DICT FIRST)
# os.chdir("D:/Projects/Raven3/raven3-shop-master")
# with open("config.rvt") as json_data:
#     data = json.load(json_data)
# json = pd.Series(data)
# print(json)