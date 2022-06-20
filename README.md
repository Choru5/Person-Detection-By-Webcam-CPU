# Person-Detection-by-Webcam

Requirements:
 - A PC (no GPU required)
 - A smartphone / webcam
 
 What it is:
 -  This is a machine learning model that has been trained to detect people and notify you.
 
 Installation Instructions:
 
 - Download this repository.
 - Make sure you have Python installed
 - Open cmd and cd into this repository.
 - Install required packages by running ``` pip install -r requirements.txt ```
 - Download DroidCam Client on your PC and the DroidCam app on your phone (if using a webcam ignore this)

 Customizable Settings:
 ```
 notifTitle = "Warning" # This will change the title of the notification being displayed
 notifContent = "Person detected!" # This will change the content of the notification being displayed

 visuals = True # This will toggle the visiblity of the camera feed
 
 IN = 1  # This will toggle the webcam source (0 = normal webcam, 1 = smartphone DroidCam webcam)
```

 How to use:
 
 - Open cmd and cd into this repository.
 - Run the command ``` python pythondetector.py ``` to start the program, make sure you have DroidCam Client open and are connected to your phones DroidCam via Wi-Fi or USB (if using a webcam ignore this)
