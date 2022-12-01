# Import Dependencies
from moviepy.editor import *
import csv
from datetime import datetime
import pandas as pd

# Read CSV file
df = pd.read_csv('blue.csv')

# Start loop with one row at a time
for row in df.iloc:

    #start time
    start_str=row[0].replace(',',"")
    print(start_str)

    # end time
    end_str=row[1].replace(',',"")
    print(end_str)

    # Clipping the video
    video = VideoFileClip("blue.mkv").subclip(t_start=start_str, t_end=end_str)
    print("Video Clipped")

    # Create dynamic name with start and end time
    name = "clip"+"-"+start_str+"-"+end_str+".mp4"
    print(name)

    # Save video clip blob in result variable
    result = CompositeVideoClip([video])
    print("CompositeVideoClip")

    # Write video clip file as per given format
    result.write_videofile(name)
    print("Video File written")
