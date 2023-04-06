import os
import requests
from flask import Flask, request, Response

app = Flask(__name__)

apikey = os.environ['APILAYER_KEY']


@app.route('/')
def index():
  return 'Hello from Flask!'


@app.route('/whois/<string:domain>')
def whois(domain):
  url = f'https://api.apilayer.com/whois/query?domain={domain}'
  headers = {'apikey': apikey}

  try:
    response = requests.get(url, headers=headers)
  except requests.exceptions.RequestException as e:
      return Response(f"error: {str(e)}", status=500)

  status_code = response.status_code
  result = response.text

  return Response(result, status=status_code, mimetype="application/json")


@app.route('/dns/<string:record>/<string:domain>')
def dns(record, domain):
  url = f'https://api.apilayer.com/dns_lookup/api/{record}/{domain}'
  headers = {'apikey': apikey}

  try:
    response = requests.get(url, headers=headers)
  except requests.exceptions.RequestException as e:
      return Response(f"error: {str(e)}", status=500)

  status_code = response.status_code
  result = response.text

  return Response(result, status=status_code, mimetype="application/json")


@app.route("/.well-known/ai-plugin.json")
def plugin_manifest():
  host = request.headers['Host']
  with open("ai-plugin.json") as f:
    text = f.read()
    text = text.replace("PLUGIN_HOSTNAME", f"https://{host}")
    return Response(text, mimetype="text/json")


@app.route("/openapi.yaml")
def openapi_spec():
  host = request.headers['Host']
  with open("openapi.yaml") as f:
    text = f.read()
    text = text.replace("PLUGIN_HOSTNAME", f"https://{host}")
    return Response(text, mimetype="text/yaml")


app.run(host='0.0.0.0', port=5000)
