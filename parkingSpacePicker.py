import cv2 as cv
import pickle

img=cv.imread('carParkImg.png')

width,height=107,48

try :
    with open('carParkPos','rb') as f :
        positionList=pickle.load(f)
except:
    positionList=[]

def mouseClick(events,x,y,flags , params):
    if events==cv.EVENT_LBUTTONDOWN:
        positionList.append((x,y))
    if events==cv.EVENT_RBUTTONDOWN:
        for i,pos in enumerate(positionList):
            x1,y1=pos
            if x1<x<x1+width and y1<y<y1+width:
                positionList.pop(i)
    
    with open('carParkPos','wb') as f:
        pickle.dump(positionList,f)

while True:
    img=cv.imread('carParkImg.png')
    for pos in positionList:
        cv.rectangle(img,pos,(pos[0]+width,pos[1]+height) ,(255,0,255),2)
    cv.imshow('Image',img)

    cv.setMouseCallback('Image',mouseClick)
    cv.waitKey(1)


