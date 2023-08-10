
def clean_directory(directory):
    import os
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        try:
            if os.path.isfile(filepath):
                os.remove(filepath)
        except Exception as e:
            print(f"Error deleting file: {filepath}")


def num_files(directory):
    import os
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    num_dir = len(files)
    return num_dir


def clear_file(filename):

    with open(filename, "w") as f:
        pass  # Do nothing


def delete_last_file(directory):
    import os

    # Get a list of all files in the directory
    file_list = os.listdir(directory)

    # Find the name of the last file
    last_file_name = sorted(file_list)[-1]

    # Delete the last file
    os.remove(os.path.join(directory, last_file_name))


def main():
    import prediction
    import nlp
    import translationraspberryclient
    import extraction
    import record_vid
    import filereceive

    clear_file("/home/tester/finalProject/translated_content.txt")
    filereceive.fileserver("/home/tester/finalProject/videos")
    #record_vid.record("/home/tester/Desktop/videos")
    delete_last_file("/home/tester/finalProject/videos")
    extraction.main("/home/tester/finalProject/videos")
    clean_directory("/home/tester/finalProject/videos")
    prediction.translation()
    print("All .pkl Files Successfully Translated")
    clean_directory("/home/tester/finalProject/videos_after")
    translated_sentence = nlp.read_labels_translate()
    translationraspberryclient.main(translated_sentence)


if __name__ == "__main__":
    main()
