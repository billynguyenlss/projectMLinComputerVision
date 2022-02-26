# For more information, please refer to https://aka.ms/vscode-docker-python
FROM ubuntu:20.04

# # Keeps Python from generating .pyc files in the container
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies for ubuntu build
RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential \
    python3 python3-pip python3.8-venv python3.8-dev
RUN apt-get install -y --fix-missing ffmpeg libsm6 libxext6

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install build

# install dependencies for streamlit web demo
COPY dist/projectmlincvmediapipe-0.1.0-py3-none-any.whl .
RUN python3 -m pip install projectmlincvmediapipe-0.1.0-py3-none-any.whl

RUN python3 -m pip install streamlit

# copy app.py to run
WORKDIR /app
COPY streamlitapp/app.py /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
EXPOSE 8501

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
ENTRYPOINT ["streamlit", "run"]
CMD [ "app.py"]
