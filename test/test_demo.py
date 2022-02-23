import os
import os.path as osp
import sys

import cv2
import numpy as np
import pytest
from cv2 import IMREAD_GRAYSCALE

from projectmlincvmediapipe import demo

sys.path.append(osp.dirname(osp.realpath(__file__)))


@pytest.mark.parametrize("img_name", ["img/portrait.jpg"])
def test_regression(img_name):
    def mse(imageA, imageB):
        err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
        err /= float(imageA.shape[0] * imageA.shape[1])
        return err

    dir_path = os.path.abspath(os.path.dirname(__file__))
    img_path = os.path.join(dir_path, img_name)

    out1_true = cv2.imread(os.path.join(dir_path, "img/out1_true.jpg"), IMREAD_GRAYSCALE)
    out2_true = cv2.imread(os.path.join(dir_path, "img/out2_true.jpg"), IMREAD_GRAYSCALE)
    out3_true = cv2.imread(os.path.join(dir_path, "img/out3_true.jpg"), IMREAD_GRAYSCALE)
    print("true out1:", out1_true.shape)
    print("true out2:", out2_true.shape)
    print("true out3:", out3_true.shape)
    img = cv2.imread(img_path)
    print("img:", img.shape)

    h = img.shape[0]
    w = img.shape[1]

    output, out1, out2, out3 = demo.main(img_path)
    print("output:", output.shape)
    print("out1:", out1.shape)
    print("out2:", out2.shape)
    assert output.shape == (1, 144, 256, 2)
    assert out1.shape == (h, w)
    assert out2.shape == (h, w)
    assert mse(out1, out1_true) < 0.05
    assert mse(out2, out2_true) < 0.05
    assert mse(out3, out3_true) < 0.05


@pytest.mark.parametrize("img_name", ["img/portrait_small_1.jpg", "img/portrait_small_2.jpg"])
def test_small_image(img_name):

    dir_path = os.path.abspath(os.path.dirname(__file__))
    img_path = os.path.join(dir_path, img_name)
    print(os.getcwd())
    img = cv2.imread(img_path)

    h = img.shape[0]
    w = img.shape[1]

    output, out1, out2, out3 = demo.main(img_path)
    print("output:", output.shape)
    print("out1:", out1.shape)
    print("out2:", out2.shape)
    assert output.shape == (1, 144, 256, 2)
    assert out1.shape == (h, w)
    assert out2.shape == (h, w)


@pytest.mark.parametrize("img_name", ["img/portrait_large_1.jpg", "img/portrait_large_2.jpg"])
def test_large_image(img_name):

    dir_path = os.path.abspath(os.path.dirname(__file__))
    img_path = os.path.join(dir_path, img_name)
    print(os.getcwd())
    img = cv2.imread(img_path)

    h = img.shape[0]
    w = img.shape[1]

    output, out1, out2, out3 = demo.main(img_path)
    print("output:", output.shape)
    print("out1:", out1.shape)
    print("out2:", out2.shape)
    assert output.shape == (1, 144, 256, 2)
    assert out1.shape == (h, w)
    assert out2.shape == (h, w)


if __name__ == "__main__":
    test_regression()
    test_large_image()
    test_small_image()
