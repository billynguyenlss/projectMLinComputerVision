# For more information, please refer to https://aka.ms/vscode-docker-python
FROM ubuntu:20.04

# # Keeps Python from generating .pyc files in the container
ENV DEBIAN_FRONTEND=noninteractive

# Turns off buffering for easier container logging
RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential
RUN apt-get install -y --no-install-recommends python3
RUN apt-get install -y --no-install-recommends python3-pip
RUN apt-get install -y --no-install-recommends python3.8-venv
RUN apt-get install -y --no-install-recommends python3.8-dev

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install build
