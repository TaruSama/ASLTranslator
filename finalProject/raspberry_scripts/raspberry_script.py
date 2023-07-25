import record_vid
import client_send_vid
import raspberry_helpers
import time

if __name__ == "__main__":

    directory = "/home/tester/videos"
    record_vid.record(directory)
    print("Initiate filereceive script on Server - client script will start in 5 seconds")
    time.sleep(5)
    client_send_vid.fileclient(directory)
    raspberry_helpers.clean_directory(directory)


