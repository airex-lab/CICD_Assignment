# CICD Assignment - Devaraj N (First action got passed and second action got failed due to score criteria)

## Introduction
- This repository contains a `data` folder containing the datasets for training and testing.
- It contains a `train.py` file for training a model and saving it and a `test.py` for testing the model.
- It contains a `requirements.txt` listing the python dependencies.
- It also contains a workflow file at `.github/workflows/score.yml` which trains the model in `train`.py and then tests it using `test.py` and succeeds only if the score is above `0.50`.
- You can view the [pull request](https://github.com/StarsCDS/CICD_Assignment/pull/2) for an example.

## Steps
- Fork this repository
- Create an account in docker hub (or any other registry of your choice)
- Create a Dockerfile which trains the model in the building phase and executes `test.py` when the container is run
- Create 2 github action workflows triggered on pull request
  - First one: creates a docker image and pushes it to a registry
  - Second one: pulls the docker image from the registry and runs it. It succeeds only if the score returned is greater than 0.50
- Have 3 separate pull requests from different branches covering the following 3 scenarios 
  - Both of your actions fail
  - One of your actions fail
  - Both of your actions pass
- Note: You should change only the `train.py` file
- Note: The second action should only run if the first one passes
- Names of the actions: `Train`(first one) and `Test`(second one)
