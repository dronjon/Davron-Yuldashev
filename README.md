Note: You should make sure that Swagger Petsore Sample local environment is up and running.
# Pet Store API tests

A number of pet store API tests were set up using pytest framework as part of the take-home challenge.

## Installation

It is best to use PyCharm community edition in order to set up and run these API tests. PyCharm can be installed [here](https://www.jetbrains.com/pycharm/download/). Once you have installed PyCharm, you will need to pull the tests from a GitHub repository which can be found [here](https://github.com/dronjon/test-project). Once the repo is pulled, run this command to install all the necessary libraries.

```bash
pip install -r requirements.txt
```

## To Run
To run the tests you need to open a new terminal window, which can be opened at the bottom left corner of PyCharm. Make sure that you are in the project root folder. Once you are in the root type/paste
```python
pytest 
```
 in your command line and hit enter. The above command will run all of the tests. If you want to run an individual test, you will need to type/paste

```python
pytest -k <name_of_the_test> 
```


# Test Reports

You can run a detailed report on the test and view it as HTML. To do that type
```bash
pytest --alluredir=reports/allure
```
after you run all of the tests or after the individual test name generate the test report by typing
```bash
allure serve reports/allure
```
in the command line. The report will allow you to see a detailed overview of how many tests you run, how many of them passed and how many failed.
