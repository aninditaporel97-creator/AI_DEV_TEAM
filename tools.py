import os

def save_file(filename, content):
    """
    Save AI-generated content into the output folder.
    """

    output_folder = "output"

    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    file_path = os.path.join(output_folder, filename)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

    return f"{filename} saved successfully!"