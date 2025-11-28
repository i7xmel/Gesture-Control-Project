import cv2
import numpy as np
import HandTrackingModule as htm
import pyautogui
import time

# Screen width and height
screenWidth, screenHeight = pyautogui.size()

# Camera settings
wCam, hCam = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0

detector = htm.handDetector(detectionCon=0.75, maxHands=1)

# Smoothening factor
smoothening = 5
prevX, prevY = 0, 0
currX, currY = 0, 0

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if lmList:
        x1, y1 = lmList[8][1:]  # Index finger tip
        x2, y2 = lmList[12][1:]  # Middle finger tip
        x4, y4 = lmList[20][1:]  # Little finger tip

        # Check which fingers are up
        fingers = []
        # Thumb
        if lmList[4][1] > lmList[3][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        # Fingers
        for id in [8, 12, 16, 20]:
            if lmList[id][2] < lmList[id - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        # Moving the cursor when only the index finger is up
        if fingers[1] == 1 and fingers[2] == 0 and fingers[4] == 0:
            x3 = np.interp(x1, (75, wCam - 75), (0, screenWidth))
            y3 = np.interp(y1, (75, hCam - 75), (0, screenHeight))

            currX = prevX + (x3 - prevX) / smoothening
            currY = prevY + (y3 - prevY) / smoothening

            pyautogui.moveTo(screenWidth - currX, currY)
            prevX, prevY = currX, currY

        # Left click when both the index finger and middle finger are up
        if fingers[1] == 1 and fingers[2] == 1 and fingers[4] == 0:
            length = np.hypot(x2 - x1, y2 - y1)
            if length < 40:
                pyautogui.click()

        # Right click when both the index finger and little finger are up
        if fingers[1] == 1 and fingers[4] == 1 and fingers[2] == 0:
            length = np.hypot(x4 - x1, y4 - y1)
            if length < 50:
                pyautogui.click(button='right')

    # Calculate FPS for performance monitoring
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
