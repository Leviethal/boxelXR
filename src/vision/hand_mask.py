import numpy as np
import cv2

def generate_hand_mask(frame, hand_landmarks, img_w, img_h):
    mask = np.zeros((img_h, img_w), dtype=np.uint8)

    for hand in hand_landmarks:
        points = []
        for lm in hand.landmark:
            x = int(lm.x * img_w)
            y = int(lm.y * img_h)
            points.append([x, y])

        hull = cv2.convexHull(np.array(points))
        cv2.fillConvexPoly(mask, hull, 255)

    return mask
