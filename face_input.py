import cv2
import os

def face_input(face_name):
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)  # set video width
    cam.set(4, 480)  # set video height

    face_detector = cv2.CascadeClassifier('database/haar/haarcascade_frontalface_default.xml')


    # define the name of the directory to be created
    path = "database/img/"+str(face_name)
    os.makedirs(path)

    print("\n [INFO] Initializing face capture. Look the camera and wait ...")
    # Initialize individual sampling face count
    count = 0
    file = open('database/userid.txt','r')
    face_id = file.read()
    file.close()
    
    pt = 'database/name/'+str(face_id)+'.txt'
    file1 = open(pt,'w')
    file1.write(str(face_name))
    file1.close()
    
    file2 = open('database/userid.txt','w')
    x = int(face_id)+1
    file2.write(str(x))
    file2.close()
    
    while (True):
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray,1.3,5)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            count += 1

            # Save the captured image into the datasets folder
            cv2.imwrite(str(path) + "/"+str(face_name)+"." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y + h, x:x + w])

            cv2.imshow('image', img)

        k = cv2.waitKey(100) & 0xff  # Press 'ESC' for exiting video
        if k == 27:
            break
        elif count >= 10:  # Take 10 face sample and stop video
            break

    # Do a bit of cleanup
    print("\n [INFO] Exiting Program and cleanup stuff")
    cam.release()
    del cam
    cv2.destroyAllWindows()
