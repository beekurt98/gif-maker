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
