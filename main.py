import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip, vfx


class GifMaker:
    def __init__(self, file, fps, speed, new_file_name):
        self.file_name = new_file_name
        self.file = file
        self.fps = fps
        self.speed = speed

    def make_gif(self):
        video = VideoFileClip(self.file).fx(vfx.speedx, self.speed)
        video.write_gif(self.file_name, fps=self.fps)


def browse_files():
    file = filedialog.askopenfilename(
        initialdir="/",
        title="Select a File",
        filetypes=(("Video files", "*.mp4*"), ("All files", "*.*"))
    )
    if file:
        label_file_explorer.config(text=f"File Selected:\n{file}")
        app_state['file'] = file


def save_gif():
    file = app_state.get('file')
    speed = speed_text.get()
    fps = fps_text.get()
    name = name_entry.get().strip()

    if file and speed.isdigit() and fps.isdigit() and name:
        save_path = filedialog.asksaveasfilename(
            initialfile=name,
            defaultextension=".gif",
            filetypes=[("GIF files", "*.gif")]
        )
        if save_path:
            gif = GifMaker(file, int(fps), int(speed), save_path)
            gif.make_gif()
            label_file_explorer.config(text=f"GIF saved to:\n{save_path}")
    else:
        label_file_explorer.config(text="Please select a file and fill all fields.")


app_state = {'file': None}

window = tk.Tk()
window.title("Video to GIF Converter")
window.geometry("500x400")
window.config(background="#f0f0f0")

label_file_explorer = tk.Label(
    window,
    text="Select a video file to convert to GIF",
    fg="#333",
    bg="#f0f0f0",
    font=("Segoe UI", 10),
    wraplength=480,
    justify="center"
)

button_explore = tk.Button(
    window,
    text="Browse Video",
    command=browse_files,
    bg="#4CAF50",
    fg="white",
    font=("Segoe UI", 10),
    padx=10,
    pady=5
)

# Label and entry for GIF name
name_label = tk.Label(window, text="Output GIF name:", bg="#f0f0f0", font=("Segoe UI", 10))
name_entry = tk.Entry(window, font=("Segoe UI", 10), width=30)

# Speed label and dropdown
speed_label = tk.Label(window, text="Playback Speed:", bg="#f0f0f0", font=("Segoe UI", 10))
speed_text = tk.StringVar(window)
speed_text.set("1")
speed_dropdown = tk.OptionMenu(window, speed_text, *["1", "2", "3", "5", "10"])
speed_dropdown.config(font=("Segoe UI", 10))

# FPS label and dropdown
fps_label = tk.Label(window, text="Frames Per Second (FPS):", bg="#f0f0f0", font=("Segoe UI", 10))
fps_text = tk.StringVar(window)
fps_text.set("10")
fps_dropdown = tk.OptionMenu(window, fps_text, *["5", "10", "20", "30", "50"])
fps_dropdown.config(font=("Segoe UI", 10))

button_save = tk.Button(
    window,
    text="Save GIF",
    command=save_gif,
    bg="#2196F3",
    fg="white",
    font=("Segoe UI", 10),
    padx=10,
    pady=5
)

button_exit = tk.Button(
    window,
    text="Exit",
    command=window.quit,
    bg="#f44336",
    fg="white",
    font=("Segoe UI", 10),
    padx=10,
    pady=5
)

# Layout
label_file_explorer.pack(pady=(20, 10))
button_explore.pack(pady=5)
name_label.pack()
name_entry.pack(pady=(0, 10))
speed_label.pack()
speed_dropdown.pack(pady=5)
fps_label.pack()
fps_dropdown.pack(pady=5)
button_save.pack(pady=10)
button_exit.pack(pady=5)

window.mainloop()
