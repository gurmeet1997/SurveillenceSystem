import cv2
import time

width=150
xcls=640
pos=640

tempPos=640
countPos=0
countMul=0
countZero=0
count255=0
frameCount=0

multiWarningFlag=False
coverFlag=False
personFlag=False


cap = cv2.VideoCapture(r'C:\Users\hp\Pictures\combined.mp4')
_, frame1 = cap.read()
frame1=cv2.resize(frame1,(640,640))
_, frame2 = cap.read()
frame2=cv2.resize(frame2,(640,640))
th1=cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
_, th1 = cv2.threshold(th1, 170, 255, cv2.THRESH_BINARY)
th1=cv2.resize(th1,(40,40))
frameCount+=2

start=time.time()
end=time.time()
detStart=time.time()
detEnd=time.time()
multiCountStart=time.time()
multiCountEnd=time.time()
print(th1.shape)
key=1

while (cap.isOpened()):



    if((multiCountEnd-multiCountStart)>8):
        multiCountStart = time.time()
        multiCountEnd = time.time()
        countMul=0

    countZero = 0
    count255 = 0

    for i in range(40):
        for j in range(40):
            if(th1[i][j]==0):
                countZero+=1
            elif(th1[i][j]==255):
                count255+=1

    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)




    contourf = []
    contourff=[]

    for contour in contours:

        (x, y, w, h) = cv2.boundingRect(contour)
        if (cv2.contourArea(contour)) < 1000 or (cv2.contourArea(contour)) > 2500:
            continue
        else:
            contourf.append(contour)

    for contour in contourf:
        flag=True
        (x, y, w, h) = cv2.boundingRect(contour)
        if (len(contourff) == 0):
            contourff.append(contour)
        else:
            for cnt in contourff:
                xi,yi,wi,hi=cv2.boundingRect(cnt)
                if (abs(x - xi) <= width):
                    flag=False
                    break
                else:
                    continue
            if(flag):
                contourff.append(contour)

    xmin=640
    for cnt in contourff:
        (x, y, w, h) = cv2.boundingRect(cnt)
        if(x<xmin):
            xmin=x
    if (abs(xmin - tempPos) < 251):     
        countPos = countPos + 1
    else:
        countPos=0

    if (countPos == 3):
        countPos = 0
        pos = tempPos

    tempPos=xmin


    if((not(personFlag)) and (pos < 450) ):
        personFlag=True
        detStart=time.time()
    elif((personFlag) and (pos>500) and (pos < 639)):
        personFlag=False

    end = time.time()
    multiCountEnd=time.time()

    if(len(contourff)>1):
        countMul = countMul + 1
        print("countMul: "+str(countMul))
        if(countMul==3):
            multiWarningFlag=True

    cv2.arrowedLine(frame1,(635,250),(430,250),(255,0,0),10)
    cv2.putText(frame1, "ATM Entrance", (430, 230), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0, 0), 2)


    if(count255<300 or countZero<300):
        cv2.putText(frame1, "Camera View Obstructed", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    elif(multiWarningFlag):
        cv2.putText(frame1,"Multiple Person Detected",(10,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
        cv2.putText(frame1, "Press \'d\' to resume", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1)
        cv2.putText(frame1, "Time elapsed: "+str(end-start), (10, 170), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1)
    elif(personFlag and abs(end-detStart)>80):
        cv2.putText(frame1, "Person is taking unusually long time", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.putText(frame1, "Time elapsed: " + str(end - start), (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1)
    elif (personFlag):
        cv2.putText(frame1, "Person Detected inside ATM", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.putText(frame1, "Time elapsed: " + str(end - start), (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1)
    else:
        cv2.putText(frame1, "Press ESC to terminate: ", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.putText(frame1, "Time elapsed: " + str(end - start), (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1)


    cv2.imshow("live", frame1)
    frame1 = frame2
    _, frame2 = cap.read()
    frame2 = cv2.resize(frame2, (640, 640))

    th1=cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
    _, th1 = cv2.threshold(th1, 170, 255, cv2.THRESH_BINARY)
    th1 = cv2.resize(th1, (40, 40))
    frameCount+=1
    print(frameCount)


    k=cv2.waitKey(key)
    if (k == 27):
        break
    elif (k == ord('d')):
        multiWarningFlag=False
        countMul=0
cap.release()
cv2.destroyAllWindows()