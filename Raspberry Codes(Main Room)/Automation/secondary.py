from flask import Flask, request
import string
import requests


#defines the number of relay pins
relay_1=14
relay_2=18

app = Flask(__name__)
    
#syntax to create a flask listner server
 
@app.route('/', methods = ["POST"])
def post():
    c=request.data.decode()
    print(c)
    if(c=='d1_on'):
        requests.get('http://192.168.1.17/d1=on')
    elif(c=='d1_off'):
        requests.get('http://192.168.1.17/d1=off')
    elif(c=='d2_on'):
        requests.get('http://192.168.1.17/d2=on')
    elif(c=='d2_off'):
        requests.get('http://192.168.1.17/d2=off')
    elif(c=='r_on'):
        requests.get('http://192.168.1.17/LED=ON')
    elif(c=='r_off'):
        requests.get('http://192.168.1.17/LED=OFF')
    elif(c=='r_med'):
        requests.get('http://192.168.1.17/LED=MEDIUM')
    elif(c=='r_med'):
        requests.get('http://192.168.1.17/LED=LOW')
    return ''
 
app.run(host='0.0.0.0', port= 37340)