import os

def analyze_path(path):
    # Check if path exists
    if not os.path.exists(path):
        print(f"Path '{path}' does not exist.")
        return

    # Find filename and directory portion
    directory, filename = os.path.split(path)
    print(f"Path '{path}' exists.")
    print(f"Directory: {directory}")
    print(f"Filename: {filename}")

# Example usage
given_path = r"C:\Users\kimti\Desktop\PP2\lab6"
analyze_path(given_path)
