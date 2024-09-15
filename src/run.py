 #line-by-line explanation of the run.py script you provided


####this script sets up and serves a web application using the waitress server on a port defined by the environment (or 5000 by default).#####

import os    #This imports the os module, which allows interaction with the operating system. Here, it will be used to access environment variables, like the port number.
from prometheus_client import Counter, Summary, generate_latest
from flask import request
import time


from storage import app  #This imports the app object from a module  storage. The app is likely a Flask (or similar framework) instance, which defines the web application's behavior.
from waitress import serve #This imports serve from the waitress module, a production WSGI (Web Server Gateway Interface) server used to serve Python web applications.


# Create Prometheus metrics for counting and request duration
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests', ['method', 'endpoint', 'status_code'])
REQUEST_TIME = Summary('http_request_duration_seconds', 'Time spent processing request', ['method', 'endpoint', 'status_code'])
STATUS_CODES = Counter('http_status_codes_total', 'HTTP status codes', ['status_code'])

@app.before_request
def start_timer():
    request.start_time = time.time()

@app.after_request
def track_metrics(response):
    request_latency = time.time() - request.start_time
    REQUEST_TIME.labels(method=request.method, endpoint=request.path, status_code=response.status_code).observe(request_latency)
    REQUEST_COUNT.labels(method=request.method, endpoint=request.path, status_code=response.status_code).inc()
    STATUS_CODES.labels(status_code=response.status_code).inc()  # Track HTTP status codes
    return response

@app.route('/metrics')
def metrics():
    return generate_latest(), 200

if __name__ == "__main__":   #This checks if the script is being run directly (not imported as a module).
    port = os.getenv("PORT", default=5000)  #Retrieves the PORT environment variable, or defaults to 5000 if it is not set. This determines which port the web app will run on.
    serve(app, host="0.0.0.0", port=port)  #Starts the waitress server, hosting the app on all available IP addresses (0.0.0.0) and the specified port. This makes the application accessible over the network.

