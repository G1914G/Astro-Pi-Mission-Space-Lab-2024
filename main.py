# Import the PiCamera class from the picamera module
from picamera import PiCamera
from exif import Image
from datetime import datetime

def get_time(image):
    # Open image and read as binary (rb)
    with open(image,'rb') as image_file:
        img = Image(image_file)
        time_str = img.get("datetime_original")
        time = datetime.strptime(time_str, '%Y:%m:%d %H:%M:%S')
    """
    for data in img.list_all():
        print(data)
    """
    return time

def main():
    # Create an instance of the PiCamera class
    cam = PiCamera()

    # Set the resolution of the camera to 4056×3040 pixels
    cam.resolution = (4056, 3040)

    # Capture an image
    cam.capture("image1.jpg")
    cam.capture("image2.jpg")

    time = get_time("image1.jpg")
    print(time)

# main stuff https://realpython.com/python-main-function/
if __name__ == "__main__":
    main()