************************
Poetry Lambda Layer Demo
************************

This project shows how to build and publish a Lambda Layer of non-trivial complexity. I mean it would serve as the starting point for a "common code" sort of library.  As such, we need to demonstrate a simple package structure **with** some external package dependencies.  To keep this simple, we'll add a dependency on the requests library ::

    poetry new poetry-lambda-layer
    cd poetry-lambda-layer
    poetry add requests

Our goal will be to expose a function that returns this raw source code for this README.  The URL for that is: ::

    https://raw.githubusercontent.com/JohnLockwood/getting-started-with-poetry/master/poetry-lambda-layer/README.rst

The function code is here in :demo.py:`poetry_lambda_layer/demo.py`.

We'll use poetry itself as a helper for poetry. ::


    poetry add poetry
