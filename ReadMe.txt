# Master Testing Framework using Python Pytest
The testing framework has following dependencies:-

1> boto3 : sudo pip install boto3   ---S3 cli
2> paramiko: sudo apt-get install python-paramiko   -- ssh client
3> pytest: sudo pip install pytest       -- Pytest package
4> pytest coverage: sudo pip install -U pytest-cov  -- To measure the code Coverage
5> pytest: sudo pip install -U pytest-xdist     -- To run tests parallel
6> pytest: sudo pip install -U pytest-html      -- to generate html reports
7> PyPy:sudo apt-get install pypy
8> aws cli: sudo pip install awscli
9> confirgure aws cli: http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html
10> python -m pip install requests



Pytest
=================================================
pip install pytest-xdist
wget https://bootstrap.pypa.io/get-pip.py
sudo pypy get-pip.py
pypy -m pip install pytest

Usage of pytest
=================================================

Run all test in a module
------------------------
pytest test_mod.py

Run tests by keyword expressions
--------------------------------
pytest -k "keywordInTestsName"

To Generate pytest html report
--------------------------------
py.test --html=report.html

Run a specific test within a module
---------------------------------------
pytest test_mod.py::test_func
OR
pytest test_mod.py::TestClass::test_method

Run test with marker
---------------------
pytest -m <marker> e.g. pytest -m slow

Run test with package
---------------------
pytest --pyargs pkg.testing

Run tests in parallel
---------------------
py.test -n 4
## Test will run in 4 parallel nodes

Run all test in a folder
---------------------------
py.test -v

Run selected tests
--------------------
python -m pytest [...]

stop after first failure
----------------------------
pytest -x
stop after first N failures
----------------------------
pytest --maxfail=N

pytest Measure Coverage:
-----------------------------
py.test --cov-report html --cov [myPackage] --verbose
## mention all packages in array

pytest Exit codes
-------------------------------------------------------------------------
Exit code 0:	All tests were collected and passed successfully
Exit code 1:	Tests were collected and run but some of the tests failed
Exit code 2:	Test execution was interrupted by the user
Exit code 3:	Internal error happened while executing tests
Exit code 4:	pytest command line usage error
Exit code 5:	No tests were collected

pytest plugins
===============
https://docs.pytest.org/en/latest/plugins.html#plugins

pytest Fixtures
==================
https://docs.pytest.org/en/latest/fixture.html#fixtures


Test Guidelines
=================
1> Always write test with module name and method name start with 'test_'
2> There should be one test Module per feature
3> All Test cases should be there in TestCases python package
