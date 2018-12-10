import datetime
file_name = datetime.datetime.now().strftime('mylogfile_%H_%M_%d_%m_%Y.log')
file1 = open(file_name,'w')
file1.write("hello world")
file1.close()
