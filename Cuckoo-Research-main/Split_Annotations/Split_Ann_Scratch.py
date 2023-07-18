from opensoundscape.audio import Audio
from opensoundscape.spectrogram import Spectrogram
from opensoundscape.annotations import BoxedAnnotations

import numpy as np
import pandas as pd
from glob import glob

from matplotlib import pyplot as plt

import sys
import codecs

# audio_file = 'F:\\Training_Data\\82-3_20220620_070000.WAV'
# annotation_file = "F:\\Training_Data\\82-3_20220620_070000.Table.1.selections.txt"

audio_file = sys.argv[0]
annotation_file = sys.argv[1]

# print({annotation_file, "decoded"})

ann_file = open("decoded.txt", "a")

print('success files opened')
with codecs.open(annotation_file, 'r', 'utf8') as file:
    for line in file:
        value = line.decode('utf8', errors='replace')
        ann_file.write(value)
        

# annotation_file2 = ann_file.decode('utf8', errors='ignore')
print('success files decoded')

# output_file = sys.argv[2]

print('success files read')


# below fails to encode annotations to utf-8...so encode first, then call BoxedAnnotations? encoding operates on strings, so must read file by lines

annotations = BoxedAnnotations.from_raven_files([ann_file], keep_extra_columns=["BBCU", "YBCU"], annotation_column_idx=13, audio_files=[audio_file])

print('success boxed annotations generated')

# annotations2 = BoxedAnnotations.from_raven_files([annotation_file],  annotation_column_idx=None, audio_files=[audio_file])

num_rows = annotations.df.shape[0]
row = 0

# FILL ANNOTATIONS COLUMN WITH BOTH, BBCU, YBCU, None
while row < num_rows:
    if ((annotations.df["BBCU"][row] == 1) and (annotations.df["YBCU"][row] == 1)):
        annotations.df["annotation"][row] = "BOTH"
        print("both\n")
    elif (annotations.df["BBCU"][row] == 1):
        annotations.df["annotation"][row] = "BBCU"
        print("BBCU\n")
    elif (annotations.df["YBCU"][row] == 1):
        annotations.df["annotation"][row] = "YBCU"
        print("YBCU\n")
    else: 
        annotations.df["annotation"][row] = None
        print("none\n")
    row += 1

print('success annotations formatted')
print(annotations.df.head())


# SPLIT 30 MIN AUDIO INTO 5 SEC CLIPS
final_split_audio = annotations.one_hot_clip_labels(
    clip_duration=5.0,
    clip_overlap=0,
    min_label_overlap=0,
    full_duration=1800.0,
    class_subset=None
)

print('success audio split')
print(final_split_audio.head(1800))
print('complete')
# TODO: figure out how to export final_split_audio to a raven-compatible file
# final_split_audio.to_raven_files("C:\Users\bw165311\Documents\Python Scripts\SplitFiles1")

# with open(output_file, 'w') as file:
#     file.write('file successfully written to.')


# TODO: have BBCU and YBCU columns show in split files --> [30]: from tutorial
# OR
# TODO: get single annotations column to show BBCU, YBCU, BOTH, NaN 
#   so that the split audio files show columns titled BBCU, YBCU, BOTH   


############# END OF FUNCTIONAL CODE ##############################




############ CODE BELOW functions, not optimal #################

# splits audio file into 5 second clips
# audio = Audio.from_file(audio_file)
# _, clip_df_5sec = audio.split(
#     clip_duration=5.0, 
#     clip_overlap=0.0
# )

# print(clip_df_5sec.head())

################ JARGON ##################

        # labels_df = annotations2.one_hot_labels_like(
        #     clip_df_5sec,
        #     min_label_overlap=0.0
        #     class_subset=["BBCU"]
        # )

        # print("\n\n")
        # print(labels_df.head())


