pip install ffmpeg-python
conda install -c conda-forge ffmpeg
import ffmpeg
stream =ffmpeg.input('0530.mp4')
stream=ffmpeg.hflip(stream)
ffmpeg.run(stream)