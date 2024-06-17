import cv2
import numpy as np
import pyrealsense2 as rs
import mediapipe as mp

pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
pipeline.start(config)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

def get_touch_coordinates(image_width, image_height, landmark):
    x = int(landmark.x * image_width)
    y = int(landmark.y * image_height)
    return x, y

try:
    while True:
        frames = pipeline.wait_for_frames()
        color_frame = frames.get_color_frame()
        depth_frame = frames.get_depth_frame()
        if not color_frame or not depth_frame:
            continue

        color_image = np.asanyarray(color_frame.get_data())
        depth_image = np.asanyarray(depth_frame.get_data())
        image_height, image_width, _ = color_image.shape

        results = hands.process(cv2.cvtColor(color_image, cv2.COLOR_BGR2RGB))

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(color_image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                x, y = get_touch_coordinates(image_width, image_height, index_finger_tip)
                
                depth = depth_frame.get_distance(x, y)
                print(f"Index finger tip coordinates: ({x}, {y}), Depth: {depth:.2f} meters")

                cv2.circle(color_image, (x, y), 10, (0, 255, 0), cv2.FILLED)

        cv2.imshow('RealSense', color_image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    pipeline.stop()
    cv2.destroyAllWindows()
