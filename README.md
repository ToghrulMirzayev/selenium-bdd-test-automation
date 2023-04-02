# selenium-bdd-test-automation

# Overview
This project demonstrates the use of Behavior-Driven Development (BDD) methodology to write automated tests for a web application using Python, Selenium and Behave.

# Approach
In this project, I followed the BDD methodology to write our automated tests. 
I used: 
* Gherkin syntax to write features, which describe the behavior of the web application in a natural language. 
* Python as the programming language
* Selenium for web automation.
* Behave as a BDD framework, which allows running features as tests. 
* Allure as a test reporting tool, which provides detailed reports on test results.

## Prerequisites
* Python >= 3.8

## Installation
* Clone the repository
* Install the dependencies

```commandline
pip install -r requirements.txt
```

## Usage
To run the tests, use the following command:

```commandline
behave
```

To view the test results in the Allure server, use the following command:

```commandline
allure serve allure-results
```