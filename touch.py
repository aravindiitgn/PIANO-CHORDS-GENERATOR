import pyrealsense2 as rs
import numpy as np
import cv2

# Initialize camera
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
pipeline.start(config)

try:
    while True:
        # Wait for a frame
        frames = pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        if not depth_frame:
            continue

        # Convert depth frame to numpy array
        depth_image = np.asanyarray(depth_frame.get_data())

        # Apply a colormap for visualization
        depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)

        # Find the minimum depth value to detect touch
        min_depth = np.min(depth_image)

        # Set a threshold to identify touches (adjust as necessary)
        touch_threshold = 500  # mm

        # Detect touches
        touch_points = np.where(depth_image < touch_threshold)
        
        for y, x in zip(touch_points[0], touch_points[1]):
            cv2.circle(depth_colormap, (x, y), 5, (0, 0, 255), -1)

        # Show the result
        cv2.imshow('Depth', depth_colormap)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    # Stop the pipeline
    pipeline.stop()
    cv2.destroyAllWindows()