import os
import sys
import json

path = sys.argv[1] # get name of file with redirected sites

oldtime = os.path.getmtime(path) # memorize the date of the file was modified

with open(path, encoding='utf-8') as data_file:
    data = json.loads(data_file.read()) # open the file with redirected sites

request = sys.stdin.readline() # get data from squid

while request:
    [ch_id, url, ip, fqdn, ident, method, urlgroup] = request.split()

    if os.path.getmtime(path) > oldtime:
        with open(path, encoding='utf-8') as data_file:
            data = json.loads(data_file.read())  # check if the file was modified, reload it

    answer = '' # variable for redirected url
    for key in data['urls']:
        if key in url: # check url in file with redirected sites
            answer = data['urls'][key] # get redirected url     
        if answer:
                response = ch_id + ' OK rewrite-url=http://' + answer + ip + fqdn + ident + method + urlgroup # create a response for squid
                answer = '' # clean redirected url
        else:
                response = ' OK'

    sys.stdout.write(response)
    sys.stdout.flush() # send response to squid

    request = sys.stdin.readline() # get new data from squid
