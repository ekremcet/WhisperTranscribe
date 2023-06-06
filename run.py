import argparse
from Transcriber import Transcriber
from glob import glob

model_sizes = {
    "tiny": "Relative speed: 32X, VRAM: 1GB",
    "base": "Relative speed: 16X, VRAM: 1GB",
    "small": "Relative spee: 6X, VRAM: 2GB",
    "medium": "Relative speed: 2X, VRAM: 5GB",
    "large-v2": "Relative speed: 1X, VRAM: 10GB"
}

parser = argparse.ArgumentParser(description="Transcribe YouTube Videos Using Whisper from OpenAI",
                                 formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-link", type=str,
                    help="link to YouTube video")
parser.add_argument("-name", type=str,
                    help="name of the output")
parser.add_argument("-api", type=bool, default=False,
                    help="use OpenAI API to transcribe")
parser.add_argument("-gdrive", type=bool, default=str,
                    help="path to google drive video")
parser.add_argument("--model", type=str, default="base",
                    choices=["tiny", "base", "small", "medium", "large"],
                    help="".join(
                        "{} -> {}\n".format(key, value) for key, value in model_sizes.items()))


def console_entry():
    args = parser.parse_args()
    model_size = args.model
    # Initialize transcriber
    transcriber = Transcriber(model_size=model_size)
    # Download and save audio file
    if args.gdrive:
        transcriber.extract_audio_gdrive(args.gdrive)
    else:
        transcriber.download_audio(args.link)
    # Start transcribing
    for ind, audio_file in enumerate(sorted(glob("./Data/Chunks/*.m4a"))):
        result = transcriber.transcribe(audio_file)
        transcriber.write_result(result, args.name, ind)
    print("Transcribe completed!!")
    # Clear download folders
    transcriber.clear()


if __name__ == '__main__':
    console_entry()
