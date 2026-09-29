This repo belongs to Duwon Kong and it's group for purpose of 2810ICT Assignment 2, Griffith University.

This repo includes:

Flat rate calculation model (Complete, sanity check may required)

Time-Of-Usage (TOU) rate calculation model (Complete, sanity check may required)

Tiered rate calculation model (Complete, sanity check may required)

Pandas testing

requirements.txt: for environment requirement

Sample usage dataset (CSV format)

## Usage 

### Linux/MacOS

#### Running the code

1. `python -m venv .venv`
2. `source .venv/bin/activate`
3. `pip install -r requirements.txt`
4. `./main.py`

#### Running the testing framework

1. After you have installed all of the required packages, you run `pytest` to see the test results
2. For more a more verbose output and you'd like to see the specific tests ran, run `pytest -v`
3. To generate the coverage report, run `pytest --cov --cov-report html`
4. To generate testing reports run `pytest --html report.html` or to generate 
a report of a report of a specific test, run `pytest test_flat.py --html flat.html`
