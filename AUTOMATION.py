import cv2
import dropbox
import time
import random

start_time = time.time()


def take_snapshort():
    number = random.randint(0, 100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret, frame = videoCaptureObject.read()
        image_name = "img" + str(number) + ".png"
    cv2.imwrite(image_name, frame)
    start_time = time.time
    result = False

    return image_name
    print("snapshort taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()


take_snapshort()


def upload_file():
    access_token = 'nRVWoQlQ7KIAAAAAAAAAARVGkWWMXXzBuUycgV7eRpPmcgfQROYlcE74Gy_SsuOd'
    file = image_name
    file_from = file
    file_to = "/newFolder1"+(image_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,
                         mode=dropbox.files.WriteMode.overWrite)
        print("file uploaded")


def main():
    while(True):
        if ((time.time() - start_time) >= 3):
            name = take_snapshort()
            upload_file(name)


main()
