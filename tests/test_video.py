import pytest 
from smartref.data.video import hello_video
from smartref.data.video import calculate_duration

def test_hello_video():
    result = hello_video()
    assert  result == "Hello from SmartRef video module"
    # assert  result == "Test"

def test_calculate_duration():
    result = calculate_duration(
        frame_count = 900,
        fps = 30
    )
    assert result == 30.0

def test_calculate_duration_invalid_fps():
    with pytest.raises(ValueError):
        calculate_duration(
            frame_count = 900,
            fps = 0
        )

def test_calculate_duration_invalid_frame_count():
    with pytest.raises(ValueError):
        calculate_duration(
            frame_count = -900,
            fps = 30
        )
