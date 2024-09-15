## SRE-Instrumentation

This project involves adding Prometheus instrumentation to an in-memory Storage API written in Python.

### Goal

The goal is to integrate Prometheus metrics into the Storage API and visualize them using Grafana. **Storage API** this service implements a simple in-memory Storage API for putting, getting, and deleting binary data. 

---

## Steps Taken to run and Test the app localy

**1. Clone the Repository**

Clone the repository to your local machine to explore and make changes:

```bash
git clone repository
cd PAth of repository
```



**2. Understand the Requirements**

Review the README and challenge instructions to understand the required instrumentation, the monitoring tools used, and the expected outcomes. The objective is to add Prometheus instrumentation to the Python-based in-memory Storage API.
Reviewed the code line by line and added comment expalining what each line does in the associated code files


**3. Set Up the Environment locally first to test it running:** 

Follow the steps outlined in `src/README.md`for setup details.

I run the following commands in MacOS



**Install Dependencies**


 ```bash
   make prod  or pip3 install -e . 
```
 Explanation: pip3 install -e . installs the package in editable mode, allowing code modifications without reinstalling the package. This is useful for development as it creates a symbolic link between the local code and the installed package.


* Run the Service

Execute make run or python3 run.py:

```bash
make run or
python3 run.py
```
Explanation: This command sets up and serves the web application using the Waitress server on the specified port (default 5000). Waitress is a production-quality WSGI server for Python web applications, handling multiple requests efficiently.


**Development Setup**

Install Development Dependencies

Run make dev or pip3 install -e .[dev]:

```bash

make dev or pip3 install -e .[dev]
```

Explanation: The -e flag installs the package in editable mode, and [dev] installs additional development dependencies such as linters and testing frameworks.

**Run Tests**

To run tests, use:


```bash make test or pytest storage/test.py ```

If encountering errors with pytest not found, do the following:

Troubleshooting:
- Ensure pytest is installed (pip show pytest).
- Check your PATH to ensure pytest is accessible.
- Use the full path to pytest if needed. 
```bash 
python3 -m pytest storage/test.py
```

**Run the Service with Hot Reloading**

If hupper is not found, ensure it is installed and in your PATH. To run the service with hot reloading:

```bash hupper -m waitress --port 5000 storage:app ```

Explanation: hupper enables hot reloading of Python applications.
-m specifies the module to run.
waitress is the WSGI server hosting your application.
--port 5000 sets the port for the server.
storage:app specifies the WSGI application callable.


---

## Create a Dockerfile for the Storage API:

**1. Add Prometheus Metrics Endpoint**

Use the `prometheus_client` library to expose metrics and add a `/metrics` endpoint to the Storage API. Add the Prometheus metrics section to `src/run.py`.


**2. Create Dockerfile**

Write a Dockerfile to package the Storage API and ensure it runs on `http://storage_api:5000`

**3. Update Docker-Compose**

Modify docker-compose.yml to include the Storage API and link it to the Prometheus container `(check code in docker-compose.yml)`.

Run: ```bash docker-compose up ```

This command starts Prometheus, Grafana, and the Storage API. Verify endpoints:

* Prometheus: `http://localhost:9090`
* Grafana: `http://localhost:3000`
* Storage API: `http://localhost:5000`

**4. Verify Metrics Endpoint**

Check Prometheus metrics at `http://localhost:5000/metrics`

Use `scripts/generate_traffic.sh` to generate traffic if needed.

---
 ## Visualize Metrics in Grafana


**1. Log in to Grafana**

Access Grafana at `http://localhost:3000` and log in with default credentials (admin/admin). Change the password upon first login.


**2. Add Prometheus as a Data Source**

* Go to Configuration -> Data Sources.
* Add Prometheus with the URL `http://localhost:9090`.

**3. Create Grafana Dashboard**


**Create a new dashboard:**

Click **Create** -> **Dashboard**.
Add a new **Time Series panel** with below query.

**Graph 1: Average HTTP Request Duration**
* Add a graph panel.
* Query: avg(http_request_duration_seconds_count{})
* Legend: "Average Request Duration".


**Add another new Time Series panel**

**Graph 2: HTTP Status Codes**
* Add another graph panel.
* Query: sum by (status_code) (rate(http_requests_total[5m]))
* Legend: "HTTP Status Codes".


**Save Dashboard**
* Click Save and give the dashboard a name. Below are screenshots of the graph metrics I created:


![This is an alt text.](/image/1.png "This is a sample image.")




 ---

 ## Try to figure out why you see HTTP 500 errors for some endpoints:


**Summary**

* Confirm Metric Reporting: Ensure HTTP 500 errors are being reported and collected by Prometheus.
* Examine Logs: Check application logs for error details.
* Review Configurations: Verify that all configurations are correct and that resources are sufficient.
* Review Changes: Look at recent code or configuration changes.
* Test and Debug: Reproduce and debug the issue in a controlled environment.
* Consult Documentation: Look for known issues or solutions in relevant documentation.


* when tried to run docker compose , the storage_api app got some warning as following:

 ```bash
storage_api-1  | WARNING:waitress.queue:Task queue depth is 2
storage_api-1  | WARNING:waitress.queue:Task queue depth is 1

```

**Addressing Waitress Queue Depth Warnings**

* indicate a low task queue depth. This could impact performance and cause HTTP 500 errors. Consider increasing the queue depth or number of threads, optimizing code, and monitoring performance.


* Understanding Task Queue Depth

- Task Queue Depth: This refers to the number of tasks (or requests) that can be queued up for processing by Waitress. A higher depth means that more requests can be queued and processed concurrently.

- Warnings:
        Depth of 1: Indicates that the task queue is set to a depth of 1, meaning only one request can be queued at a time. This could lead to performance issues under load.
        Depth of 2: Indicates a similar issue but with a slightly larger queue. It means that there’s a bit more capacity, but still, it’s relatively low for handling a high number of concurrent requests.

 ---

## Deploy the Storage API, Prometheus, and Grafana to Kubernetes

* All the deployment of kubernetes manifest files are in `kubernetes` folder, to run them localy on your kubernetes cluster:

```bash
kubectl apply -f storage-api.yaml
kubectl apply -f prometheus.yaml
kubectl apply -f grafana.yaml

```

---

## Challenges

* **Python Understanding**: Initially unfamiliar with Python,  took time to research the code, learning how Flask and Prometheus work.
* **Prometheus & Grafana**:  had no prior experience installing or configuring dashboards and metrics, but learned by experimenting and exploring documentation.
* **Kubernetes**: Due to limited time,  only created the Kubernetes manifest files. With more time,  would have deployed the app to AWS EKS (Elastic kuberentes service) or GKE (Google Cloud Engine) using ArgoCD and GitLab CI for full automation, and ECR (Elastic container registery) by AWS for image storage.

