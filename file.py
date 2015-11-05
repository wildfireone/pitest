import datetime
import time

fh = open ("mytimelog.txt", "w")
fh.write(str(datetime.datetime.now()))
fh.close()

time.sleep(10)

fh = open("mytimelog.txt" , "a")
fh.write(str(datetime.datetime.now()))
fh.close()

        

