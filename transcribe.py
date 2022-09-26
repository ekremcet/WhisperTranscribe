import whisper

model = whisper.load_model("base")
result = model.transcribe("./test.mp3")
with open("./result.txt", "w") as f:
    for line in result["text"].split("."):
        print(line)
        f.writelines(line + "\n")
