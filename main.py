import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

def run_hand_tracking():
    cam=cv2.VideoCapture(index=0)
    #initializing camera
    with mp_hands.Hands(
        model_complexity=0,
        max_num_hands=2,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5,
    ) as hands:
        #frame capture loop
        while cam.isOpened():
            sucess,frame=cam.read()
            if not sucess:
                print('empty frame.')
                continue
            #converting color format:
            frame_rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            results=hands.process(frame_rgb)
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        image=frame,
                        landmark_list=hand_landmarks,
                        connections=mp_hands.HAND_CONNECTIONS,
                        landmark_drawing_spec=mp_drawing_styles.get_default_hand_landmarks_style(),
                        connection_drawing_spec=mp_drawing_styles.get_default_hand_connections_style(),
                    )

            #display window and flip frame
            cv2.imshow('Hand tracking',cv2.flip(frame,1))
            #quitting
            if cv2.waitKey(1) & 0xFF ==ord('q'):
                break
if __name__=='__main__':
    run_hand_tracking()