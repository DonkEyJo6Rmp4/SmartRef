def hello_video():
    return "Hello from SmartRef video module"


def calculate_duration(frame_count, fps):
    if (fps <= 0):
        raise ValueError("Invalid Input: fps <= 0")
    if (frame_count <=0):
        raise ValueError("Invalid Input: frame_count <= 0")
    
    return (frame_count / fps)
