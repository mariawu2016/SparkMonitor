# Standard imports
import cv2
import numpy as np
# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()
params.blobColor=255
# Change thresholds
params.minThreshold = 60
params.maxThreshold = 100
# Filter by Area.
params.filterByArea = True
params.minArea = 2
params.maxArea=200
# Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.1
# Filter by Convexity
params.filterByConvexity = True
params.minConvexity = 0.87
# Filter by Inertia
params.filterByInertia = True
params.minInertiaRatio = 0.01
# Create a detector with the parameters
ver = (cv2.__version__).split('.')
#if int(ver[0]) < 3 :
#    detector = cv2.SimpleBlobDetector(params)
#else :
detector = cv2.SimpleBlobDetector_create(params)

# Read image
im = cv2.imread("fire2.jpg", 0)
#im = cv2.imread("6869.jpg", 0)
roi = im[100:1720, 0:1080]

# Set up the detector with default parameters.
#detector = cv2.SimpleBlobDetector()
# Detect blobs.
keypoints = detector.detect(roi)
# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(roi, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

#im[100:1820, 0:1080] = cv2.bitwise_and(im_with_keypoints,im,)
# Show keypoint
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)