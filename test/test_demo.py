import os

import cv2

from src.projectmlincvmediapipe import demo


def test_regression():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    img_path = os.path.join(dir_path, "portrait.jpg")
    img = cv2.imread(img_path)

    h = img.shape[0]
    w = img.shape[1]

    output, out1, out2 = demo.main("portrait.jpg")
    print("output:", output.shape)
    print("out1:", out1.shape)
    print("out2:", out2.shape)
    assert output.shape == (1, 144, 256, 2)
    assert out1.shape == (h, w)
    assert out2.shape == (h, w)


def test_small_image():
    for img_name in ["portrait_small_1.jpg", "portrait_small_2.jpg"]:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        img_path = os.path.join(dir_path, img_name)
        img = cv2.imread(img_path)

        h = img.shape[0]
        w = img.shape[1]

        output, out1, out2 = demo.main("portrait.jpg")
        print("output:", output.shape)
        print("out1:", out1.shape)
        print("out2:", out2.shape)
        assert output.shape == (1, 144, 256, 2)
        assert out1.shape == (h, w)
        assert out2.shape == (h, w)


def test_large_image():
    for img_name in ["portrait_large_1.jpg", "portrait_large_2.jpg"]:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        img_path = os.path.join(dir_path, img_name)
        img = cv2.imread(img_path)

        h = img.shape[0]
        w = img.shape[1]

        output, out1, out2 = demo.main("portrait.jpg")
        print("output:", output.shape)
        print("out1:", out1.shape)
        print("out2:", out2.shape)
        assert output.shape == (1, 144, 256, 2)
        assert out1.shape == (h, w)
        assert out2.shape == (h, w)
