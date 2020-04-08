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

# Set up parameters

weights_file = input("Enter weights file: ")
textgen = textgenrnn()
textgen.load(weights_file)
num = int(input("Enter number of files to generate: "))
t = input("Enter temperature as list or decimal (enter for default): ")
if t == "":
    temperature = [1.0, 0.5, 0.2, 0.2] # Default
elif t[0] == "[":
    temperature = t.strip('][').split(', ') # Convert to list
else:
    temperature = float(t) # Interpert as float
directory = input("Enter directory to save files: ").rstrip("/")
print("Generating...")

# Generate emails
generated = textgen.generate(num, return_as_list=True, temperature=temperature, max_gen_length=max_len, top_n=top_n,
                             progress=True)
print("Generated!")
print("Saving files...")
# Format and save emails (~|~ is a placeholder for newline)
current_time = datetime.now().strftime("%d-%b--%H-%M")
for i in range(num):
    filename = directory + "/generated--" + current_time + "--" + str(i) + ".txt"
    with open(filename,"w") as file:
        file.write(generated[i])
    with fileinput.FileInput(filename, inplace=True) as file:
        for line in file:
            print(line.replace(" ~|~ ", "\n"), end='')
