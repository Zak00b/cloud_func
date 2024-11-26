import json
from flask import Response
import functions_framework



@functions_framework.http
def main(request):
    request_json = request.get_json()

    # Retrieve sessionInfo, or initialize it if not present
    txt = request_json.get("name", {})

    return Response(json.dumps(txt), 200, mimetype="application/json")
