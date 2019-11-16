from pydub import AudioSegment

sound1 = AudioSegment.from_file("./audioFiles/Bodak-Yellow.wav")
sound2 = AudioSegment.from_file("./audioFiles/September.wav")

combined = sound1.overlay(sound2)

combined.export("./combined.wav", format='wav')