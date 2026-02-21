import json
from server import handle_request

def send_request(function_name: str, payload: dict):

    request = json.dumps({
        "function": function_name,
        "payload": payload
    })

    response = handle_request(request)

    return json.loads(response)