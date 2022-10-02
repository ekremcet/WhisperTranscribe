# WhisperTranscribe
Transcribing YouTube videos using OpenAI's Whisper. <br>

> Download YouTube videos as transcribed text files 

## Installation
Clone the repository and install requirements

```
git clone https://github.com/ekremcet/WhisperTranscribe.git
cd ./WhisperTranscribe
pip3 install -r requirements.txt
```

## Sample Usage
```
python3 run.py -link https://www.youtube.com/watch?v=1UoRU3Dp3x8&ab_channel=ATHENA -name LiDeR --model base
```

This will save the transcirbed audio as text files with and without time stamps in `./Results/LiDeR/` folder. 

Each 10 minute long chunk is saved separately.
