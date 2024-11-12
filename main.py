import json
from flask import Response
import functions_framework



@functions_framework.http
def main():
    return Response(json.dumps("Hello World"), 200, mimetype="application/json")
