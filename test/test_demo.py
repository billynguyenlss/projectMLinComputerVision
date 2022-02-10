from src.projectmlincvmediapipe import demo


def test_regression():
    output, out1, out2 = demo.main("portrait.jpg")
    print("output:", output)
    assert output == (1, 144, 256, 2)
    assert out1 == (144, 256)
    assert out2 == (144, 256)


def test_small_image():
    pass


def test_large_image():
    pass
