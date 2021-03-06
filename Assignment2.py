import cv2
def changeDemColor(contours, img, maxValue):
    thresHold = 0.0879
    for cnt in contours:
        if cv2.contourArea(cnt) < maxValue*thresHold:
            cv2.drawContours(img,[cnt],-1,255,-1)

def getMaxVal(contours):
    maxValue = 0
    for cnt in contours:
        currArea = cv2.contourArea(cnt)
        if currArea > maxValue:
            maxValue = currArea
    return maxValue

def demarcation_removal(img, index):
    _ , thres = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thres, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    maxValue = getMaxVal(contours)
    changeDemColor(contours, img, maxValue)
    cv2.imwrite("result{0}.jpg".format(index), img)

if __name__ == "__main__":
    window_name = 'Result'
    for x in range(1, 5):
        demarcation_removal(cv2.imread("Example{0}.png".format(x),0), x)

