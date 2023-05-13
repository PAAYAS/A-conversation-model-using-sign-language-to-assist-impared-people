from pydub import AudioSegment
def convert(audio):
    mp3_file = AudioSegment.from_file(audio, format="mp3")
    mp3_file.export("file.wav", format="wav")