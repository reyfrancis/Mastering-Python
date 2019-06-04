'''
Let’s summarize the five files in the root directory:

extract_embeddings.py : We’ll review this file in Step #1 which is responsible for using a deep learning feature extractor to 
generate a 128-D vector describing a face. All faces in our dataset will be passed through the neural network to generate 
embeddings.

openface_nn4.small2.v1.t7 : A Torch deep learning model which produces the 128-D facial embeddings. We’ll be using this deep 
learning model in Steps #1, #2, and #3 as well as the Bonus section.

train_model.py : Our Linear SVM model will be trained by this script in Step #2. We’ll detect faces, extract embeddings, and fit 
our SVM model to the embeddings data.

recognize.py : In Step #3 and we’ll recognize faces in images. We’ll detect faces, extract embeddings, and query our SVM model 
to determine who is in an image. We’ll draw boxes around faces and annotate each box with a name.

recognize_video.py : Our Bonus section describes how to recognize who is in frames of a video stream just as we did in Step #3 
on static images.

Let’s move on to the first step!
'''

#Import libraries
from imutils import paths

'''
Instead of calling warpAffines to translate images, it is a convenience to use imutils.

Translation is the shifting of an image in either the x or y direction. To translate an image in OpenCV you need to supply the 
(x, y)-shift, denoted as (tx, ty) to construct the translation matrix M: 
 
M = | 1 0 t_x |
	| 0 1 t_y |

And from there, you would need to apply the cv2.warpAffine  function.
Instead of manually constructing the translation matrix M and calling cv2.warpAffine, you can simply make a call to translate 
function of imutils.

Example:
# translate the image x=25 pixels to the right and y=75 pixels up
translated = imutils.translate(workspace, 25, -75)
'''

import numpy as np
import argparse   # Use cmd interface with python
import imutils
import pickle
import cv2
import os

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--dataset", required=True,
	help="path to input directory of faces + images")
ap.add_argument("-e", "--embeddings", required=True,
	help="path to output serialized db of facial embeddings")
ap.add_argument("-d", "--detector", required=True,
	help="path to OpenCV's deep learning face detector")
ap.add_argument("-m", "--embedding-model", required=True,
	help="path to OpenCV's deep learning face embedding model")
ap.add_argument("-c", "--confidence", type=float, default=0.5,
	help="minimum probability to filter weak detections")
args = vars(ap.parse_args())

'''
Next, we process our command line arguments:

--dataset : The path to our input dataset of face images.
--embeddings : The path to our output embeddings file. Our script will compute face embeddings which we’ll serialize to disk.
--detector : Path to OpenCV’s Caffe-based deep learning face detector used to actually localize the faces in the images.
--embedding-model : Path to the OpenCV deep learning Torch embedding model. This model will allow us to extract a 128-D facial embedding vector.
--confidence : Optional threshold for filtering week face detections.
'''

# load our serialized face detector from disk
print("[INFO] loading face detector...")
protoPath = os.path.sep.join([args["detector"], "deploy.prototxt"])   # The path to OpenCV's deep learning face detector is added 
																	  # with 'deploy.prototxt' at the end
modelPath = os.path.sep.join([args["detector"],						  # The path to OpenCV's deep learning face detector is added 
	"res10_300x300_ssd_iter_140000.caffemodel"])					  # with 'res10_300x300_ssd_iter_140000.caffemodel' at the end
detector = cv2.dnn.readNetFromCaffe(protoPath, modelPath)
 
# load our serialized face embedding model from disk
print("[INFO] loading face recognizer...")
embedder = cv2.dnn.readNetFromTorch(args["embedding_model"])	      # path to output serialized db of facial embeddings is loaded into
																	  # into Deep Neural Network

# Grab the paths to the input images in our dataset
print("[INFO] quantifying faces...")
imagePaths = list(paths.list_images(args["dataset"]))   # Create list of the iamges from the path of directory of faces + images.
 														# The imagePaths  list, built on Line 37, contains the path to each image 
 														# in the dataset. I’ve made this easy via my imutils  function, paths.list_images
# Initialize our lists of extracted facial embeddings and
# Corresponding people names
knownEmbeddings = []
knownNames = []
 
# Initialize the total number of faces processed
total = 0  

# loop over the image paths
for (i, imagePath) in enumerate(imagePaths):
	# extract the person name from the image path
	print("[INFO] processing image {}/{}".format(i + 1,
		len(imagePaths)))
	name = imagePath.split(os.path.sep)[-2]
 
	# load the image, resize it to have a width of 600 pixels (while
	# maintaining the aspect ratio), and then grab the image
	# dimensions
	image = cv2.imread(imagePath)
	image = imutils.resize(image, width=600)
	(h, w) = image.shape[:2]