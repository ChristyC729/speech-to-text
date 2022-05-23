# Transcription

Two different implementations of speech-to-text transcriptions are displayed in the project. The AssemblyAI API was used to `POST` and `GET` files. Both implementations were written in Python.

## Accepted File Types:
### Audio Files:
* .3ga
* .aac
* .ac3
* .aif
* .aiff
* .alac
* .amr
* .ape
* .au
* .dss
* .flac
* .flv
* .m4a
* .m4b
* .m4p
* .mp3
* .mpga
* .ogg, .oga, .mogg
* .opus
* .qcp
* .tta
* .voc
* .wav
* .wma
* .wv
### Video Files:
* .webm
* .MTS, .M2TS, .TS
* .mov
* .mp4, .m4p (with DRM), .m4v
* .mxf

## 1. Transcribing Local Files:

In the folder directory, you can run:
```
python3 transcribe_local.py
```
It will then prompt the user to enter the local path to the audio file. 
```
Enter local file path:
```
If the file path is located, it will return the transcription directly in the terminal.

## 2. Transcribing URL Files:

In the folder directory, you can run:
```
python3 transcribe_url.py
```
It will then prompt the user to enter the local path to the audio file. 
```
Enter file url:
```
If the file url is located, it will return the transcription directly in the terminal.