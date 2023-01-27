# import cv2

# input_rtsp = "tcp://10.0.0.85:5000"
# #input_rtsp = "tcp://10.0.0.230:5001"
# # # input_rtsp = "/dev/video0"

# cap = cv2.VideoCapture(input_rtsp)

# while True:
#     ret, frame = cap.read()
    
#     cv2.imshow('frame', frame)


#     if cv2.waitKey(1) == ord('q'):
#         break
    
# # When everything done, release the capture
# cap.release()
# cv2.destroyAllWindows()

# from https://stackoverflow.com/a/52506614/8941739

import numpy as np
import sys
import cv2
import time
from imutils.video import VideoStream
import datetime

# input_rtsp = "tcp://10.0.0.85:5000"
# input_rtsp = "tcp://10.0.0.230:5001"
# input_rtsp = "/dev/video0"
input_rtsp = "rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mp4"

# start the video stream thread and give the camera sensor time to warmup and feed the buffer
vs = VideoStream(input_rtsp).start()
time.sleep(1.0)
while True:
    frame = vs.read()

    if frame is not None:
        # grab the current timestamp and draw it on the frame
        timestamp = datetime.datetime.now()
        cv2.putText(frame, timestamp.strftime(
            "%A %d %B %Y %I:%M:%S%p"), (10, frame.shape[0] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

        sys.stdout.buffer.write(frame.tobytes())


vs.stop()
