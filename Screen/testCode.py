for i in range(1, len(pos_list[0])):
    cv2.circle(img, (pos_list[1][i], pos_list[0][i]), 4, (0, 255, 0), -1)
    cv2.imwrite("image1.jpg", img)