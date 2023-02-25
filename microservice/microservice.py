import time
from json2html import *

print("Listening for requests ...")

while True:
    time.sleep(1)

    try:
        with open("data/request.txt", "r") as f:
            line = f.readline()
    except FileNotFoundError:
        continue

    if line == "request":

        print("Request received ...")
        with open("data/request.txt", "w") as f:
            f.write("received")

        with open("data/books.json") as f:
            d = f.read()
            scanOutput = json2html.convert(json=d)

        with open("data/response.html", "w") as htmlFile:
            htmlFile.write(str(scanOutput))

        print("Json file is converted into html successfully")

    elif line == "exit":
        with open("data/request.txt", "w") as f:
            f.write("")
        print("Shutting down ...")
        exit()