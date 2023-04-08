import cv2
import numpy as np

def ela(image_path, output_path):
    original_image = cv2.imread(image_path)
    temp_image_path = "temp.jpg"
    cv2.imwrite(temp_image_path, original_image, [cv2.IMWRITE_JPEG_QUALITY, 90])
    temp_image = cv2.imread(temp_image_path)

    diff = cv2.absdiff(original_image, temp_image)
    gray_diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    ela_image = cv2.GaussianBlur(gray_diff, (5,5), 0)

    cv2.imwrite(output_path, ela_image)

    return ela_image
