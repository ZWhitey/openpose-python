# Openpose Python

[![Build status](https://ci.appveyor.com/api/projects/status/kjc2uttibxo5b4uo?svg=true)](https://ci.appveyor.com/project/ZWhitey/openpose-python)

Unofficial pre-built [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) packages with cuda for Python.

This package only test on windows 10 with python 3.6 
# Installaion

Prerequisites:

* Python 3.5+
* Numpy
* OpenCV
* Windows x64
* Nvidia GPU

Installaion:

* Python library
    1. Download whl file from [release page](https://github.com/ZWhitey/openpose-python/releases)
    2. Run `pip install WHL_FILE_NAME` to install
* Openpose models  
    1. Clone [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) 
    2. Run `./models/getModels.bat` to download models

# Usage

This code is based on [OpenPose python tutorial 01](https://github.com/CMU-Perceptual-Computing-Lab/openpose/tree/master/examples/tutorial_api_python)
```python
# From Python
# It requires OpenCV installed for Python
import sys
import cv2
import pyopenpose as op

# Custom Params (refer to include/openpose/flags.hpp for more parameters)
params = dict()
params["model_folder"] = "YOUR_MODELS_PATH"

try:
    # Starting OpenPose
    opWrapper = op.WrapperPython()
    opWrapper.configure(params)
    opWrapper.start()

    datum = op.Datum()
    imageToProcess = cv2.imread('YOUR_IMAGE_PATH')
    datum.cvInputData = imageToProcess
    opWrapper.emplaceAndPop([datum])
    print("Body keypoints: \n" + str(datum.poseKeypoints))
    cv2.imshow("OpenPose 1.5.1 - Tutorial Python API", datum.cvOutputData)
    cv2.waitKey(0)
    
except Exception as e:
    print(e)
    sys.exit(-1)
```
More detailed information can be find in [OpenPose Official Repository](https://github.com/CMU-Perceptual-Computing-Lab/openpose)


# Todo

- Support other OS (linux, mac)
- Support OpenCL and CPU version


