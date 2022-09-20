import keyboard
# import pymem
# import time 
import autopy
import cv2
import mediapipe as mp
from offsets import *

# Отслеживаем запущенный процесс под названием csgo.exe
# _process = pymem.Pymem("csgo.exe")
# _client = pymem.process.module_from_name(_process.process_handle, "client.dll").lpBaseOfDll

cap = cv2.VideoCapture(0)

width, height = autopy.screen.size()

hands = mp.solutions.hands.Hands(static_image_mode=False,
                        max_num_hands=2,
                        min_tracking_confidence=0.5,
                        min_detection_confidence=0.60)

mpDraw = mp.solutions.drawing_utils

def main():
    while True:
        _, img = cap.read()
        result = hands.process(img)
        if result.multi_hand_landmarks:
            for id, lm in enumerate(result.multi_hand_landmarks[0].landmark):
                h, w, _ = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                cv2.circle(img, (cx, cy), 3, (255, 0, 255))
                if id == 8:
                    cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
                    autopy.mouse.move(cx * width / w, cy * height / h)

                    # Передаем стрельбу. Можно настроить на любой другой триггер ...
                    # attack = _client + dwForceAttack
                    # _process.write_int(attack, 5)
                    # time.sleep(0.01)
                    # _process.write_int(attack, 4)

            mpDraw.draw_landmarks(img, result.multi_hand_landmarks[0], mp.solutions.hands.HAND_CONNECTIONS)
        rotated = cv2.rotate(img, cv2.ROTATE_180)
        cv2.imshow('Eldar Jivi, brats', rotated)
        cv2.waitKey(1)
        if keyboard.is_pressed('esc'):
            break

if __name__ == "__main__":
    main()