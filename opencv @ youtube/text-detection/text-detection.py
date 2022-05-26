import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\tesseract\\tesseract.exe'

img = cv2.imread("assets/life.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
imgNum = cv2.imread('assets/numbers - Copy.jpg')
imgNum = cv2.cvtColor(imgNum, cv2.COLOR_BGR2RGB)

#print(pytesseract.image_to_string(img))

# DETECTING CHARACTERS
def read_char(image):
    hImg, wImg, _ = image.shape
    boxes = pytesseract.image_to_boxes(image)
    for b in boxes.splitlines():
        b = b.split(' ')
        #print(b)
        x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
        cv2.rectangle(image, (x,hImg-y), (w,hImg-h), (0,0,255), 1)
        cv2.putText(image, b[0], (x, hImg-y-30), cv2.FONT_HERSHEY_SIMPLEX, 1, (25,25,255), 2)
    cv2.imshow("Characters", image)

# # DETECTING WORDS
def read_words(image):
    hImg, wImg, _ = image.shape
    boxes = pytesseract.image_to_data(image)
    for x, b in enumerate(boxes.splitlines()):
        if x != 0:
            b = b.split()
            # print(b)
            if len(b) == 12:
                x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 1)
                cv2.putText(image, b[11], (x, y + 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (25, 25, 255), 2)
    cv2.imshow("Words", image)

# DETECTING NUMBERS
def read_num(image):
    hImg, wImg, _ = image.shape
    cong = r'--oem 3 --psm 6 outputbase digits' #oem and psm represents the engine mode.

    boxes = pytesseract.image_to_data(image, config=cong)
    for x, b in enumerate(boxes.splitlines()):
        if x != 0:
            b = b.split()
            # print(b)
            if len(b) == 12:
                x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 1)
                cv2.putText(image, b[11], (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (25, 25, 255), 2)
    cv2.imshow("Numbers", image)


read_char(img)
read_words(img)
read_num(imgNum)




cv2.waitKey(0)

