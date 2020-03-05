# -*- coding: utf-8 -*-
"""ASVspoof2019_data_prepration.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Z9UliBTd-cJcqj-MQ16c21aLZNWTosbd
"""

from google.colab import drive
drive.mount('/content/drive/')

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/drive/My Drive/SA/Code/spoof_detection_deep_features

import keras 
import numpy as np
import librosa as lb
import pandas as pd
import os
import sys
# import pandas as pd
from keras.utils import to_categorical
# import soundfile as sf
from keras.layers import Dense
from keras.models import Sequential
from keras.callbacks import History 
from keras.utils import plot_model,to_categorical
from keras.optimizers import SGD
from keras.callbacks import TensorBoard, ModelCheckpoint
from keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import MinMaxScaler
# import speechpy as sp
# import statistics
from keras import backend as K
from keras.layers import Dense, Activation, Flatten

filename = "/content/drive/My Drive/SA/Code/spoof_detection_deep_features/data/ASVspoof2019/LA/ASVspoof2019_LA_cm_protocols/ASVspoof2019.LA.cm.train.trn.txt"

# open the file for reading
filehandle = open(filename, 'r')
train_protocol = []
while True:
    # read a single line
    line = (filehandle.readline())
    train_protocol.append(line)
    if not line:
        break

# close the pointer to that file
filehandle.close()

train_protocol = [s[:-1] for s in train_protocol]

train_protocol = pd.DataFrame([s.split(' ') for s in train_protocol])

train_protocol.head()

train_protocol.columns = ['speaker_id','file_id', 'blah','system_id', 'label']

train_protocol = train_protocol[['speaker_id', 'file_id', 'system_id', 'label']]

train_protocol

train_protocol = train_protocol.dropna()

train_protocol.iloc[1,1]

#import names of files in dataset
path = r'/content/drive/My Drive/SA/Code/spoof_detection_deep_features/data/ASVspoof2019/LA/ASVspoof2019_LA_train/flac'
files = []
missing=[]
print(path)
for r, d, f in os.walk(path):
    for file in f:
        if '.flac' in file  :        
            files.append(os.path.join(r, file))
        else:
            missing.append(file)
print(len(files))

files = [s.split('/') for s in files]

files = [s[-1] for s in files]

files = [s[:-5] for s in files]

files1 = [s.split(' ') for s in files]

for s in files:
  if len(s)>12:
    print(s)
    files.remove(s)

train_file_id = list(train_protocol.iloc[:,1])

train_file_id

train_labels = []
train_audio = []
for count,audio in enumerate(files):
  index = train_file_id.index(audio)
  if bool(index) == True:
    train_audio.append(lb.load('/content/drive/My Drive/SA/Code/spoof_detection_deep_features/data/ASVspoof2019/LA/ASVspoof2019_LA_train/flac/'+audio+'.flac',sr=16000))
    train_labels.append(train_protocol.iloc[index,3])
  if count%100 == 0 :
    print(count)
np.save("",np.array(train_audio))
np.save("",train_labels)

index = train_file_id.index('LA_T_4941896')
print(train_protocol.iloc[index])

train_audio

train_labels

function ClickConnect(){
console.log("Working"); 
document.querySelector("colab-toolbar-button").click() 
}setInterval(ClickConnect,60000)
