import cv2
import numpy as np

blank = np.zeros((400,400), dtype="uint8")

rectangle = cv2.rectangle(blank.copy(), (30,30), (370,370), 255, -1)

circle = cv2.circle(blank.copy(), (200,200), 200, 255, -1)

cv2.imshow("original rectangle", rectangle)
cv2.imshow("original circle", circle)

#bitwise XOR operator

bitwiseXOR = cv2.bitwise_xor(rectangle, circle)

cv2.imshow("bitwiseXOR", bitwiseXOR)

"""
bitwise XOR operator finds the not common pixel between two images.
"""

cv2.waitKey(0)
cv2.destroyAllWindows()


