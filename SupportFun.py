__author__ = 'randxie'

import math
import numpy as np
from PIL import Image,ImageDraw,ImageFont

# calculate Manhatan Distance
def Manhatan(node):
    count = 0
    for i in range(node.shape[0]):
        for j in range(node.shape[1]):
            if (node[i][j]!=0):
                count = count + abs(math.ceil(node[i][j]*1.0/node.shape[0])-1-i) + abs(((node[i][j]+node.shape[0]-1)%node.shape[1])-j)
    return count

# represent node (np.array) as string
def NodeRepr(node):
    return str(node)

# calculate neighbor of current node
def GetNeighbor(node):
    neighbor_list = []
    idx1 = np.where(node == 0)[0][0]
    idx2 = np.where(node == 0)[1][0]
    if idx1 != 0:
        tmp = node.copy()
        tmp[idx1-1][idx2], tmp[idx1][idx2] = tmp[idx1][idx2], tmp[idx1-1][idx2]
        neighbor_list.append(tmp)

    if idx2 != 0:
        tmp = node.copy()
        tmp[idx1][idx2-1], tmp[idx1][idx2] = tmp[idx1][idx2], tmp[idx1][idx2-1]
        neighbor_list.append(tmp)

    if idx1 != (node.shape[0]-1):
        tmp = node.copy()
        tmp[idx1][idx2], tmp[idx1+1][idx2] = tmp[idx1+1][idx2], tmp[idx1][idx2]
        neighbor_list.append(tmp)

    if idx2 != (node.shape[1]-1):
        tmp = node.copy()
        tmp[idx1][idx2], tmp[idx1][idx2+1] = tmp[idx1][idx2+1], tmp[idx1][idx2]
        neighbor_list.append(tmp)
    return neighbor_list

# transform node representation as PIL image
def GenImage(node):
    space = 40
    width = space*(node.shape[0]+2)
    height = space*(node.shape[1]+2)
    bgcolor = (255,255,255)
    font_width = 20
    image = Image.new('RGB',(width,height),bgcolor)
    font = ImageFont.truetype('FreeSans.ttf',font_width)
    fontcolor = (0,0,0)
    draw = ImageDraw.Draw(image)
    for i in range(node.shape[0]):
        for j in range(node.shape[1]):
            draw.text((space+i*space,space+j*space),str(node[j][i]),font=font,fill=fontcolor)
    return image