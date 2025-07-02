from pydub import AudioSegment
# Loading the 5 audio files
audio1 = AudioSegment.from_file("first.mp3")
audio2 = AudioSegment.from_file("second.mp3")
audio3 = AudioSegment.from_file("third.mp3")
audio4 = AudioSegment.from_file("fourth.mp3")
audio5 = AudioSegment.from_file("five.mp3")

merge_audio = audio1 + audio2 + audio3 + audio4 + audio5
merge_audio.export("merge_audio.mp3", format="mp3")
print("Done!")
