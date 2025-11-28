import tkinter as tk
import customtkinter as ctk
import subprocess
import os
from PIL import Image, ImageTk
import cv2
from threading import Thread
import time

# Paths to your existing Python scripts
video_control_script = 'videocontrol.py'
audio_control_script = 'VolumeHandControl.py'
mouse_tracking_script = 'mouse.py'
rock_paper_scissors_script = 'rock_paper_scissors.py'
gesture_mapping_script = 'gesture_mapping.py'
media_control_script = 'mediacontrol.py'
bouncing_ball_script = 'pythongame.py'

# Placeholder functions for subprocesses
video_process = None
audio_process = None
media_process = None
mouse_process = None
bouncing_ball_process = None
rps_process = None
gesture_mapping_process = None

def start_video_control():
    global video_process
    if video_process is None:
        video_process = subprocess.Popen(['python', video_control_script])
        print("Video control started")

def stop_video_control():
    global video_process
    if video_process is not None:
        video_process.terminate()
        video_process = None
        print("Video control stopped")

def start_audio_control():
    global audio_process
    if audio_process is None:
        audio_process = subprocess.Popen(['python', audio_control_script])
        print("Audio control started")

def stop_audio_control():
    global audio_process
    if audio_process is not None:
        audio_process.terminate()
        audio_process = None
        print("Audio control stopped")

def start_media_control():
    global media_process
    if media_process is None:
        media_process = subprocess.Popen(['python', media_control_script])
        print("Media control started")

def stop_media_control():
    global media_process
    if media_process is not None:
        media_process.terminate()
        media_process = None
        print("Media control stopped")

def start_mouse_tracking():
    global mouse_process
    if mouse_process is None:
        mouse_process = subprocess.Popen(['python', mouse_tracking_script])
        print("Mouse tracking started")

def stop_mouse_tracking():
    global mouse_process
    if mouse_process is not None:
        mouse_process.terminate()
        mouse_process = None
        print("Mouse tracking stopped")

def start_bouncing_ball():
    global bouncing_ball_process
    if bouncing_ball_process is None:
        bouncing_ball_process = subprocess.Popen(['python', bouncing_ball_script])
        print("Bouncing ball started")

def stop_bouncing_ball():
    global bouncing_ball_process
    if bouncing_ball_process is not None:
        bouncing_ball_process.terminate()
        bouncing_ball_process = None
        print("Bouncing ball stopped")

def start_rock_paper_scissors():
    global rps_process
    if rps_process is None:
        rps_process = subprocess.Popen(['python', rock_paper_scissors_script])
        print("Rock Paper Scissors started")

def stop_rock_paper_scissors():
    global rps_process
    if rps_process is not None:
        rps_process.terminate()
        rps_process = None
        print("Rock Paper Scissors stopped")

def start_gesture_mapping():
    global gesture_mapping_process
    if gesture_mapping_process is None:
        gesture_mapping_process = subprocess.Popen(['python', gesture_mapping_script])
        print("Gesture Mapping application started")

def stop_gesture_mapping():
    global gesture_mapping_process
    if gesture_mapping_process is not None:
        gesture_mapping_process.terminate()
        gesture_mapping_process = None
        print("Gesture Mapping application stopped")

def toggle_features():
    if var_video.get():
        start_video_control()
    else:
        stop_video_control()
    
    if var_audio.get():
        start_audio_control()
    else:
        stop_audio_control()

    if var_media.get():
        start_media_control()
    else:
        stop_media_control()

    if var_mouse_tracking.get():
        start_mouse_tracking()
    else:
        stop_mouse_tracking()

    if var_bouncing_ball.get():
        start_bouncing_ball()
    else:
        stop_bouncing_ball()
    
    if var_rps.get():
        start_rock_paper_scissors()
    else:
        stop_rock_paper_scissors()

def enable_all_features():
    var_video.set(1)
    var_audio.set(1)
    var_media.set(1)
    var_mouse_tracking.set(1)
    var_bouncing_ball.set(1)
    var_rps.set(1)
    toggle_features()

def end_program():
    stop_video_control()
    stop_audio_control()
    stop_media_control()
    stop_mouse_tracking()
    stop_bouncing_ball()
    stop_rock_paper_scissors()
    stop_gesture_mapping()  # Ensure gesture mapping is stopped
    root.destroy()

