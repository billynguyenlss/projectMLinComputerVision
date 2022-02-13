# projectMLinComputerVision

This project under the course "Project machine learning in computer vision".
Please follow the instruction from below to set up environment for local running.

Clone my github repo, specify by branch `week1a`.

```python
git clone --b week1a https://github.com/billynguyenlss/projectMLinComputerVision.git
cd projectMLinComputerVision
```

## 1) Select python version (as tensorflow work only for python version 3.7-3.9) and create a virtual environment

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

## 2) Install dependencies for this demo project. 

This command is not required if you are rerunning this project.

```python
pip install -r requirements.txt
```

## 3) Running the demo.py

**In Ubuntu:**
```python
python3 demo.py
```

**In Window:**
```python
python demo.py
```

## 4) Results
If you are running successfully, there are 3 output images `out1.jpg`, `out2.jpg`, `out3.jpg` in the project directory.
In addition, the output in the console is as following:

![Screen capture of successfully run of task 1](img/project1.jpg)