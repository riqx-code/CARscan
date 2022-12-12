

from shapely.geometry import Polygon
import json 
import cv2 as cv



# import Images using json file
f1 = open('1.json')
f2 = open('2.json')
f3 = open('3.json')
f4 = open('4.json')
f5 = open('5.json')
fd1 = open('1d.json')
fd2 = open('2d.json')
fd3 = open('3d.json')
fd4 = open('4d.json')
fd5 = open('5d.json')

# load images
d1 = json.load(f1)
d2 = json.load(f2)
d3 = json.load(f3)
d4 = json.load(f4)
d5 = json.load(f5)
dd1 = json.load(fd1)
dd2 = json.load(fd2)
dd3 = json.load(fd3)
dd4 = json.load(fd4)
dd5 = json.load(fd5)


# list of parts of all cars

# car part list 
cpart = []
# first car parts 
l = []
for i in range(len(d1)):
    l.append(d1[i]['value']['points'])
    if i == len(d1)-1:
      cpart.append(l)
      l=[]
# second car parts
l = []
for i in range(len(d2)):
    l.append(d2[i]['value']['points'])
    if i == len(d2)-1:
      cpart.append(l)
      l=[]
# third car parts
l = []
for i in range(len(d3)):
    l.append(d3[i]['value']['points'])
    if i == len(d3)-1:
      cpart.append(l)
      l=[]
# fourth car parts
l = []
for i in range(len(d4)):
    l.append(d4[i]['value']['points'])
    if i == len(d4)-1:
      cpart.append(l)
      l=[]
# fifth car part
l = []
for i in range(len(d5)):
    l.append(d5[i]['value']['points'])
    if i == len(d5)-1:
      cpart.append(l)
      l=[]



# list of damage area of all cars

# car part list 
cdpart = []
# first car damage area
l = []
for i in range(len(dd1)):
    l.append(dd1[i]['value']['points'])
    if i == len(dd1)-1:
      cdpart.append(l)
      l=[]
# second car damage area
l = []
for i in range(len(dd2)):
    l.append(dd2[i]['value']['points'])
    if i == len(dd2)-1:
      cdpart.append(l)
      l=[]
# third car damage area
l = []
for i in range(len(dd3)):
    l.append(dd3[i]['value']['points'])
    if i == len(dd3)-1:
      cdpart.append(l)
      l=[]
# fourth car damage area
l = []
for i in range(len(dd4)):
    l.append(dd4[i]['value']['points'])
    if i == len(dd4)-1:
      cdpart.append(l)
      l=[]
# fifth car damage area
l = []
for i in range(len(dd5)):
    l.append(dd5[i]['value']['points'])
    if i == len(dd5)-1:
      cdpart.append(l)
      l=[]



# list of parts  name of all cars

# car part name list 
cname = []
# first car parts area
l = []
for i in range(len(d1)):
    l.append(d1[i]['value']['polygonlabels'][0])
    if i == len(d1)-1:
      cname.append(l)
      l=[]
# second car parts area
l = []
for i in range(len(d2)):
    l.append(d2[i]['value']['polygonlabels'][0])
    if i == len(d2)-1:
      cname.append(l)
      l=[]
# third car parts area
l = []
for i in range(len(d3)):
    l.append(d3[i]['value']['polygonlabels'][0])
    if i == len(d3)-1:
      cname.append(l)
      l=[]
# fourth car parts area
l = []
for i in range(len(d4)):
    l.append(d4[i]['value']['polygonlabels'][0])
    if i == len(d4)-1:
      cname.append(l)
      l=[]
# fifth car part area
l = []
for i in range(len(d5)):
    l.append(d5[i]['value']['polygonlabels'][0])
    if i == len(d5)-1:
      cname.append(l)
      l=[]

"""# IMAGE LOAD"""

""" This code is manually adding position of damage : this is done because of a mistake in Data provided , please look at Notebook of 
Task 1 for more clarity"""

#now manually add side of the car by looking at image : for bonus task 

# # image load

# img1 = cv.imread('/content/drive/MyDrive/images/1.jpg')
# img2 = cv.imread('/content/drive/MyDrive/images/2.jpg')
# img3 = cv.imread('/content/drive/MyDrive/images/3.jpg')
# img4 = cv.imread('/content/drive/MyDrive/images/4.jpg')
# img5 = cv.imread('/content/drive/MyDrive/images/5.jpg')

# cv.imshow(img1)

# cname[0].append('backside')

# cv.imshow(img3)

# cname[2].append('drive-front-side')

# cv.imshow(img4)

# cname[3].append('driver-back-side')

# cv.imshow(img5)

# cname[4].append('passenger-front-side')





# list of damage type of all cars

# car damage type list 
damtype = []
# first car damage type
l = []
for i in range(len(dd1)):
    l.append(dd1[i]['value']['polygonlabels'][0])
    if i == len(dd1)-1:
      damtype.append(l)
      l=[]
# second car damage type
l = []
for i in range(len(dd2)):
    l.append(dd2[i]['value']['polygonlabels'][0])
    if i == len(dd2)-1:
      damtype.append(l)
      l=[]
# third car damage type
l = []
for i in range(len(dd3)):
    l.append(dd3[i]['value']['polygonlabels'][0])
    if i == len(dd3)-1:
      damtype.append(l)
      l=[]
# fourth car damage type
l = []
for i in range(len(dd4)):
    l.append(dd4[i]['value']['polygonlabels'][0])
    if i == len(dd4)-1:
      damtype.append(l)
      l=[]
# fifth car damage type
l = []
for i in range(len(dd5)):
    l.append(dd5[i]['value']['polygonlabels'][0])
    if i == len(dd5)-1:
      damtype.append(l)
      l=[]



"""# Damage Area calculation using overlapping """

def inter(l1,l2):
  p = Polygon(l1)
  q = Polygon(l2)
  return p.intersection(q).area

damageinfo = []

for i in range(5):
  l = []
  for j in range(len(cdpart[i])):
    for k in range(len(cpart[i])):
      x = inter(cpart[i][k],cdpart[i][j])
      if(x != 0):
        carpart_poly = Polygon(cpart[i][k])
        carpart_area = carpart_poly.area
        li = {}
        li['damage_area'] = x
        li['damage_area_percent'] = (x/carpart_area)*100
        li['damage_at'] = cname[i][k]
        li['damage_type'] = damtype[i][j]
        l.append(li)
  
  l.append(len(l))
  damageinfo.append(l)




# Data Printing

for i in range(len(damageinfo)):
  print(f"car number {i+1} ")
  l = damageinfo[i]
  for j in range(len(l)-1):
    print(f"In car-{i+1} , damage no :{j+1} , damage_area :   {l[j]['damage_area']} , damage_percent : {l[j]['damage_area_percent']}%  at  {l[j]['damage_at']}     of type    {l[j]['damage_type']} ")
  print('\n')



