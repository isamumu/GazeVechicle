import numpy as np


def shape_to_np(shape):
    # initialize the list of (x, y)-coordinates
    coords = np.zeros((68, 2), dtype=np.float32)

    # loop over the 68 facial landmarks and convert them
    # to a 2-tuple of (x, y)-coordinates
    for ii in range(0, 68):
            coords[ii] = (shape.part(ii).x, shape.part(ii).y)

    # return the list of (x, y)-coordinates
    return coords


def rect_to_bb(rect):
	# take a bounding predicted by dlib and convert it
	# to the format (x, y, w, h) as we would normally do
	# with OpenCV
	x = rect.left()
	y = rect.top()
	w = rect.right() - x
	h = rect.bottom() - y
 
	# return a tuple of (x, y, w, h)
	return (x, y, w, h)