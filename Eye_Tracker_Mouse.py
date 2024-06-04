import cv2
import mediapipe as mp
import pyautogui
cam=cv2.VideoCapture(0)
face_mesh=mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
s_w,s_h=pyautogui.size()
while True:
    _,frame=cam.read()
    frame=cv2.flip(frame,1)
    rgb_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output=face_mesh.process(rgb_frame)
    landmark_point=output.multi_face_landmarks
    frame_h,frame_w,_ = frame.shape
    if landmark_point:
        landmarks=landmark_point[0].landmark
        for id,landmark in enumerate(landmarks[474:478]):
            #print(len(landmarks[474:478]))
            x=int(landmark.x *frame_w)
            y=int(landmark.y*frame_h)
            cv2.circle(frame,(x,y),3,(0,255,0))
            #print(x,y)
            if id ==2:
                s_x=1.2*s_w/frame_w *x
                s_y=1.2*s_h/frame_h *y
                pyautogui.moveTo(s_x,s_y)
        left = [landmarks[145],landmarks[159]]
        for landmark in left:
            x=int(landmark.x *frame_w)
            y=int(landmark.y*frame_h)
            cv2.circle(frame,(x,y),3,(0,255,255))
        print(left[0].y- left[1].y)
        if (left[0].y- left[1].y)<0.004:
            #print("click")
            pyautogui.click()
            pyautogui.sleep(1)
    cv2.imshow('Eye Mouse',frame)
    cv2.waitKey(1)