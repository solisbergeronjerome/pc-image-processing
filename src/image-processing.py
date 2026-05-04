import cv2 as cv
import numpy as np

defaultRes = (920, 920)

img = cv.imread("Picture.png")


def reScaleImage(image, res=defaultRes):
    """Scales an image up or down to the default
        resolution set by defaultRes
        (INTER_AREA for downscale).

    Args:
        image (cv): Image to upscale or downscale

    Returns:
        scaledImage: Image set to the default scale
    """
    height, width = image.shape[:2]
    if height < res[0] | width < res[1]:
        scaledImage = cv.resize(image, res, interpolation=cv.INTER_AREA)
    else:
        scaledImage = cv.resize(image, res, interpolation=cv.INTER_LINEAR)
    return scaledImage


def sharpenImage(image):
    """Sharpens image using Laplacien 2D kernel and convolution

    Args:
        image (cv): Image to sharpen

    Returns:
        sharpenedImage: Result of the convolution with Laplacian kernel
    """
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    sharpenedImage = cv.filter2D(image, -1, kernel)
    return sharpenedImage


def defaultProcess(image):
    """Default image processing pipeline
    Only scale to default and sharpen (no segmentation)
    Args:
        image (cv): Image to process

    Returns:
        image : Processed image
    """
    return sharpenImage(reScaleImage(image))


cv.imshow("Camera Feed", defaultProcess(img))
k = cv.waitKey(0)
