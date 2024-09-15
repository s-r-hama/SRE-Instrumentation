from unittest.mock import patch
from storage import app

import json
import storage


@patch("storage.bucket.data", {})
def test_get_bucket_not_found():
    response = app.test_client().get("/api/buckets/1")
    assert response.status_code == 404

    payload = json.loads(response.data)
    assert payload["error"] == "not found"


@patch("storage.bucket.data", {"1": "hello"})
def test_get_bucket_found():
    with patch("storage.bucket.data", {"1": "hello"}):
        response = app.test_client().get("/api/buckets/1")

        assert response.status_code == 200
        assert response.data == b"hello"


@patch("storage.bucket.data", {})
def test_put_bucket():
    response = app.test_client().put("/api/buckets/1", data="hello")

    assert response.status_code == 200
    assert storage.bucket.data == {"1": b"hello"}


@patch("storage.bucket.data", {})
def test_delete_bucket_not_found():
    response = app.test_client().delete("/api/buckets/1")
    assert response.status_code == 400

    payload = json.loads(response.data)
    assert payload["error"] == "bad request"


# TODO: Add test for test_delete_bucket_found


######## explanation here  of the code above


"""The unittest.mock module in Python provides a framework for creating and using mock objects for unit testing. It is especially useful for isolating code under test from external dependencies, allowing you to test your code in a controlled and predictable environment. Here's a summary of what unittest.mock does:

    Create Mock Objects: unittest.mock allows you to create mock objects that can simulate the behavior of real objects. These mocks can be configured to return specific values, raise exceptions, or track how they are used.

    Patch Objects: The patch function is used to replace real objects in your code with mock objects during the test. This is useful for isolating the code under test from external systems like databases, APIs, or file systems.

    Assertions: Mocks come with built-in assertions to verify how they were used, such as checking if methods were called, how many times they were called, and with what arguments.

    Spec and Side Effects: You can specify how mocks should behave by defining their return values or side effects (e.g., raising exceptions). This helps simulate various scenarios and edge cases.

    Call History: Mocks can track how many times they were called and with what arguments. This is useful for verifying that your code interacts with them correctly.

Common Functions and Classes

    Mock: The base class for creating mock objects. You can instantiate a Mock object and configure it to return specific values or raise exceptions.

    MagicMock: A subclass of Mock that includes additional methods and attributes that make it behave more like a real object, such as __getitem__, __setitem__, and __iter__.

    patch: A decorator or context manager that temporarily replaces an object with a mock during the test. It’s commonly used to replace functions, methods, or objects in modules.

    patch.object: A variant of patch that specifically replaces attributes on objects.

    patch.dict: A variant of patch that replaces dictionary items during the test.

    patch.multiple: Allows you to patch multiple attributes on an object at once."""



"""This code is a set of unit tests for an API, using pytest and unittest.mock.patch to mock certain parts of the storage module. Here’s a breakdown of what each test does:

    test_get_bucket_not_found():
        Setup: Mocks storage.bucket.data to be an empty dictionary {}.
        Action: Sends a GET request to /api/buckets/1 using the Flask test client.
        Assertions:
            Asserts that the response status code is 404 (Not Found).
            Asserts that the response JSON payload contains an error message "not found".

    test_get_bucket_found():
        Setup: Mocks storage.bucket.data to contain a single entry {"1": "hello"}.
        Action: Sends a GET request to /api/buckets/1 using the Flask test client.
        Assertions:
            Asserts that the response status code is 200 (OK).
            Asserts that the response data is the byte string b"hello".

    test_put_bucket():
        Setup: Mocks storage.bucket.data to be an empty dictionary {}.
        Action: Sends a PUT request to /api/buckets/1 with the data "hello".
        Assertions:
            Asserts that the response status code is 200 (OK).
            Asserts that storage.bucket.data has been updated to {"1": b"hello"} (note that the data is stored as bytes).

    test_delete_bucket_not_found():
        Setup: Mocks storage.bucket.data to be an empty dictionary {}.
        Action: Sends a DELETE request to /api/buckets/1 using the Flask test client.
        Assertions:
            Asserts that the response status code is 400 (Bad Request).
            Asserts that the response JSON payload contains an error message "bad request"."""