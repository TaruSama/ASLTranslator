import cv2
import mediapipe as mp
import os

def record(output_dir):
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands

    # Initialize video capture
    cap = cv2.VideoCapture(0)

    # Initialize MediaPipe Hands
    with mp_hands.Hands(min_detection_confidence=0.75, min_tracking_confidence=0.75) as hands:
        is_recording = False
        recording_count = 0
        no_hand_count = 0
        recording_delay = 20 # Number of frames (1/2 second at 30 fps) to wait before stopping recording

        # Specify directory to save output videos

        os.makedirs(output_dir, exist_ok=True)

        while True:
            # Read frame from video capture
            ret, frame = cap.read()

            # Convert frame to RGB for use with MediaPipe
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Process image with MediaPipe Hands
            results = hands.process(image)

            # Check if hand is detected
            if results.multi_hand_landmarks:
                # Draw landmarks on image
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Get the landmark of the index fingertip
                index_finger_tip_landmark = results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

                # Get the dimensions of the camera window
                height, width, _ = image.shape

                # Calculate the boundary for the corner
                corner_boundary = int(min(height, width) * 0.25)

                # Check if the fingertip is in the top-left corner
                if index_finger_tip_landmark.x * width < corner_boundary and index_finger_tip_landmark.y * height < corner_boundary:
                    # Stop recording if currently recording
                    if is_recording:
                        is_recording = False
                        out.release()
                        print(f'Stopped recording output{recording_count}.mp4')
                        no_hand_count = 0

                    # Exit the program
                    break

                # Start recording if not already recording
                if not is_recording:
                    is_recording = True
                    recording_count += 1
                    output_path = os.path.join(output_dir, f'output{recording_count}.mp4')
                    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), 30, (frame.shape[1], frame.shape[0]))
                    print(f'Started recording {output_path}')

            # Stop recording if no hand detected for recording_delay frames (1/2 second at 30 fps)
            elif is_recording:
                no_hand_count += 1
                if no_hand_count >= recording_delay:
                    is_recording = False
                    out.release()
                    print(f'Stopped recording output{recording_count}.mp4')
                    no_hand_count = 0

            # Write frame to output video if recording
            if is_recording:
                out.write(frame)

            # Display image
            cv2.imshow('Hand Tracking', image)

            # Exit if 'q' key is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    # Release video capture and destroy windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    output_dir = '/home/tester/finalProject/videos'
    record(output_dir)
