import cv2
import numpy as np
import pyrealsense2 as rs
import mediapipe as mp

# Initialize RealSense camera
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
pipeline.start(config)

# Initialize MediaPipe Hand Tracking
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

def get_touch_coordinates(image_width, image_height, landmark):
    x = int(landmark.x * image_width)
    y = int(landmark.y * image_height)
    return x, y

try:
    while True:
        # Get frames from the RealSense camera
        frames = pipeline.wait_for_frames()
        color_frame = frames.get_color_frame()
        if not color_frame:
            continue

        # Convert images to numpy arrays
        color_image = np.asanyarray(color_frame.get_data())
        image_height, image_width, _ = color_image.shape

        # Process image and find hands
        results = hands.process(cv2.cvtColor(color_image, cv2.COLOR_BGR2RGB))

        # Draw hand landmarks and map index finger to touch coordinates
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(color_image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Get coordinates of the index finger tip
                index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                x, y = get_touch_coordinates(image_width, image_height, index_finger_tip)
                print(f"Index finger tip coordinates: ({x}, {y})")

                # Draw a circle at the tip of the index finger
                cv2.circle(color_image, (x, y), 10, (0, 255, 0), cv2.FILLED)

                # Map coordinates to touch screen interaction here

        # Display the image
        cv2.imshow('RealSense', color_image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    pipeline.stop()
    cv2.destroyAllWindows()