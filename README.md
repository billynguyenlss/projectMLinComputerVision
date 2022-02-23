# projectMLinComputerVision

This project under the course "Project machine learning in computer vision".
Please follow the instruction from below to set up environment for local running.

## Week 1 - Assignment 1

Please visit the branch `week1a` to reproduce my work under first assignment of week 1.

```
https://github.com/billynguyenlss/projectMLinComputerVision/tree/week1a

git clone -b week1a https://github.com/billynguyenlss/projectMLinComputerVision.git
```

## Week 1 - Assignment 2

Please visit the branch `week1b` to reproduce my work under second assignment of week 1.

```
https://github.com/billynguyenlss/projectMLinComputerVision/tree/week1b

git clone -b week1b https://github.com/billynguyenlss/projectMLinComputerVision.git
```

## Week 2 - Assignment 1

Please visit the branch `week2a` to reproduce my work under first assignment of week 2.

```
https://github.com/billynguyenlss/projectMLinComputerVision/tree/week2a

git clone -b week2a https://github.com/billynguyenlss/projectMLinComputerVision.git
```

## Week 2 - Assignment 2

Please visit the branch `week2b` to reproduce my work under first assignment of week 2.

```
https://github.com/billynguyenlss/projectMLinComputerVision/tree/week2b
```

### 1) Prepare the test environment

Select python version (as tensorflow work only for python version 3.7-3.9) and create a virtual environment

**In Ubuntu:**

```python
pyenv install 3.8.10
```

Create and activate virtual environment:

```python
pyenv virtualenv 3.8.10 .venv

pyenv local .venv
```

**In Window:**

```python
conda create -n <your_virtual_environment_name> python=3.8.10

conda activate <your_virtual_environment_name>
```

### 2) Clone my project and build the package

```bash
git clone --branch week2b https://github.com/billynguyenlss/projectMLinComputerVision.git
cd projectMLinComputerVision
```

For all below steps, make sure you are in the test virtual environment, specified as above.

### 3) Prepare test cases as requirements

All test cases are prepared in folder `test`.

* function `test_regression()` for assignment requirement: "A regression test using a single image that checks results are always the same".
* function `test_small_image()` and `test_large_image()` for assignment requirement: "A “no error” test with big image, small image".

### 4) Test in local

You can install `pytest` in virtual environment and run pytest locally before pushing to github repo.

```python
pip install pytest
```
Then run the pytest by following command:

```python
pytest
```

### 5) Build CI/CD pipeline

Push the completed project to github repo, then set up in Github Action a CI/CD flow to build a Python package.

Once complete, every time you commit and push a new version (in my case, the branch `main`), then it's automatically build and test the new version. The successful CI/CD flow is as following:

![Completed CI/CD workflow](img/week2b-001.JPG)
