import cv2

p = cv2.imread("poster.jpg")

rocket = p[120:360,400:500]
p[0:240,500:600] = rocket
ttc = "I love to code"
cv2.putText(p, ttc, (20, 220),  
            fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 1,  
            color=(0,0,255)
           )

cv2.imshow("Poster", p)

# Copying image into another file
cv2.imwrite("Greetings.jpg", p)

print(p)
cv2.waitKey(0)