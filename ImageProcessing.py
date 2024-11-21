### CANNY, DISTANCE CALCULATION, IMAGE PROCESSING
### SAMUEL WANG


import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from PIL import Image


def CannyProcess(image) -> list:
    '''
    Takes an image, processes it, and returns the edges
    :param image: the image to be processed by Canny
    :return: edges from cv.Canny
    '''
    # Reading in the Image
    src = cv.imread(image)

    # Convert to HSV
    img_hsv = cv.cvtColor(src, cv.COLOR_BGR2HSV)

    ## SHIFT HUE SPACE to decrease fuzziness on edges
    shift = 90
    img_hsv[:, :, 0] = (img_hsv[:, :, 0].astype(int) + shift) % 180

    # Bounds for color selection CHANGE THIS TO CHANGE WHAT COLOR IS PICKED UP
    lower_bound = np.array([0,90,0])
    upper_bound = np.array([255,255,255])

    # Create a mask around the color
    mask = cv.inRange(img_hsv, lower_bound, upper_bound)
    img_iso = cv.bitwise_and(src, src, mask=mask)

    # Dilation to close contours, also slightly expands the exact edge of shape
    # BUT expansion should be consistent from image to image
    kernel = np.ones((15,15), np.uint8)
    dilation = cv.dilate(mask,kernel,iterations = 1)
    src_processed = cv.blur(dilation, (3,3))

    # Canny Edge Detection
    threshold1 = 90
    threshold2 = 180
    edges = cv.Canny(src_processed, threshold1, threshold2)

    return edges


def createContours(edges: list, drawContours = False) -> list:
    '''
    Creates contours from Canny edges (hopefully closes the edges)
    :param edges: edges from cv.Canny()
    :param drawContours: whether or not to show the drawn contours. Defaults to False.
    :return: contours
    '''
    contours, _ = cv.findContours(edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    # Note: RETR_EXTERNAL tries to only return an outermost contour (ex. if a contour is inside another contour, it is ignored)
    # Note: CHAIN_APPROX_NONE just means we want ALL points detected back instead of simplifying

    if drawContours:
        drawing = np.zeros((edges.shape[0], edges.shape[1], 3), dtype=np.uint8)
        for i in range(len(contours)):
            cv.drawContours(drawing, contours, i, (255, 255, 255))
        # Window
        cv.namedWindow("Contours", cv.WINDOW_NORMAL)
        cv.imshow('Contours', drawing)
        cv.waitKey()

    return contours


def compareBoundingEdges(contours1: list, contours2: list, cutHeight: float, showCutImage = False) -> dict():
    '''
    Compares the two images' bounding boxes
    :param contours1: List of contours for the first image
    :param contours2: List of contours for the second image
    :param cutHeight: Data above this height will be ignored
    :return: A dictionary containing the number of pixel difference between the corners of each bounding box for each image
    '''
    # First: convert to x, y coordinates
    x1, y1, x2, y2 = list(), list(), list(), list()
    for i in contours1:
        for j in i:
            row, col = j[0]
            if col > cutHeight:
                x1.append(row)
                y1.append(-1 * col)

    for i in contours2:
        for j in i:
            row, col = j[0]
            if col > cutHeight:
                x2.append(row)
                y2.append(-1 * col)

    if showCutImage:
        plt.scatter(x1, y1, s = 1, color = 'red')
        plt.scatter(x2, y2, s = 1, color = 'blue')
        plt.title('Cut Image'), plt.xticks([]), plt.yticks([])
        plt.xlim(0, 2500)
        plt.ylim(-3000, 0)
        plt.show()

    # Find bounding box coordinates
    x1min, x1max, y1min, y1max = min(x1), max(x1), min(y1), max(y1)
    x2min, x2max, y2min, y2max = min(x2), max(x2), min(y2), max(y2)

    print(x1min, x1max, y1min, y1max)
    print(x2min, x2max, y2min, y2max)

    # Find differences
    differences = {'Leftmost Point' : x1min - x2min, 'Bottommost Point': y1min - y2min,
                   'Rightmost Point' : x1max - x2max, 'Topmost Point' : y1max - y2max}

    return differences


def plotEdgesonImage(image, edges):
    '''
    Compares the detected edges to the source image for troubleshooting
    :param image: source image
    :param edges: edges from Canny
    :return:
    '''
    plt.subplot(121), plt.imshow(src) # Note: colors swapped b/c OpenCV stores colors in BGR, but matplotlib does in RGB
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(edges)
    plt.title('Edges Image'), plt.xticks([]), plt.yticks([])
    plt.show()


if __name__ == "__main__":
    # Example of how to run these functions
    edges1 = CannyProcess('IMG_8336.jpg')
    edges2 = CannyProcess('IMGB.jpg')

    contours1 = createContours(edges1)
    contours2 = createContours(edges2)

    differences = compareBoundingEdges(contours1, contours2, cutHeight = 2000, showCutImage = True)

    print(differences)