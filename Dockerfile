# For more information, please refer to https://aka.ms/vscode-docker-python
FROM ubuntu:20.04

# Keeps Python from generating .pyc files in the container
ENV DEBIAN_FRONTEND=noninteractive

# Turns off buffering for easier container logging
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential \
    python3 \
    python3-pip \
    python3.8-venv \
    python3.8-dev \
    && apt-cache clean \
    && rm -rf /var/apt/archives

RUN python3 -m pip install --upgrade pip \
    && python3 -m pip install build

# Install pip requirements
# COPY requirements.txt .
# RUN python -m pip install -r requirements.txt
RUN python3 -m build
RUN python3 -m pip install dist/projectmlincvmediapipe-0.1.0.tar.gz
RUN python3 -m pip install streamlit

WORKDIR /app
COPY . /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["streamlit run", "streamlitapp\app.py"]
