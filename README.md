# test-framwork
A Test framework for python projects

## Setup
```
pip install -r requirements.txt
```

## How to run the codes
Unittest can be usde to run individual unit tests for individual components or can be triggered as a whole for the entire folder where all unit test files reside.
```
python -m unittest discover test

python -m unittest -v tests\test_sample_code.py

python -m coverage run -m unittest tests

python -m coverage report
```