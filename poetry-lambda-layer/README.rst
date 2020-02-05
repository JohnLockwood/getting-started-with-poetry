************************
Poetry Lambda Layer Demo
************************

This project shows how to build and publish a Lambda Layer of non-trivial complexity. I mean it would serve as the starting point for a "common code" sort of library.  As such, we need to demonstrate a simple package structure **with** some external package dependencies.  To keep this simple, we'll add a dependency on the requests library ::

    poetry new poetry-lambda-layer
    cd poetry-lambda-layer
    poetry add requests

