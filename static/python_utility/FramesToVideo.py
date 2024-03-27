import cv2

input_folder = '/Users/a20/Documents/spring2024/4527_cv/projects/project4/static/output_frames'
video_fps = 60
width, height = 2248, 1392
output_video_path = '/Users/a20/Documents/spring2024/4527_cv/projects/project4/static/driving_labeled.mp4'

out = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*'X264'), video_fps, (width, height))

frame_count = 3242

for i in range(frame_count):
    frame_path = f"{input_folder}/frame{i}.jpg"
    frame = cv2.imread(frame_path)
    out.write(frame)

out.release()
