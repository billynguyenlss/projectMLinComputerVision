import os.path as osp
import pathlib
from glob import glob

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")


def get_data():
    current_dir = osp.abspath(osp.dirname(__file__))
    data = glob(current_dir + "/src/projectmlincvmediapipe/*/*")
    data = ["/".join(elem.replace("\\", "/").split("/")[-2:]) for elem in data]

    return data


setup(
    name="projectmlincvmediapipe",
    version="0.1.0",
    description="demo packaging python project using Mediapipe Meet Segmentation pretrained model",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/billynguyenlss/projectMLinComputerVision",
    author="billynguyen",
    author_email="billynguyen.lss@gmail.com",
    package_dir={"": "src"},
    packages=find_packages(where="src"),  # Required
    python_requires=">=3.7, <3.10",
    install_requires=[
        "numpy==1.20.0",
        "opencv-contrib-python==4.5.5.62",
        # "tensorflow==2.8.0",
        "tflite_runtime>=2.5",
    ],
    package_data={"projectmlincvmediapipe": ["img/*.jpg", "model/*.tflite"]},
    entry_points={"console_scripts": ["demo=projectmlincvmediapipe.demo:run"]},
)
