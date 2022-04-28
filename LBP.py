import cv2


def Local_Binary_Pattern(gray):
    newImage = gray.copy()
    row, column = gray.shape
    for r in range(row):
        for c in range(column):
            computing_val = 0
            if (r >= 1) and (c >= 1) and (r + 1 < row) and (c + 1 < column):
                if gray[r - 1][c - 1] >= gray[r][c]:    # top left
                    computing_val += 1
                if gray[r - 1][c] >= gray[r][c]:        # top
                    computing_val += 2
                if gray[r - 1][c + 1] >= gray[r][c]:    # top right
                    computing_val += 4
                if gray[r][c + 1] >= gray[r][c]:        # right
                    computing_val += 8
                if gray[r + 1][c + 1] >= gray[r][c]:    # bottom right
                    computing_val += 16
                if gray[r + 1][c] >= gray[r][c]:        # bottom
                    computing_val += 32
                if gray[r + 1][c - 1] >= gray[r][c]:    # bottom left
                    computing_val += 64
                if gray[r][c - 1] >= gray[r][c]:        # left
                    computing_val += 128
                newImage[r][c] = computing_val
                # print(newImage[r][c])
            else:
                continue
    return newImage


"""
    [x-1][y-1] [x-1][y] [x-1][y+1]
    [x][y-1]   [x][y]   [x][y+1]
    [x+1][y-1] [x+1][y] [x+1][y+1] 
"""

image_path = input('Enter path of the image: ')
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#x, y = gray.shape
#print(x, " x -> y ", y)

calculated_image = Local_Binary_Pattern(gray)
# print(calculated_image)

cv2.imshow('Local Binary Pattern on the image', calculated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

name_to_save = input('Enter the name for the new image: ')
cv2.imwrite(name_to_save, calculated_image)
