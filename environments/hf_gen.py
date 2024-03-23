import numpy as np
import cv2

filename= "/Users/nishanacharya/Desktop/rl_project/environments/hf.png"

N = 64
M = 12
div = 2
mat = np.random.randint(0, 255, size=(M//div,N//div), dtype=np.uint8).repeat(div, axis=0).repeat(div, axis=1)
#mat[N//2 - 4: N//2 + 4, N//2 - 4: N//2 + 4] = 255
cv2.imwrite(filename, mat)

# N = 64
# M = 12
# div = 2
# mat = np.random.randint(0, 255, size=(M//div,N//div), dtype=np.uint8).repeat(div, axis=0).repeat(div, axis=1)
# for i in range(10):
    #   filename= "/Users/nishanacharya/Desktop/rl_project/environments/hf' + f'{i}'+ '.png"
    #   cv2.imwrite(filename, (float(i/10)*mat))
    #   smoothening = [ 0.1 0.01 0.001]