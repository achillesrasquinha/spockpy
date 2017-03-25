# imports - compatibility imports
from __future__ import absolute_import

# imports - third-party packages
import numpy as np
import cv2

# imports - module imports
from spockpy.event import Event
from spockpy._util import (
    _to_grayscale,
    _get_opencv_version,
    _mount_roi,
	_to_grayscale,
	_get_opencv_version,
	_mount_roi
)

_DEFAULT_GAUSSIAN_BLUR_KERNEL = (35, 35)
_DEFAULT_THRESHOLD_TYPE       = cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU

_COLOR_RED   = (0, 0, 255)
_COLOR_GREEN = (0, 255, 0)
_COLOR_GREEN = (0, 255, 0)

def _get_contours(array):
    major = _get_opencv_version()[0]

    if major == 3:
        _, contours, _ = cv2.findContours(array, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    else:
        _, contours    = cv2.findContours(array, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    return contours

def _draw_contours(array, *args, **kwargs):
    cv2.drawContours(array, *args, **kwargs)

def _get_defects_count(cnt, defects):
    ndefects = 0

    # for i in range(defects.shape[0]):
    #   b,e,f,_  = defects[i, 0]
    #   beg      = np.array(contour[b][0])
    #   end      = np.array(contour[e][0])
    #   far      = np.array(contour[f][0])
    #   x        = np.linalg.norm(end - beg)
    #   y        = np.linalg.norm(far - beg)
    #   z        = np.linalg.norm(end - far)
    #   angle    = np.arccos((np.power(y, 2) + np.power(z, 2) - np.power(x, 2)) / (2 * y * z)) * 57
    #   ndefects = (ndefects + 1) if angle <= 90 else ndefects
    import math
    for i in range(defects.shape[0]):
        s,e,f,d = defects[i,0]
        start = tuple(cnt[s][0])
        end = tuple(cnt[e][0])
        far = tuple(cnt[f][0])
        a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
        b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
        c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)
        angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 57
        if angle <= 90:
            ndefects += 1
            #cv2.circle(array,far,1,[0,0,255],-1)
        #dist = cv2.pointPolygonTest(cnt,far,True)
        #cv2.line(array,start,end,[0,255,0],2)
        #cv2.circle(crop_img,far,5,[0,0,255],-1)
    return ndefects


def detect(array, verbose = False):
    event      = Event(Event.NONE)

    copy       = array.copy()

    gray       = _to_grayscale(array)
    blur       = cv2.GaussianBlur(gray, ksize = _DEFAULT_GAUSSIAN_BLUR_KERNEL, sigmaX = 0)
    _, thresh  = cv2.threshold(blur, 127, 255, _DEFAULT_THRESHOLD_TYPE)

    if verbose:
        cv2.imshow('spockpy.HoverPad.roi.threshold', thresh)

    contours   = _get_contours(thresh.copy())
    largecont  = max(contours, key = lambda contour: cv2.contourArea(contour))

    if verbose:
        roi  = cv2.boundingRect(largecont)
        copy = _mount_roi(copy, roi, color = _COLOR_RED)

    convexHull = cv2.convexHull(largecont)

    if verbose:
        _draw_contours(copy, contours    ,-1, _COLOR_RED  , 0)
        _draw_contours(copy, [largecont] , 0, _COLOR_GREEN, 0)
        _draw_contours(copy, [convexHull], 0, _COLOR_GREEN, 0)

    hull           = cv2.convexHull(largecont, returnPoints = False)
    defects        = cv2.convexityDefects(largecont, hull)
    ndefects       = _get_defects_count(largecont, defects)

    if   ndefects == 0:
        # TODO: check for a single finger.
        event.setType(Event.ROCK)
    elif ndefects == 1:
        # TODO: check for an Event.LIZARD
        event.setType(Event.SCISSOR)
    elif ndefects == 2:
        event.setType(Event.SPOCK)
    elif ndefects == 4:
        event.setType(Event.PAPER)

    if verbose:
        cv2.imshow('spockpy.HoverPad.roi', copy)

	major = _get_opencv_version()[0]

	if major == 3:
		_, contours, _ = cv2.findContours(array, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
	else:
		_, contours    = cv2.findContours(array, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

	return contours

def _draw_contours(array, *args, **kwargs):
	cv2.drawContours(array, *args, **kwargs)

def _get_defects_count(contour, defects):
	ndefects = 0

	for i in range(defects.shape[0]):
		b,e,f,_  = defects[i, 0]
		beg      = np.array(contour[b][0])
		end      = np.array(contour[e][0])
		far      = np.array(contour[f][0])
		x        = np.linalg.norm(end - beg)
		y        = np.linalg.norm(far - beg)
		z        = np.linalg.norm(end - far)
		angle    = np.arccos((np.power(y, 2) + np.power(z, 2) - np.power(x, 2)) / (2 * y * z)) * 57
		ndefects = (ndefects + 1) if angle <= 90 else ndefects

	return ndefects


def detect(array, verbose = False):
	event      = Event(Event.NONE)

	copy       = array.copy()

	gray       = _to_grayscale(array)
	blur       = cv2.GaussianBlur(gray, ksize = _DEFAULT_GAUSSIAN_BLUR_KERNEL, sigmaX = 0)
	_, thresh  = cv2.threshold(blur, 127, 255, _DEFAULT_THRESHOLD_TYPE)

	if verbose:
		cv2.imshow('spockpy.HoverPad.roi.threshold', thresh)

	contours   = _get_contours(thresh.copy())
	largecont  = max(contours, key = lambda contour: cv2.contourArea(contour))

	if verbose:
		roi  = cv2.boundingRect(largecont)
		copy = _mount_roi(copy, roi, color = _COLOR_RED)

	convexHull = cv2.convexHull(largecont)

	if verbose:
		_draw_contours(copy, contours    ,-1, _COLOR_RED  , 0)
		_draw_contours(copy, [largecont] , 0, _COLOR_GREEN, 0)
		_draw_contours(copy, [convexHull], 0, _COLOR_GREEN, 0)

	hull           = cv2.convexHull(largecont, returnPoints = False)
	defects        = cv2.convexityDefects(largecont, hull)
	ndefects       = _get_defects_count(largecont, defects)

	if   ndefects == 0:
		# TODO: check for a single finger.
		event.setType(Event.ROCK)
	elif ndefects == 1:
		# TODO: check for an Event.LIZARD
		event.setType(Event.SCISSOR)
	elif ndefects == 2:
		event.setType(Event.SPOCK)
	elif ndefects == 4:
		event.setType(Event.PAPER)

	if verbose:
		cv2.imshow('spockpy.HoverPad.roi', copy)

	return event