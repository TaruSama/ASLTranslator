import os
import sys
import mediapipe_extract as ext
import record_vid
import prediction
import nlp
import extraction


def clean_directory(directory):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        try:
            if os.path.isfile(filepath):
                os.remove(filepath)
        except Exception as e:
            print(f"Error deleting file: {filepath}")


def get_next_path(directory):
    directory_index = "/home/tester/finalProject"
    # Create a file to keep track of the last returned path
    state_file = os.path.join(directory_index, "index.txt")
    if not os.path.exists(state_file):
        with open(state_file, "w") as f:
            f.write("0")

    # Read the last returned path from the file
    with open(state_file, "r") as f:
        last_path_index = int(f.read())

    # Get a list of all files in the directory
    files = sorted(os.listdir(directory))

    # Determine the next path to return
    next_path = os.path.join(directory, files[last_path_index])
    # Increment the last returned path index and write it to the file
    if last_path_index == len(files) - 1:
        with open(state_file, "w") as f:
            f.write("0")
    else:
        with open(state_file, "w") as f:
            f.write(str(last_path_index + 1))
    return next_path


def num_files(directory):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    num_dir = len(files)
    return num_dir


def extraction_loop(directory):
    video_name = os.path.basename(get_next_path(directory))
    ext.extraction(video_name)
    print("Key point Extracted from Video")
    args = [sys.executable] + sys.argv
    os.execv(sys.executable, args)


def clear_file(filename):

    with open(filename, "w") as f:
        pass  # Do nothing


def delete_last_file(directory):
    # Get a list of all files in the directory
    file_list = os.listdir(directory)

    # Find the name of the last file
    last_file_name = sorted(file_list)[-1]

    # Delete the last file
    os.remove(os.path.join(directory, last_file_name))


def main():

    with open("/home/tester/finalProject/record_flag.txt", "r") as file:
        record_flag_var = int(file.read())

    with open("/home/tester/finalProject/extraction_flag.txt", "r") as file:
        extraction_flag_var = int(file.read())

    if record_flag_var == 0 and extraction_flag_var == 0:
        with open("/home/tester/finalProject/index.txt", "w") as file:
            file.write("0")
        clear_file("/home/tester/finalProject/translated_content.txt")
        print("Camera Launched")
        record_vid.record("/home/tester/finalProject/videos")
        with open("/home/tester/finalProject/record_flag.txt", "w") as file:
            file.write("1")
        with open("/home/tester/finalProject/extraction_flag.txt", "w") as file:
            file.write("1")
        delete_last_file("/home/tester/finalProject/videos")
        num_dir = num_files("/home/tester/finalProject/videos")
        videos_left = num_dir
        with open("/home/tester/finalProject/extraction_index.txt", "w") as file:
            file.write(str(videos_left))

    """
    with open("/home/tester/finalProject/extraction_index.txt", "r") as file:
        videos_left = int(file.read())
    while videos_left != 0:
        videos_left = videos_left - 1
        with open("/home/tester/finalProject/extraction_index.txt", "w") as file:
            file.write(str(videos_left))
        extraction_loop("/home/tester/finalProject/videos")
    """
    extraction.main("/home/tester/finalProject/videos")

    print("All Videos Extracted Successfully ")
    with open("/home/tester/finalProject/record_flag.txt", "w") as file:
        file.write("0")

    with open("/home/tester/finalProject/extraction_flag.txt", "w") as file:
        file.write("0")

    clean_directory("/home/tester/finalProject/videos")

    prediction.translation()

    print("All .pkl Files Successfully Translated")

    clean_directory("/home/tester/finalProject/videos_after")

    nlp.read_labels_translate()


if __name__ == "__main__":
    main()
