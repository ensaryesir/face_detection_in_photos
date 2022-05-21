import cv2

#face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") #nesne oluşturduk
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml") #ilkinde hata alınca bunu kullandım düzeldi

img = cv2.imread("C:\\Users\\ensar\\Desktop\Kodlama Egzersizleri\\Projelerim\\face for cv2 projects\\arwen.jpg") #fotoyu yükleme
#img = cv2.imread("C:\\Users\\ensar\\Desktop\Kodlama Egzersizleri\\Projelerim\\face for cv2 projects\\number 1.jpg")

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)

print(type(faces))
print(faces)

for x,y,w,h in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0),5)

resized_image = cv2.resize(img, (1200,800)) #şekli boyutlandırma
#resized_image = cv2.resize(img, (int(img.shape[1]/1), int(img.shape[0]/1))) #şekli boyutlandırma 2.yöntem

cv2.imshow("Face detection in photos",resized_image)
cv2.waitKey(0)
cv2.destroyWindow()


