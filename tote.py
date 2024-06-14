import cv2
import numpy as np

def process_frame(frame):
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Perform edge detection
    edges = cv2.Canny(blurred, 50, 150)

    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours and bounding boxes
    output = frame.copy()
    for contour in contours:
        # Get the bounding box
        x, y, w, h = cv2.boundingRect(contour)

        # Filter out small or non-rectangular contours
        if w > 50 and h > 50 and w < frame.shape[1] and h < frame.shape[0]:  # These thresholds can be adjusted
            cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    return output

# Capture video from the camera
cap = cv2.VideoCapture(0)  # Use the appropriate camera index

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    # Read a frame from the camera
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    # Process the frame
    output = process_frame(frame)

    # Display the result
    cv2.imshow('Detected Separations', output)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()