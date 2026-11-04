from datetime import datetime

with open("/home/Beksultan/lab7/log.txt", "a") as file:
    file.write("Script executed at: " + str(datetime.now()) + "\n")
