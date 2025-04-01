import os
import logging
from flask import Flask, request, Response
import requests
import http.client as http_client


http_client.HTTPConnection.debuglevel = 1

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True


def printHeader(request):
  print("================ Headers ================")
  for key, value in request.headers.items():
    print(f"{key}: {value}")
  print("================ END ================")
    
@app.route('/', methods=['GET'])
def get():
  printHeader(request)
  # Return the response from the target server
  return Response("", status=200, content_type="text/plain")


@app.route('/other', methods=['GET'])
def getOther():
  printHeader(request)
  # Return the response from the target server
  return Response("", status=200, content_type="text/plain")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8282)
