from pydub import AudioSegment

sound1 = AudioSegment.from_file("./Bodak-Yellow.wav")
sound2 = AudioSegment.from_file("./September.wav")

combined = sound1.overlay(sound2)

combined.export("./combined.wav", format='wav')