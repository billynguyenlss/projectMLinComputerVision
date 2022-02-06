import pathlib

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

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
    python_requires=">=3.6, <4",
    install_requires=[
        "numpy>=1.22",
        "opencv-contrib-python>=4.5",
        "tensorflow>=2.6",
        "tflite_runtime",
    ],
    package_data={"projectmlincvmediapipe": ["model_float16_quant.tflite", "portrait.jpg"]},
    entry_points={"console_scripts": ["demo=projectmlincvmediapipe.demo:main"]},
)
