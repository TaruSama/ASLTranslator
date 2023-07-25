import filereceive
import translationraspberry


if __name__ == '__main__':

    with open("/home/tester/finalProject/receivedfileflag.txt", "r") as file:
        received_file_flag = int(file.read())

    if received_file_flag == 0:
        filereceive.fileserver()
        with open("/home/tester/finalProject/receivedfileflag.txt", "w") as file:
            file.write("1")

    translationraspberry.main()

    with open("/home/tester/finalProject/receivedfileflag.txt", "w") as file:
        file.write("0")
