#Some tools for sound processing and visualization.

import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.io.wavfile
import librosa as lb
from scipy import fftpack
from magenta.models.nsynth import utils
from magenta.models.nsynth.wavenet import fastgen
#Need to install this magenta model in directory in order to execute.

fname = 'TestTone220.wav' #Put here directory of file or name.
bit_Depth = 16000 #or bit depth of your file.

#scipy function wavfile.read, just for sample rate in case of unknown.
def getSampleRate(filename): 
    fid = open(filename, 'rb')
    try:
        file_size, is_big_endian = scipy.io.wavfile._read_riff_chunk(fid) # find out how to read the file
        channels = 1 # assume 1 channel and 8 bit depth if there is no format chunk
        bit_depth = 8
        while fid.tell() < file_size: #read the file a couple of bytes at a time
            # read the next chunk
            chunk_id = fid.read(4)
    
            if chunk_id == b'fmt ':  # retrieve formatting information
                fmt_chunk = scipy.io.wavfile._read_fmt_chunk(fid, is_big_endian)
                format_tag, channels, fs = fmt_chunk[1:4]
                bit_depth = fmt_chunk[6]
                if bit_depth not in (8, 16, 32, 64, 96, 128):
                    raise ValueError("Unsupported bit depth: the wav file "
                                     "has {}-bit data.".format(bit_depth))
    finally:
        if not hasattr(filename, 'read'):
            fid.close()
        else:
            fid.seek(0)
    
    print(fs)

#Magenta model to synthezise new sound.  Uses librosa as one of the core modules.
def Plot_SingleFile(file_name, sampleRate):    
    audio = utils.load_audio(file_name, sample_length=70000) #sample_length for how long will it be.
    sample_length = audio.shape[0]
    print('{} samples, {} seconds'.format(sample_length, sample_length / float(sampleRate)))
    
    #Encoding for new sound part.
    encoding = fastgen.encode(audio, 'model.ckpt-200000', sample_length)
    print(encoding.shape)
    np.save(fname + '.npy', encoding)
    
    fig, axs = plt.subplots(2, 1, figsize = (10,5))
    axs[0].plot(audio)
    axs[0].set_title('Audio Signal')
    axs[1].plot(encoding[0]);
    axs[1].set_title('NSynth Encoding')
    
    #synthesis
    fastgen.synthesize(encoding, save_paths=['gen_' + fname], samples_per_save=sample_length)
    
#To combine sounds (Magenta takes in representation tumbre, tonality and change over time)
    
def load_encoding(fname, sample_lenght = None, sr = 16000, ckpt = 'model.ckpt-200000'):
    audio = utils.load_audio(fname, sample_length = sample_lenght, sr = sr)
    encoding = fastgen.encode(audio, ckpt, sample_lenght)
    return audio, encoding

def Combine_Plot(file1, file2): 
    sample_length = 20000 #Duration
    aud1, enc1 = load_encoding(file1, sample_length)
    aud2, enc2 = load_encoding(file2
                               , sample_length)
    
    enc_mix = (enc1 + enc2)/ 2.0
    fig, axs = plt.subplots(3, 1, figsize = (10, 7))
    fig, axs = plt.subplots(3, 1, figsize=(10, 7))
    axs[0].plot(enc1[0]); 
    axs[0].set_title('Encoding 1')
    axs[1].plot(enc2[0]);
    axs[1].set_title('Encoding 2')
    axs[2].plot(enc_mix[0]);
    axs[2].set_title('Average') 
    
def fade(encoding, mode='in'):
    length = encoding.shape[1]
    fadein = (0.5 * (1.0 - np.cos(3.1415 * np.arange(length) / 
                                  float(length)))).reshape(1, -1, 1)
    if mode == 'in':
        return fadein * encoding
    else:
        return (1.0 - fadein) * encoding
    
def crossfade(encoding1, encoding2):
    return fade(encoding1, 'out') + fade(encoding2, 'in')
    
def Combine_Synth(file1, file2):
    sample_length = 20000 #Duration
    aud1, enc1 = load_encoding(file1, sample_length)
    aud2, enc2 = load_encoding(file2, sample_length)
    fastgen.synthesize(crossfade(enc1, enc2), save_paths = ['crossfade.wav'])

def fft_index(n):
    return np.append(np.arange(n//2,n), np.arange(0, n//2))
    
def fft_unpack(x):
    return [x[i] for i in fft_index(len(x))]

def fft(x):
    X = fftpack.fft(x) 
    return fft_unpack(X)

def PlotEverything(sampleRate, dataR, freqDataR):
    plt.subplot(411)
    timeAxis = np.arange(0,len(dataR)/sampleRate,1/sampleRate)
    plt.plot(timeAxis[0:1000], dataR[0:1000])
    
    plt.subplot(412)
    freqAxis = sampleRate*np.arange(-1/2,1/2,1/len(freqDataR))
    plt.plot(freqAxis, freqDataR)
    
    plt.show()  
    
def music(name):
    
    Data = lb.core.load(name) #return audio time series.
    print("audio time series: " + str(Data))
    
    
    SR, Filedata = scipy.io.wavfile.read(name) 
    print("SampleRate: " + str(SR))

    print("DataLen: " + str(len(Filedata)))
    try:
        FiledataR, FiledataL = Filedata.T
    except:
        FiledataR = Filedata
        FiledataL = []

    freqDataR = fft(FiledataR) 
    #freqDataL = fft(FiledataL)
    
    Newsize = len(freqDataR)
    PlotEverything(SR, FiledataR, freqDataR)
