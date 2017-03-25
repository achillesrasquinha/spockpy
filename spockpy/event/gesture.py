# imports - compatibility imports
from __future__ import absolute_import

# imports - third-party packages
import math
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

def _get_eucledian_distance(a, b):
    distance = math.sqrt( (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

    return distance

def _get_defects_count(array, contour, defects, verbose = False):
    ndefects = 0
    
    for i in range(defects.shape[0]):
        s,e,f,_ = defects[i,0]
        beg     = tuple(contour[s][0])
        end     = tuple(contour[e][0])
        far     = tuple(contour[f][0])
        a       = _get_eucledian_distance(beg, end)
        b       = _get_eucledian_distance(beg, far)
        c       = _get_eucledian_distance(end, far)
        angle   = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)) * 57
            
        if angle <= 90:
            ndefects = ndefects + 1

            if verbose:
                cv2.circle(array, far, 3, _COLOR_RED, -1)

        if verbose:
            cv2.line(array, beg, end, _COLOR_RED, 1)

    return array, ndefects

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
        
    if defects is not None:
        copy, ndefects = _get_defects_count(copy, largecont, defects, verbose = verbose)

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