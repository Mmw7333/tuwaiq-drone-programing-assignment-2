from djitellopy import Tello
import cv2
from cvzone.cvzone import FaceDetectionModule

detector = FaceDetectionModule()
me = Tello()

me.connect()
me.streamon()

me.takeoff()
me.move_up(60)
me.rotate_clockwise(45)
me.move_forward(30)
while True:
    img = me.get_frame_read().frame
    img, bboxs = detector.findFaces(img, draw=True)
    cv2.imshow("Image", img)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()

me.land()