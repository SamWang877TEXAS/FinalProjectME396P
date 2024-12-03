# 3D Printing - Warping and Shedding Detection
Detect Warping on 3D Prints Using OpenCV!
Members: Samuel, Basel, Harshin

Welcome to our Final Project for ME 396P. In this README, we will briefly go over how to set up and use our code.

# Installation and Use
There are three main Python files to use and edit in order to run our project. They are designed to be able to be used independently for ease of adaptation. The first is Printer_Communications which leverages the package requests in order to communicate with the 3D printer. Since this project was designed specifically to work with Dr. Sha's lab, this Communications file is designed to run with the AMBot printers found in the lab. As a result, it may require modification for other printer types.

To install requests, simply use "pip install" if not already included in your Python installation.

The second is Image_Processing.py. This contains several functions used to actually detect the edges of each 3D print and compare the resultant edges. This is pretty heavily commented, and it is essentially a utility class (file of functions) that can be called by other Python files. Here, we can modify the target color, detection algorithm. Several are provided, though I highly recommend closestPointComparison. This method compares each point from one image to its closest on the other for any out-of-bound points. There is also a simple bounding box and kNN approach, but both of these tend to have worse results. There are also included functions to determine the maximum and minimum height of an image in order to determine at what point to truncate the image. This is because we only want to compare points that are already present in an older image/earlier in the print, otherwise, we would be comparing new layers to nothing!

This file leverages pillow, openCV, sklearn, matplotlib, and numpy. These can all be installed using pip install.

The final file is app.py. This is what actually brings all the code together. This specific file is targeted towards an Intel RealSense Camera and the AMBots printer. This file calls the Image_Processing functions and Printer_Communication functions in order to tell the print to stop when an error is detected. Modification may be needed in order to communicate with a different camera or 3D printer, but these files should be able to give you a good template for any 3D printing system.

Our version of app.py leverages os, time, openCV, and pyrealsense2. Note that pyrealsense2 is a package specifically meant to work with Intel's cameras. This is a great package as it is already in Python, making working with it easier. A different package may need to be utilized for a different camera system.

# Example Images
Note that we provided several example images from our testing. To actually use this with a printer, you will need to run app.py with all the other python files. However, if you only want to see the "computer vision aspect," as in analyzing the contours of an image, you can run the main method in Image_Processing.py as an example. You will need to download the provided images and place them in the same directory as the Python file. Note that this example in the main method, once again, is not meant to actually communicate with a printer--it is used to visualize what is happening during the contour detection process. Feel free to change the HSV bounds to change what colors are detected and the cutHeight/distance_threshold variables to adjust the image output. Details for use are commented in the code. 

# Example of Usage 
Please visit our presentation for an example running the actual project!
https://docs.google.com/presentation/d/1aKQaJyy-p1ypOjL1e1rcOHIyakJbBc2SEEk6Eyx1RUc/edit#slide=id.p

There are also a couple of example images provided in the files.
