import cv2


def show_webcam(mirror=False):
    cam = cv2.VideoCapture(1)
    while True:
        ret_val, img = cam.read()
        if mirror:
            img = cv2.flip(img, 1)
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Test Webcam - Colour', img)
        cv2.imshow("Test Webcam - Gray", gray_image)
        if cv2.waitKey(1) == ord('q'):
            break #use the q button to quit the program
    cv2.destroyAllWindows()


def main():
    show_webcam(mirror=True)


if __name__ == '__main__':
    main()
