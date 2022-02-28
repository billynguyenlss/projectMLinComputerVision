# For more information, please refer to https://aka.ms/vscode-docker-python
FROM ubuntu:20.04 as base

# # Keeps Python from generating .pyc files in the container
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies for ubuntu build
RUN apt-get update && apt-get install -y --no-install-recommends build-essential
RUN apt-get install -y --no-install-recommends python3 python3-pip python3.8-venv python3.8-dev
RUN apt-get install -y --fix-missing ffmpeg libsm6 libxext6

RUN python3 -m pip install --upgrade pip && python3 -m pip install build

# install dependencies for streamlit web demo
COPY dist/projectmlincvmediapipe-0.1.0-py3-none-any.whl .
RUN python3 -m pip install projectmlincvmediapipe-0.1.0-py3-none-any.whl

RUN python3 -m pip install streamlit

# copy app.py to run
WORKDIR /app
COPY streamlitapp/app.py /app

# expose to computer port 8501 to connect to streamlit app via localhost:8501
EXPOSE 8501

# define entry point and cmd to run streamlit app
ENTRYPOINT ["streamlit", "run"]
CMD [ "app.py"]
