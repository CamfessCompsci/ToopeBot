# ToopeBot

After crying over the loss of our daily updates, I created a bot that writes more!

## 100 PRE-GENERATED EMAILS ARE IN THE "GENERATED EMAILS" FOLDER


## Use (Needs medium to moderate levels of compsci)

The toopemail directory holds all of the daily updates to date, you can add more files to train the neural network on them as well.

toopeTrain.py runs training for a specified number of cycles, loading a pre-trained file from the top level directory if any is specified.

toopeGen.py generates emails

generate_emails.py does the same, but with hardcoded parameters that seemed to work decently (150 epochs, 0.5 temperature).


Pre-trained models for 50,100,150,200,250, and 500 epochs are in the top level directory.

Temperature controls how random the emails are, a higher temperature leads to weirder results while a low temperature can lead to direct copies of existing emails.

### Dependencies

Only tested on tensorflow 2.1 with CUDA 10.1 and cuDNN 7.6.5, python 3.6.9

Honestly the directories are a mess, you'll probably have to fix it all yourself

# Credit

Used textgenrnn by minimaxir

Hello Camfess I love you!