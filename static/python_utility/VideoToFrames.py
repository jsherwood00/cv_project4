import cv2

video_path = "/Users/a20/Documents/spring2024/4527_cv/projects/project4/assets/driving.mov"
output_folder = "/Users/a20/Documents/spring2024/4527_cv/projects/project4/assets/frames"
video = cv2.VideoCapture(video_path)

success, frame = video.read()
frame_count = 0
while success:
    output_path = (f"{output_folder}/frame{frame_count}.jpg")
    cv2.imwrite(output_path, frame)
    success, frame = video.read()
    frame_count += 1

