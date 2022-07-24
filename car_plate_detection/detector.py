# Module Installer

import pip

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

# Installing modules

install("common")
install("numpy")
install("opencv-python")
install("matplotlib")
install("paddlepaddle")
install("https://paddleocr.bj.bcebos.com/whl/layoutparser-0.0.0-py3-none-any.whl")

# Importing modules

import cv2

from matplotlib import pyplot as plt

# Read Image, Grayscale and Blur

for i in range(0, 4):
  img = cv2.imread(f"static/test.jpg")
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  # plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))
  
  bfilter = cv2.bilateralFilter(gray, 100, 100, 100)
  edged = cv2.Canny(bfilter, 30, 200)
  # plt.imshow(cv2.cvtColor(edged, cv2.COLOR_BGR2RGB))

  ocr = paddleocr.PaddleOCR(use_angle_cls=True, lang='en')
  result = ocr.ocr(edged, cls=True)

  for line in result:
      print(line[1][0])

# Applying filters to find edges for localization

bfilter = cv2.bilateralFilter(gray, 100, 100, 100)
edged = cv2.Canny(bfilter, 30, 200)
plt.imshow(cv2.cvtColor(edged, cv2.COLOR_BGR2RGB))


# Image To Text

ocr = paddleocr.PaddleOCR(use_angle_cls=True, lang='en')
result = ocr.ocr(edged, cls=True)

for line in result:
    print(line[1][0])
