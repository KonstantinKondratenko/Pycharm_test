import cv2
import numpy as np
import PIL   

from task5 import solve5

  


if __name__ == '__main__':

    img = cv2.imread('./img/sm_simp.png')
    # cv2.imshow('data image',img)
    # cv2.waitKey(0)
    
    data_np = np.array(img)
  
    result = solve5(data_np, 2, 255)
    
    cv2.imshow('result image 1', result)
    cv2.waitKey(0)

