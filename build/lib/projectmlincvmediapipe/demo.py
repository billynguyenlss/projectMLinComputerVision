import os

import cv2
import numpy as np

try:
    from tflite_runtime.interpreter import Interpreter
except:
    from tensorflow.lite.python.interpreter import Interpreter


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    img_path = os.path.join(dir_path, "portrait.jpg")
    img = cv2.imread(img_path)
    # img = cv2.imread('portrait.jpg')

    h = img.shape[0]
    w = img.shape[1]

    img = cv2.resize(img, (256, 144))
    img = np.asarray(img)
    img = img / 255.0
    img = img.astype(np.float32)
    img = img[np.newaxis, :, :, :]

    # Tensorflow Lite
    model_path = os.path.join(dir_path, "model_float16_quant.tflite")
    interpreter = Interpreter(model_path=model_path, num_threads=4)

    # interpreter = Interpreter(model_path='model_float16_quant.tflite', num_threads=4)
    interpreter.allocate_tensors()
    input_details = interpreter.get_input_details()[0]["index"]
    output_details = interpreter.get_output_details()[0]["index"]

    interpreter.set_tensor(input_details, img)
    interpreter.invoke()
    output = interpreter.get_tensor(output_details)

    print(output.shape)
    out1 = output[0][:, :, 0]
    out2 = output[0][:, :, 1]

    out1 = np.invert((out1 > 0.5) * 255)
    out2 = np.invert((out2 > 0.5) * 255)

    print("out1:", out1.shape)
    print("out2:", out2.shape)

    out1 = cv2.resize(np.uint8(out1), (w, h))
    out2 = cv2.resize(np.uint8(out2), (w, h))

    cv2.imwrite("out1.jpg", out1)
    cv2.imwrite("out2.jpg", out2)

    out3 = cv2.ximgproc.jointBilateralFilter(out2, out1, 8, 75, 75)

    cv2.imwrite("out3.jpg", out3)
