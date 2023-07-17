import translation
import vpsserver
import filereceive
import threading


def translationmachine():
    translation.main()


def vpsserverscript():
    vpsserver.main()


def filereceivescript():
    filereceive.fileserver()


if __name__ == '__main__':

    process1 = threading.Thread(target=translationmachine)
    process2 = threading.Thread(target=vpsserverscript)
    process3 = threading.Thread(target=filereceivescript)

    process1.start()
    process2.start()
    process3.start()

    process1.join()
    process2.join()
    process3.join()