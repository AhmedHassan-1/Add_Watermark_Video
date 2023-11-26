import os

try:
    import ffmpeg
    import argparse
except:
    try:
        os.system("pip install ffmpeg")
    except:
        print("cann't run ffmpeg")
