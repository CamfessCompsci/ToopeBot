import os
from datetime import datetime
import fileinput


from textgenrnn import textgenrnn
# Magic code that makes it work
import tensorflow as tf
physical_devices = tf.config.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(physical_devices[0], enable=True)


# Parse emails, replacing new lines with ~|~ so textgenrnn can interpert every email as a single line
emails = []
emailpath = 'toopemail/'

for entry in os.listdir(emailpath):
    if os.path.isfile(os.path.join(emailpath, entry)):
        file = open(emailpath + entry, "r",encoding='utf8')
        contents = file.readlines()
        stripped = []
        for line in contents:
            stripped.append(line.rstrip("\n") + " ~|~ ")
        emails.append("".join(stripped))
        file.close()
print(emails)

# Load weights if desired
textgen = textgenrnn()
file = input("Enter epochs to load from, enter for from scratch: ")
epochs = int(input("Enter epochs to train for: "))
if file != "":
    textgen.load("textgenrnn_weights_epoch_"+file+".hdf5")

# Train
textgen.train_on_texts(emails,gen_epochs=50,num_epochs=epochs,max_gen_length=5000,save_epochs=50)

# Save and format a sample output
current_time = datetime.now().strftime("%d-%b--%H-%M")
filename = "output/generated--"+current_time+".txt"
textgen.generate_to_file(filename,max_gen_length=7000)

with fileinput.FileInput(filename, inplace=True) as file:
    for line in file:
        print(line.replace(" ~|~ ", "\n"), end='')

# Save final weights
textgen.save(weights_path="textgenrnn_weights_epochs_"+str(epochs + (int(file) if file != "" else 0)+".hdf5")
