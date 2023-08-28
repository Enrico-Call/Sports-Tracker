import cv2
import numpy as np


def process_video(input_path, output_path, pose_estimator):
    cap = cv2.VideoCapture(input_path)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, 20.0, (640, 480))

    while (cap.isOpened()):
        ret, frame = cap.read()
        if not ret:
            break

        keypoints = pose_estimator(frame)

        # Draw keypoints on the frame (simplified)
        for i, (x, y) in enumerate(keypoints):
            cv2.circle(frame, (int(x), int(y)), 5, (0, 255, 0), -1)

        out.write(frame)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
