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

Set-up Build and packaging project to a Python package, which other users can build a Python package and install it from local directory or from git.

Please visit the branch `week1b` to reproduce my work under second assignment of week 1.

```
git checkout week1b
```

**Week 2 - Assignment 1**

Setup project for team work (style tools, static analysis).

Please visit the branch `week2a` for project implementation and to reproduce my work.

```
git checkout week2a
```

**Week 2 - Assignment 2**

Prepare a continious integration pipeline for your project as well as a set of the tests.

Please visit the branch `week2b` for project implementation and to reproduce my work.

```
git checkout week2b
```

**Week 3 - Assignment**

Build Docker image to prepare a web demo for the project.

Please visit the branch `week3` for project implementation and to reproduce my work.

```
git checkout week3
```

# 3. Conclusion
Assessment of a project's individual results, as well as acquired competentices.

# 4. Project outcome

Please refer to each assignment for detail outcome. Attached below is the outcome of week 3 assignment, while running web demo from docker image.


This project provide a great experience and knowledge on how to applied Computer Vision model from research to production.

# 6. Annexes
- Mediapipe Meet Segmentation: https://github.com/PINTO0309/PINTO_model_zoo/tree/main/082_MediaPipe_Meet_Segmentation
- Docker documents: https://docs.docker.com/
- Streamlit documents: https://docs.streamlit.io/
- Python packaging: https://packaging.python.org/en/latest/
- flake8: https://flake8.pycqa.org/en/latest/
- pre-commit: https://pre-commit.com/
- Github action documents: https://docs.github.com/en/actions
