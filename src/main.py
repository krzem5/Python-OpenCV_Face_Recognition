import cv2



face=cv2.CascadeClassifier("face.xml")
eye=cv2.CascadeClassifier("eye.xml")
cap=cv2.VideoCapture(0)
while (True):
	ret,img=cap.read()
	gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	faces=face.detectMultiScale(gray,1.3,5)
	for (x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
		g=gray[y:y+h,x:x+w]
		c=img[y:y+h,x:x+w]
		eyes=eye.detectMultiScale(g)
		for (ex,ey,ew,eh) in eyes:
			cv2.rectangle(c,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
	cv2.imshow("img",img)
	if ((cv2.waitKey(1)&0xff)==27):
		break
cap.release()
cv2.destroyAllWindows()
