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
## Week 3 - Assignment

### 1) Install docker

Make sure you have docker installed in your system.

### 2) Clone my project

```bash
git clone --branch week3 https://github.com/billynguyenlss/projectMLinComputerVision.git
cd projectMLinComputerVision
```

### 3) Prepare Inference web app demo with streamlit

To use streamlit, I have add the streamlit to the `requirements.txt` file.
In the virtual environment, install streamlit, if you want to run my web app locally without using docker.

```python
pip install streamlit
```
The streamlit app is prepared in `streamlitapp/app.py` file.
Please select and upload any selfie image with format `jpg`, `jgeg`, `png`.

### 4) Build docker image

The docker image building spec are defined in `Dockerfile` and `docker-compose.yml` files.

The CI workflow to build and push the docker image to Docker Hub is defined in `.gibhub/workflows/docker-build-push.yml`. The procedure to prepare this file can be refered from https://docs.docker.com/ci-cd/github-actions/.

To make CI workflow run faster, I have configured the build-cache in the `Dockerfile`, please refer detail in `.gibhub/workflows/docker-build-push.yml`.

### 5) Running docker image

To run my docker image, please run following command (make sure you have Docker installed in your system).

```python
docker container run -p 8501:8501 billynguyenco/projectmlincomputervision_mediapipe:latest
```

Then you can access my web app via http://localhost:8501

The video example is attached as below:


https://user-images.githubusercontent.com/51374762/156072280-4b01cfaa-b14c-4167-8e80-ee40423cad69.mp4

