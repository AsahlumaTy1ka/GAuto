import os
import json
#from mods import module



#htmlcont =  module.genCont()
htmlcont = open('file.md','r+')
markd = htmlcont.readlines()
if markd[0] == '':
  post_title = markd[1]
  htmlcont.seek(0)
  for li in markd:
  	if li != post_title:
  		htmlcont.write(li)
  htmlcont.truncate()
  htmlcont.close()
  		
else:
  post_title = markd[0]
  htmlcont.seek(0)
  for li in markd:
  	if li != post_title:
  		htmlcont.write(li)
  htmlcont.truncate()
  htmlcont.close()
  
#Labls = module.genLabels(post_title=post_title)
Labls =" [test,foo,hello world,john,doe]"
bannerPath = "/imgs/yee.png"
#bannerPath = module.generate_image(post_title=post_title)


def UpperFi(post_title,Labls,fname):

  upstr = f'''
---
layout: post
title: {post_title}
thumbnail-img: /assets/img/{fname}
share-img: /assets/img/{fname}
tags: {Labls}
author: Asahluma Tyika
---
'''
  return upstr  
 

upperText  = UpperFi(post_title,Labls,bannerPath)
with open("file.md","r") as f:
	lines = f.readlines()
lines[0] = lines[0].strip()+upperText+'\n'
with open("file.md","w") as f:
	f.writelines(lines)
	f.close

def create_post(markdown,img_name):
   pass
   

print(f"Title : {post_title}")
os.system("cat file.md")



