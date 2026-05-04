import cv2 as cv

defaultRes = (920, 920)

img = cv.imread("Picture.png")


def reScaleImage(image, res=defaultRes):
    """Scales an image up or down to the default
        resolution set by defaultRes
        (INTER_AREA for downscale).

    Args:
        image (cv): image to upscale or downscale

    Returns:
        scaledImage: Image set to the default scale
    """
    height, width = image.shape[:2]
    if height < res[0] | width < res[1]:
        scaledImage = cv.resize(image, res, interpolation=cv.INTER_AREA)
    else:
        scaledImage = cv.resize(image, res, interpolation=cv.INTER_LINEAR)
    return scaledImage


cv.imshow("Camera Feed", reScaleImage(img))
k = cv.waitKey(0)
