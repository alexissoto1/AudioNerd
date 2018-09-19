import numpy as np
import pyaudio, aubio #aubio mainly for the .pitch detection tool in it.
import time
import queue, argparse
import music21  

#Input assingment!
parser = argparse.ArgumentParser()
parser.add_argument("-input", required=False, type=int, help="Audio Input Device")
args = parser.parse_args()

# PyAudio object.
p = pyaudio.PyAudio()

# Open stream.
stream = p.open(format = pyaudio.paFloat32, channels=1, rate = 44100, input = True,
                input_device_index = args.input, frames_per_buffer = 4096)
time.sleep(1)

# Aubio's pitch detection.
pDetection = aubio.pitch("default", 2048, 2048//2, 44100)
pDetection.set_unit("Hz")
pDetection.set_silence(-40)

queue = queue.Queue()

def get_note(volume_thresh=0.01, printOut=False):

    current_pitch = music21.pitch.Pitch()

    while True:

        data = stream.read(1024, exception_on_overflow = False)
        samples = np.fromstring(data, dtype = aubio.float_type)
        pitch = pDetection(samples)[0]
        volume = np.sum(samples**2)/len(samples) * 100

        if pitch and volume > volume_thresh: 
            current_pitch.frequency = pitch
        else:
            continue

        if printOut:
            print(current_pitch)
        
        else:
            current = current_pitch.nameWithOctave
            queue.put({'Note': current, 'Cents': current_pitch.microtone.cents})

if __name__ == '__main__': get_note(volume_thresh=0.001, printOut=True)