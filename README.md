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

git clone -b week2b https://github.com/billynguyenlss/projectMLinComputerVision.git
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
git clone --branch week3 https://github.com/billynguyenlss/projectMLinComputerVision.git
cd projectMLinComputerVision
```

For all below steps, make sure you are in the test virtual environment, specified as above.

### 3) Prepare Inference web app demo with streamlit

To use streamlit, I have add the streamlit to the `requirements.txt` file.
In the virtual environment, install streamlit.

```python
pip install streamlit
```
The streamlit app is prepared in `streamlitapp/app.py` file.
Please select and upload any selfie image with format `jpg`, `jgeg`, `png`.

### 4) Build docker image

The docker image building spec are defined in `Dockerfile` and `docker-compose.yml` files.

The CI workflow to build and push the docker image to Docker Hub is defined in `.gibhub/workflows/docker-build-push.yml`. The procedure to prepare this file can be refered from https://docs.docker.com/ci-cd/github-actions/.

To make CI workflow run faster, pre-configured docker image are set up as ...
