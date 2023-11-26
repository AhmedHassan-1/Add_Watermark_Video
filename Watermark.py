from setup import *

parser = argparse.ArgumentParser(description="Put Watermark on Video")
parser.add_argument(
    "-v",
    "-i",
    "--video_input",
    type=str,
    help="The video that will be watermarked you must write full directory if video hadn't in the same file directory",
)
parser.add_argument(
    "-W",
    "--Watermark",
    type=str,
    help="WaterMark : you must write full directory if video hadn't in the same file directory",
)
parser.add_argument("-n", "-name", "--name", type=str, help="file name with extension")
parser.add_argument("-m_x", "--margin_X", type=str, help="Margin_X")
parser.add_argument("-m_y", "--margin_Y", type=str, help="Margin_Y")
args = parser.parse_args()
ffmpeg.input(args.video_input).output(
    args.name,
    vf="movie="
    + args.Watermark
    + f" [watermark]; [in][watermark] overlay=W-w-{int(args.margin_X)}:H-h-{int(args.margin_Y)} [out]",
).run()
os.system("clear")
