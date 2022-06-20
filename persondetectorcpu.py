import cv2
import time
import mediapipe as mp
import numpy as np
from plyer import notification

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

notifTitle = "Warning"  # This will change the title of the notification being displayed
notifContent = "Person detected!"  # This will change the content of the notification being displayed
notifIcon = "warning.ico"

visuals = True  # This will toggle the visiblity of the camera feed

IN = 1  # This will toggle the webcam source (0 = normal webcam, 1 = smartphone DroidCam webcam)

### ---------------------------------------------- Find person function -----------------------------------------------------
def getPerson(checkimage):

    personDetected = False

    checkimage.flags.writeable = False
    checkimage = cv2.cvtColor(checkimage, cv2.COLOR_BGR2RGB)
    results = pose.process(checkimage)
    checkimage.flags.writeable = True
    checkimage = cv2.cvtColor(checkimage, cv2.COLOR_RGB2BGR)

    if results.pose_landmarks:
        personDetected = True
        mp_drawing.draw_landmarks(checkimage, results.pose_landmarks, mp_pose.POSE_CONNECTIONS, mp_drawing_styles.get_default_pose_landmarks_style() )
                    
        return personDetected, checkimage 

    elif not results.pose_landmarks:
        return personDetected, checkimage

### ---------------------------------------------- Notify function -----------------------------------------------------
def notifyMe(title, message, icon):

    notification.notify(
        title = title,
        message = message,
        app_icon = icon, 
        timeout = 10,
    )

### ---------------------------------------------- Main function -----------------------------------------------------
def useWebcam(IN=None):
    canNotify = True

    cap = cv2.VideoCapture(IN)

    pTime = 0
    while cap.isOpened():
        success, img = cap.read()

        if not success:
            print("No image found.")
            continue

        personDetected, displayImg = getPerson(img)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
 
        cv2.putText(displayImg, str(int(fps)), (5, 20), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 1)

        if personDetected == True and canNotify == True:
            notifyMe(notifTitle, notifContent, notifIcon)
            canNotify = False

        elif personDetected == False and canNotify == False:
            canNotify = True         

        if visuals == True:
            cv2.imshow("capture", displayImg) 

        cv2.waitKey(1)

### -------------------  calling the main function-------------------------------

useWebcam(IN)




