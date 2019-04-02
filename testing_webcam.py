import cv2


def show_cam(mirror=False):
    cam = cv2.VideoCapture(1)
    while True:
        ret_val, img = cam.read()
        if mirror:
            img = cv2.flip(img, 1)
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            im_floodfill_inv = cv2.bitwise_not(img)
        cv2.imshow('Test Webcam - Colour', img)
        cv2.imshow("Test Webcam - Gray", gray_image)
        cv2.imshow("test webcam - invert", im_floodfill_inv)
        if cv2.waitKey(1) == ord('q'):
            print("The program is now closed!")
            break #use the Q button to quit the program
    cv2.destroyAllWindows()


def main():
    show_cam(mirror=True)


if __name__ == '__main__':
    main()
