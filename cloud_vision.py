import base64
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "superb-robot-420515-356ed151ac07.json"


def detect_landmarks(path):
    """Detects landmarks in the file."""
    from google.cloud import vision

    client = vision.ImageAnnotatorClient()

    with open(path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.landmark_detection(image=image)
    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )

    landmarks = response.landmark_annotations
    if landmarks == []:  # "Cannot Detech Location"
        # raise Exception("Cannot Detech Location")
        return
    result = dict()
    result["landmark"] = landmarks[0].description
    loc = landmarks[0].locations
    result["latitude"] = loc[0].lat_lng.latitude
    result["longtitude"] = loc[0].lat_lng.longitude
    return result


# if image is detectable
# return {'landmark': 'Taj Mahal', 'latitude': 27.175144799999998, 'longtitude': 78.04214219999999} else return None
for i in range(1, 11):
    name = f"./test_img/test{i}.jpg"
    print(detect_landmarks(name))
