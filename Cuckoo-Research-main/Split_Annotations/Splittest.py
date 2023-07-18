#practice run for splitting annotation files

from opensoundscape.audio import Audio
from opensoundscape.spectrogram import Spectrogram
from opensoundscape.annotations import BoxedAnnotations

import numpy as np
import pandas as pd
from glob import glob


from matplotlib import pyplot as plt
plt.rcParams['figure.figsize']=[15,5] #for big visuals
# from IPython.display import set_matplotlib_formats
# set_matplotlib_formats('retina')

# %config InlineBackend.figure_format = 'retina'

# import subprocess
# subprocess.run(['curl','https://drive.google.com/uc?export=download&id=1ZTlV9KzWU0lWsjZpn1rgA92LUuXO1u8a','-L', '-o','gwwa_audio_and_raven_annotations.tar.gz']) # Download the data
# subprocess.run(["tar","-xzf", "gwwa_audio_and_raven_annotations.tar.gz"]) # Unzip the downloaded tar.gz file
# subprocess.run(["rm", "gwwa_audio_and_raven_annotations.tar.gz"])

# CompletedProcess(args=['rm', 'gwwa_audio_and_raven_annotations.tar.gz'], returncode=0)

audio_file = "C:\Users\bw165311\Documents\Python Scripts\gwwa_audio_and_raven_annotations\GWWA_XC\13738.wav"
# 'gwwa_audio_and_raven_annotations/GWWA_XC/13738.wav'
annotation_file = "C:\Users\bw165311\Documents\Python Scripts\gwwa_audio_and_raven_annotations\GWWA_XC_AnnoTables\._13738.Table.1.selections.txt"
# 'gwwa_audio_and_raven_annotations/GWWA_XC_AnnoTables/13738.Table.1.selections.txt'



# Spectrogram.from_audio(Audio.from_file(audio_file)).plot()

#create an object from Raven file
annotations = BoxedAnnotations.from_raven_files([annotation_file],audio_files=[audio_file])

#inspect the object's .df attribute, which contains the table of annotations
annotations.df.head()