# projectMLinComputerVision

# Contents

- **1. Background:**
    * General description of project
    * Environment requirements
- **2. Reporting:** Report summary by weekly assignment: this include the project implementation, outcome, methods and technologies applied during the project, any issues and challenges during project implementation.
    * Week 1a
    * Week 1b
    * Week 2a
    * Week 2b
    * Week 3
- **3. Conclusion:** Assessment of a project's individual results, as well as acquired competentices.
- **4. Project outcome:** (e.g. texts, photographs, references and other materials)
- **5. Annexes:**
(if necessary: presentations for the project defence, diagrams, designs, tables, algorithms, illustrations, reviews, etc).
    - Mediapipe Meet Segmentation:
    - Docker documents
    - Streamlit documents

# 1. Background

## 1.1 Project description

This repository is my attempt to build and packaging a package from a Python project, which applied a pretrained model from research code to practice, as well as to set up a Working Environment, Continuous Integration/Continuous Deployment, create ready-for-production Docker image and publish to Docker hub.

THe pretrained model from research code is Mediapipe Meet Segmentation, which can be found from:

```
https://github.com/PINTO0309/PINTO_model_zoo/tree/main/082_MediaPipe_Meet_Segmentation
```
The program from my project takes a selfie image and segments human out of the background.

https://google.github.io/mediapipe/images/selfie_segmentation_web.mp4

## 1.2 Environment set up

Please follow the instruction from below to set up environment for local running.

**Clone my project to your local directory**

```bash
git clone https://github.com/billynguyenlss/projectMLinComputerVision.git
cd projectMLinComputerVision
```

**Set up Python environment**

Select python version (as tensorflow work only for python version 3.7-3.9) and create a virtual environment

In Ubuntu:
```
pyenv install 3.8.10

pyenv virtualenv 3.8.10 .venv

pyenv local .venv
```

In Window:
```
conda create -n <your_virtual_environment_name> python=3.8.10

conda activate <your_virtual_environment_name>
```

# 2. Reporting

**Week 1 - Assignement 1**

Run the demo code, using pretrained model from Mediapipe Meet Segmentation.

Please visit the branch `week1a` for project implementation and reproduce my work under first assignment of week 1.

```
git checkout week1a
```

**Week 1 - Assignment 2**

Set-up Build and packaging project to a Python package, which other users can build a Python package and install it from local directory or from git. To build a python package, I have defined all specification in `setup.py`.

Please visit the branch `week1b` to reproduce my work under second assignment of week 1.

```
git checkout week1b
```

The most challenge in this assignment from my perspective is about the documents/guideline for Python packaging task. It's not a clear step-by-step guideline, and lack of explaination and intuitive for some set up specification.

**Week 2 - Assignment 1**

Setup project for team work (style tools, static analysis). I have applied the technologies for style & linter tools as following:
* `black`: configure in `black.toml` file.
* `isort`: configure in `pyproject.toml` file.
* `flake8`: configure in `tox.ini` file.
* `pre-commit`: configure in `pre-commit-config.yaml` file.

Please visit the branch `week2a` for project implementation and to reproduce my work.

```
git checkout week2a
```

**Week 2 - Assignment 2**

Prepare a continious integration pipeline for your project as well as a set of the tests.

* The test cases are prepared in `test` folder and are tested by `pytest`.
* The CI workflows are set up in:
    * For auto build and test, set up another CI workflow `.github/workflows/testPush.yml`.
    * For auto testing for every pull request, set up another CI workflow `.github/workflows/testPR.yml`.
* To make CI check working for every PR/MR, go to Settings -> Branches -> add rule.

Please visit the branch `week2b` for detail project implementation and to reproduce my work.

```
git checkout week2b
```

**Week 3 - Assignment**

Build Docker image to prepare a web demo for the project.

* The docker image building spec are defined in Dockerfile and `docker-compose.yml` files.
* The CI workflow to build and push the docker image to Docker Hub is defined in `.gibhub/workflows/docker-build-push.yml`. The procedure to prepare this file can be refered from https://docs.docker.com/ci-cd/github-actions/.
* To make CI workflow run faster, I have configured the build-cache in the Dockerfile, please refer detail in `.gibhub/workflows/docker-build-push.yml`.

Please visit the branch `week3` for project implementation and to reproduce my work.

```
git checkout week3
```

The most challenge in this assignment is to keep the size of the Docker image small as well as less number of layers. Furthermore, there are further works to improve my current set up such as to re-order the Docker image building workflow to run after the Merge and Push test workflows.

# 3. Conclusion

This project provide knowledge and experience to apply a Computer Vision model from research code to production-ready solution.
It include building and packaging a package from a Python project, setting up a Working Environment, styling and linting for team-work, Continuous Integration/Continuous Deployment, creating ready-for-production Docker image and publish to Docker hub.

# 4. Project outcome

Please refer to below video for short demo of the project.

https://user-images.githubusercontent.com/51374762/156072280-4b01cfaa-b14c-4167-8e80-ee40423cad69.mp4

Or running following command (make sure you have Docker installed in your local machine):

```
docker container run -p 8501:8501 billynguyenco/projectmlincomputervision_mediapipe:latest
```

# 5. Annexes
- Mediapipe Meet Segmentation: https://github.com/PINTO0309/PINTO_model_zoo/tree/main/082_MediaPipe_Meet_Segmentation
- Docker documents: https://docs.docker.com/
- Streamlit documents: https://docs.streamlit.io/
- Python packaging: https://packaging.python.org/en/latest/
- flake8: https://flake8.pycqa.org/en/latest/
- pre-commit: https://pre-commit.com/
- Github action documents: https://docs.github.com/en/actions
