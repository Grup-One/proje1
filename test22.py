import cv2
import os
import time


def save_frame_camera_key(dosya, dosyadi, ext='jpg', window_name='frame', device_num = 0):
    cap = cv2.VideoCapture(device_num, cv2.CAP_DSHOW)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    if not cap.isOpened():
        return

    os.makedirs(dosya, exist_ok=True)
    base_path = os.path.join(dosya, dosyadi)

    

    ret, frame = cap.read()
    cv2.imshow(window_name, frame)


    cv2.imwrite('{}.{}'.format(base_path, ext), frame)
    
 

    cv2.destroyWindow(window_name)


save_frame_camera_key('C:/Users/NABER/Desktop/ddene', 'camera_capture')

for i in range(2):
    save_frame_camera_key('C:/Users/NABER/Desktop/ddene', 'camera_capture' + str(i))

    time.sleep(5)