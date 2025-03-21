
from flask import Request

def http_hello_world(request: Request):
    """HTTP Function that responds with a greeting."""
    request_json = request.get_json(silent=True)
    name = request_json.get('name', 'World') if request_json else 'World'
    
    return f"Hello, {name} from Cloud Functions!", 200

