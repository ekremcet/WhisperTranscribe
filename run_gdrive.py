import argparse
from Transcriber import Transcriber
from glob import glob


model_sizes = {
    "tiny": "Relative speed: 32X, VRAM: 1GB",
    "base": "Relative speed: 16X, VRAM: 1GB",
    "small": "Relative spee: 6X, VRAM: 2GB",
    "medium": "Relative speed: 2X, VRAM: 5GB",
    "large": "Relative speed: 1X, VRAM: 10GB"
}

parser = argparse.ArgumentParser(description="Transcribe Videos in Your Google Drive Using Whisper from OpenAI",
                                 formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-path", type=str,
                    help="path to GoogleDrive video")
parser.add_argument("-name", type=str,
                    help="name of the output")
parser.add_argument("--model", type=str, default="base",
                    choices=["tiny", "base", "small", "medium", "large"],
                    help="".join(
                        "{} -> {}\n".format(key, value) for key, value in model_sizes.items()))


def console_entry():
    args = parser.parse_args()
    model_size = args.model
    # Initialize transcriber
    transcriber = Transcriber(model_size=model_size)
    # Extract audio from google drive video
    transcriber.extract_audio_gdrive(args.path)
    # Start transcribing
    for ind, audio_file in enumerate(sorted(glob("./Data/Chunks/*.m4a"))):
        result = transcriber.transcribe(audio_file)
        transcriber.write_result(result, args.name, ind)
    print("Transcribe completed!!")
    # Clear download folders
    transcriber.clear()


if __name__ == '__main__':
    console_entry()
