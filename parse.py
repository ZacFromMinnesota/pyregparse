import re
import time

#edit the filepath then run it 
textfile = open('C:/Users/stopt/Desktop/Tech/Python/pyreg/log.txt', 'r')
filetext = textfile.read()
textfile.close()

time.sleep(1)

# This was my first attempt
port = re.findall('port [0-9]*', filetext)
clientport = re.findall('Client Port: [0-9]*', filetext)
s_port = re.findall('s_port:"(.*?)"', filetext)
print(f'\nHere are the ports from individual lines of regex for each port: port= {port} Client Port= {clientport} s_port= {s_port} \n')

time.sleep(1)

#could probably be cleaned up and restructured but here is one line of regex
#I didn't include port 80 under service:"80" because that info is duplicated by the service_id:"http" but I would just have to restructure the first section of regex to include it
oneline = re.findall('(?: Client Port|[a-z]\wport|port|Port)(?:.{1,3})[0-9]*.', filetext)
print(f'Here are all the ports from oneline of regex: {oneline} \n')

input('press enter to exit')


