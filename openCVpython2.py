import cv2
 
cap = cv2.VideoCapture('./ch02_20180914132057.mp4')
 
fps = cap.get(cv2.CAP_PROP_FPS)  # 获取帧速
print(fps)
fWidth = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
print(fWidth)
 
fHeight = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(fHeight)
 
fNums = cap.get(cv2.CAP_PROP_FRAME_COUNT)
print(fNums)

success,frame = cap.read()
i = 0
while(i<6876):
    #success,frame = cap.read()
    if(i>6825):
        success,arr = cv2.imencode('.jpg', frame)
        a = arr.tostring()
        fp = open('./ch02_20180914132057/'+str(i)+'.jpg', 'wb')
        fp.write(a)
        fp.close()
    i = i + 1
    success,frame = cap.read()
