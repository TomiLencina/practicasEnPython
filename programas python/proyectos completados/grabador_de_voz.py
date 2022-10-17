import sounddevice
from scipy.io.wavfile import write

fs = 44100
name = input("Elige un nombre para tu archivo: ")
segundos = int(input("Ingresa la cantidad de tiempo que funcionara el grabador: "))
print("Grabando...")
record_voice = sounddevice.rec(int(segundos * fs),samplerate=fs, channels=2)
sounddevice.wait()
write("{}.wav".format(name), fs,record_voice)
print("El archivo se guarda en tu carpeta automaticamente...")