def update_background_video():
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video file.")
        return

    # Get video properties
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    delay = int(1000 / fps)  # Delay in milliseconds

    while True:
        # Loop through video frames
        ret, frame = cap.read()
        if not ret:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Restart video from the beginning
            continue

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (canvas.winfo_width(), canvas.winfo_height()))
        
        photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
        canvas.create_image(0, 0, image=photo, anchor='nw')
        canvas.image = photo

        time.sleep(delay / 1000.0)  # Delay for smooth playback

    cap.release()

# Initialize customtkinter
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("dark-blue")

# Create the main window
root = tk.Tk()
root.title("Gesture Control GUI")
root.state('zoomed')  # Open in full screen

# Create a Canvas widget for background video
canvas = tk.Canvas(root, bg='black', bd=0, highlightthickness=0)
canvas.pack(fill='both', expand=True)

# Start the video in a separate thread
video_path = "GECO.mp4"
video_thread = Thread(target=update_background_video)
video_thread.daemon = True
video_thread.start()

# Load the background image
background_image_path = "2.png"
background_image = Image.open(background_image_path)
background_image = background_image.resize((1200, 1000), Image.LANCZOS)

background_image_tk = ImageTk.PhotoImage(background_image)

# Create a frame to hold the widgets
frame = tk.Frame(root, bg='black')
frame.place(relx=0.5, rely=0.5, anchor='center')

# Set the background image to the frame
frame_background_label = tk.Label(frame, image=background_image_tk)
frame_background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Bring widgets to the front
frame_background_label.lower()

# Load and display the main image in the dialog
image_path = "1.png"
main_image = Image.open(image_path).resize((200, 200))
main_image_tk = ImageTk.PhotoImage(main_image)

image_label = tk.Label(frame, image=main_image_tk, bg='black')
image_label.pack(pady=10)

# Create variables to store the state of each feature
var_video = tk.IntVar()
var_audio = tk.IntVar()
var_media = tk.IntVar()
var_mouse_tracking = tk.IntVar()
var_bouncing_ball = tk.IntVar()
var_rps = tk.IntVar()

# Font configuration
font_config = ('Sans', 14)

# Create checkboxes for each feature
chk_video = tk.Checkbutton(frame, text="Control Video", variable=var_video, font=font_config, bg='black', fg='white', selectcolor='black')
chk_video.pack(anchor='w', padx=20, pady=5)

chk_audio = tk.Checkbutton(frame, text="Control Audio", variable=var_audio, font=font_config, bg='black', fg='white', selectcolor='black')
chk_audio.pack(anchor='w', padx=20, pady=5)

chk_media = tk.Checkbutton(frame, text="Control Media", variable=var_media, font=font_config, bg='black', fg='white', selectcolor='black')
chk_media.pack(anchor='w', padx=20, pady=5)

chk_mouse_tracking = tk.Checkbutton(frame, text="Mouse Tracking", variable=var_mouse_tracking, font=font_config, bg='black', fg='white', selectcolor='black')
chk_mouse_tracking.pack(anchor='w', padx=20, pady=5)

chk_bouncing_ball = tk.Checkbutton(frame, text="Bouncing Ball", variable=var_bouncing_ball, font=font_config, bg='black', fg='white', selectcolor='black')
chk_bouncing_ball.pack(anchor='w', padx=20, pady=5)

chk_rps = tk.Checkbutton(frame, text="Rock Paper Scissors", variable=var_rps, font=font_config, bg='black', fg='white', selectcolor='black')
chk_rps.pack(anchor='w', padx=20, pady=5)

# Create buttons
btn_toggle = tk.Button(frame, text="Start", command=toggle_features, font=font_config, bg='black', fg='white')
btn_toggle.pack(pady=10)

btn_gesture_mapping = tk.Button(frame, text="Open Gesture Mapping", command=start_gesture_mapping, font=font_config, bg='black', fg='white')
btn_gesture_mapping.pack(pady=10)

btn_end = tk.Button(frame, text="End", command=end_program, font=font_config, bg='black', fg='white')
btn_end.pack(pady=10)

root.mainloop()


