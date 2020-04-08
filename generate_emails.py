import fileinput
from datetime import datetime

from textgenrnn import textgenrnn
# Magic code that makes it work
import tensorflow as tf

physical_devices = tf.config.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(physical_devices[0], enable=True)

# Hyperparameters
max_len = 7000
top_n = 3
temperature = 0.5

# Generate emails
weights_file = "textgenrnn_weights_epoch_150.hdf5"
textgen = textgenrnn()
textgen.load(weights_file)

num = int(input("Enter number of files to generate: "))
directory = input("Enter directory to save files: ").rstrip("/")+"/"

print("Generating...")
generated = textgen.generate(num, return_as_list=True, temperature=temperature, max_gen_length=max_len, top_n=top_n,
                             progress=True)
print("Generated!")
print("Saving files...")
# Save and reformat emails (~|~ is the placeholder for new line)
current_time = datetime.now().strftime("%d-%b--%H-%M")
for i in range(1,num+1):
    filename = directory + str(i) + ".txt"
    with open(filename, "w") as file:
        file.write(generated[i-1])
    with fileinput.FileInput(filename, inplace=True) as file:
        for line in file:
            print(line.replace(" ~|~ ", "\n"), end='')
