import cv2
import numpy as np


address = "C:/Users/Ali/Documents/Tumor recognition/yes/Y8.jpg"


def auto_canny(image, sigma=0.33):
    # compute the median of the single channel pixel intensities
    v = np.median(image)
    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper)
    # return the edged image
    return edged


def resize(img_path=address):
    image = cv2.imread(img_path)
    dim = (200, 290)
    image = cv2.resize(image, dim)
    img_path = img_path.replace("jpg", r"jpeg")
    print(img_path)
    cv2.imwrite(img_path, image)
    return img_path


def BGR2GRAY(img_path=address):
    """img_path = img_path of resize function"""
    image = cv2.imread(img_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY, 0.7)
    img_path = img_path.replace(".jpeg", "_gray.jpeg")
    print(img_path)
    cv2.imwrite(img_path, gray)
    return img_path


def THRESH_BINARY(img_path=address):
    """img_path = img_path of resize function"""
    image = cv2.imread(img_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY, 0.7)
    (T, thresh) = cv2.threshold(gray, 153, 255, cv2.THRESH_BINARY)
    img_path = img_path.replace(".jpeg", "_THRESH_BINARY.jpeg")
    print(img_path)
    cv2.imwrite(img_path, thresh)

    return img_path


def THRESH_BINARY_INV(img_path=address):
    """img_path = img_path of resize function"""
    image = cv2.imread(img_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY, 0.7)
    (T, threshInv) = cv2.threshold(gray, 153, 255, cv2.THRESH_BINARY_INV)

    img_path = img_path.replace(".jpeg", "_THRESH_BINARY_INV.jpeg")
    print(img_path)
    cv2.imwrite(img_path, threshInv)

    return img_path


def MORPH_CLOSE(img_path=address):
    """img_path = img_path OF THRESH_BINARY function"""
    thresh = cv2.imread(img_path)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 5))
    closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    img_path = img_path.replace("_THRESH_BINARY.jpeg", "_morph_close.jpeg")
    print(img_path)
    cv2.imwrite(img_path, closed)

    return img_path


def erode_and_dilate_func(img_path=address):
    """img_path = img_path of MORPH_CLOSE function"""
    closed = cv2.imread(img_path)
    closed = cv2.erode(closed, None, iterations=6)
    closed = cv2.dilate(closed, None, iterations=10)

    img_path = img_path.replace("_morph_close.jpeg", "_erode_and_dilate_func.jpeg")
    print(img_path)
    cv2.imwrite(img_path, closed)

    return img_path


def show_environment_of_tumor(img_path=address):
    """img_path = img_path of resize function"""

    image = cv2.imread(img_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY, 0.7)

    (T, thresh) = cv2.threshold(gray, 153, 255, cv2.THRESH_BINARY)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 5))
    closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    closed = cv2.erode(closed, None, iterations=6)
    closed = cv2.dilate(closed, None, iterations=10)

    canny = auto_canny(closed)

    img_path = img_path.replace(".jpeg", "_environment.jpeg")
    print(img_path)
    cv2.imwrite(img_path, canny)

    return img_path


def show_tumor(img_path=address):
    """img_path = img_path of resize function"""

    image = cv2.imread(img_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY, 0.7)

    (T, thresh) = cv2.threshold(gray, 153, 255, cv2.THRESH_BINARY)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 5))
    closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    closed = cv2.erode(closed, None, iterations=6)
    closed = cv2.dilate(closed, None, iterations=10)

    canny = auto_canny(closed)

    (cnts, _) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(image, cnts, -1, (0, 255, 0), 2)

    img_path = img_path.replace(".jpeg", "_show_tumor.jpeg")
    print(img_path)
    cv2.imwrite(img_path, image)
    return img_path


