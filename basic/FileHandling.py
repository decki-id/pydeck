import json
import os


# READ FILE.
# file = open("coba.json")
# print(file.read())


# APPEND/EDIT FILE.
# file = open("test.txt", "w")
# file.write("This is text from Python.\nThis is another text.\nThis is another fuckin' text.\nThis is another motherfuckin' goddamn text.")
# file.close()
# file = open("test.txt", "r")
# print(file.read())


# WRITE NEW FILE OR OVERWRITE THE EXISTING ONE.
# x = [
#     {
#         "Name": "Decki Herdiawan Soepandi",
#         "Age": 27,
#         "Address": "Padalarang",
#         "Single": True,
#     },
#     {"Name": "Sutriyanto", "Age": 32, "Address": "Yogyakarta", "Single": False},
# ]
# file = open("anotherFile.json", "w")
# file.write(json.dumps(x, indent=4))
# file.close()
# file = open("anotherFile.json")
# print(file.read())


# DELETE FILE.
# os.remove("anotherfile.json")


# DELETE FOLDER.
# os.rmdir("folderName")