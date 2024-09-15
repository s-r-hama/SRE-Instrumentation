## SRE-Instrumentation

This project involves adding Prometheus instrumentation to an in-memory Storage API written in Python.

### Goal

The goal is to integrate Prometheus metrics into the Storage API and visualize them using Grafana. **Storage API** this service implements a simple in-memory Storage API for putting, getting, and deleting binary data. 

---

### Steps Taken

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

Follow the steps outlined in *src/README.md* for setup details.

I run the following commands in MacOS



* Install Dependencies


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


* Development Setup

Install Development Dependencies

Run make dev or pip3 install -e .[dev]:

```bash

make dev or pip3 install -e .[dev]
```

Explanation: The -e flag installs the package in editable mode, and [dev] installs additional development dependencies such as linters and testing frameworks.

* Run Tests

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

* Run the Service with Hot Reloading

If hupper is not found, ensure it is installed and in your PATH. To run the service with hot reloading:


```bash
hupper -m waitress --port 5000 storage:app
````

Explanation: hupper enables hot reloading of Python applications.
-m specifies the module to run.
waitress is the WSGI server hosting your application.
--port 5000 sets the port for the server.
storage:app specifies the WSGI application callable.


---


























