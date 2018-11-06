
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 10:14:35 2018

@author: alexissoto
"""

'''

Music Production Kit

'''

import librosa as lb

song = "Fantasia_Impromptu.m4a" #Input file

def TempoChange():
    
    y, sr = lb.load(song, duration = 30)
    tempo, beat_frames = lb.beat.beat_track(y = y, sr = sr)
    stretch = lb.effects.time_stretch(y, 2.0) #2.0 for double fast. 0.5 for half
    lb.output.write_wav('Double fast.wav', stretch, sr = sr) #Your output here.
    
def Harmonics():
    
    y, sr = lb.load(song, duration = 30)
    y_harmonic = lb.effects.harmonic(y)
    lb.output.write_wav('Just harmonic content.wav', y_harmonic, sr=sr)

def Percussive():
    
    y, sr = lb.load(song, duration = 30)
    y_percussive = lb.effects.percussive(y)
    lb.output.write_wav('Just percusive content.wav', y_percussive, sr = sr)
    
def Both():
    y, sr = lb.load(song, duration= 30)
    y_harmonic, y_percussive = lb.effects.hpss(y, margin = (1.0, 5.0))
    lb.output.write_wav('Percussive.wav', y_percussive, sr = sr)

def Steps():
    
    y, sr = lb.load(song, duration = 30)
    y_third = lb.effects.pitch_shift(y, sr, n_steps = 2)
    lb.output.write_wav('Major second.wav', y_third, sr=sr)
    
def Tempo():
    
    y, sr = lb.load(song, duration = 30)
    envelope = lb.onset.onset_strength(y, sr = sr)
    tempo = lb.beat.tempo(onset_envelope = envelope, sr=sr)
    print('Tempo is %d BPM' % tempo)





















