from flask import Flask
from datetime import datetime
import socket, sys, math

app = Flask(__name__)
app.debug = True
@app.route("/")
def hello():
    hostName = socket.gethostname()
    bgColor = hostName2ColorHex(hostName)
    fontColor = calContrastColor(bgColor)
    css = """<head><style>
             body{
                 background-color: #"""+str(bgColor)[2:]+""";
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

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
