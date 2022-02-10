from src.projectmlincvmediapipe import demo


def test_regression():
    output, out1, out2 = demo.main("portrait.jpg")
    print("output:", output.shape)
    print("out1:", out1.shape)
    print("out2:", out2.shape)
    assert output.shape == (1, 144, 256, 2)
    assert out1.shape == (144, 256)
    assert out2.shape == (144, 256)


def test_small_image():
    pass


def test_large_image():
    pass
