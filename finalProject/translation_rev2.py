import prediction
import nlp
import nlp_rev2
import client
import extraction
import record_vid_rev2
import file_receive
import os


def clean_directory(directory):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        try:
            if os.path.isfile(filepath):
                os.remove(filepath)
        except Exception as e:
            print(f"Error deleting file: {filepath}")


def num_files(directory):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    num_dir = len(files)
    return num_dir


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


def rearrange_lines(input_filename, word_count_list, output_filename):
    with open(input_filename, 'r') as f:
        lines = f.read().splitlines()

    output_lines = []
    index = 0

    for count in word_count_list:
        if index + count <= len(lines):
            output_lines.append(' '.join(lines[index:index + count]))
            index += count
        else:
            print(f"Warning: Not enough remaining words for line with {count} words.")

    with open(output_filename, 'w') as f:
        for line in output_lines:
            f.write(line + '\n')


def main():

    dir_vid = "/home/tester/finalProject/videos"
    translated_txt = "/home/tester/finalProject/translated_content.txt"
    dir_pkl = "/home/tester/finalProject/videos_after"
    switch_mode_flag = "/home/tester/finalProject/switch_mode_flag.txt"

    with open(switch_mode_flag, 'r') as file:
        mode_flag = file.read()
    clear_file(translated_txt)
#   file_receive.fileserver(dir_vid)
#   delete_last_file(dir_vid)
    if mode_flag == "1":
        print("Mode 2 is up")
    else:
        print("Mode 1 is up")
    word_count_list = record_vid_rev2.record_delete(dir_vid)
    extraction.main(dir_vid)
    clean_directory(dir_vid)
    prediction.translation()
    clean_directory(dir_pkl)
    rearrange_lines(translated_txt, word_count_list, translated_txt)
    translated_sentence = nlp_rev2.main(translated_txt, translated_txt)
    client.main(translated_sentence)


if __name__ == "__main__":
    main()
