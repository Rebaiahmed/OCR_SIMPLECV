import cv2


def captch_ex(file_name) :

     #Read the image with opencv
     img = cv2.imread(file_name)

     print img
     #image final
     img_final = cv2.imread(file_name)
     img2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
     ret , mask = cv2.threshold(img2gray, 180, 255, cv2.THRESH_BINARY)
     image_final = cv2.bitwise_and(img2gray, img2gray, mask=mask)
     ret, new_img = cv2.threshold(image_final, 180, 255, cv2.THRESH_BINARY)

     #Supprimeer Noise ***???????
     kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
     dilated = cv2.dilate(new_img,kernel,iterations=9)

     contours, hierarchy = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

     for contour in contours :
         [x,y,w,h] = cv2.boundingRect(contour)


         if w< 35 and h <35 :
             continue


          #Draw rectangle****************
             cv2.rectangle(img,(x, y), (x + w, y + h), (255, 0, 255), 2)


             #write original image
             cv2.imshow('captcha_result',img)
             cv2.waitKey()



file_name = 'ahmed.jpg'
captch_ex(file_name)
