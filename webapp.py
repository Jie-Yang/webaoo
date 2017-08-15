from flask import Flask
from healthcheck import HealthCheck
from datetime import datetime
import socket, sys, math

app = Flask(__name__)
app.debug = True

health = HealthCheck(app, "/health")

@app.route("/")
def hello():
    hostName = socket.gethostname()
    bgColor = hostName2ColorHex(hostName)
    fontColor = calContrastColor(bgColor)
    css = """<head><style>
             body{
                 background-color: #"""+hex2Str(bgColor)+""";
                 }
             h1,h2 {
                 color: #"""+fontColor+""";
                 position: relative;
                 top: 40%;
                 text-align: center;
                 }
             </style></head>"""
    return css+'<body><h1>'+hostName+'</h1><h2>'+str(datetime.now())+'</h2></body>'

maxInt2ColorRatio = math.pow(16,6)/(2*sys.maxint-1)
def hostName2ColorHex(hostName):
    hashcode = hash(hostName)
    color = hashcode
    colorDEC = (color+sys.maxint-1)*maxInt2ColorRatio
    colorDECInt = int(colorDEC)
    colorHex = hex(colorDECInt)
    return colorHex

contractThreshold = hex(0xffffff/2)
def calContrastColor(colorHex):
    return '000000' if colorHex > contractThreshold else 'ffffff'

def hex2Str(colorHex):
    colorStr= str(colorHex)[2:]
    while len(colorStr)<6:
        colorStr='0'+colorStr
    if len(colorStr)>6:
        colorStr=colorStr[0:6]
        
    return colorStr

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
