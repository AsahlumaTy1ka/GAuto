import os
import json
from datetime import datetime
from mods import module
from github import Github
from dotenv import load_dotenv
import base64
load_dotenv()

htmlcont1 =  module.genCont()
with open("content.md","w") as f:
	f.write(htmlcont1)
	f.close()
htmlcont = open('content.md','r+')
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
  
Labls = module.genLabels(post_title=post_title)
#Labls =" [test,foo,hello world,john,doe]"
#bannerPath = "img.jpg"
bannerPath = module.generate_image(post_title=post_title)


def UpperFi(post_title,Labls,fname):

  upstr = f'''---
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
with open("content.md","r") as f:
	lines = f.readlines()
lines[0] = lines[0].strip()+upperText+'\n'
with open("content.md","w") as f:
	f.writelines(lines)
	f.close

def create_post(mdfile,post_t,img_name):
   with open(mdfile,"r") as f:
   	data = f.read()
   time = datetime.now()
   title = post_t.replace(" ","-")
   filename = time.strftime("%Y")+"-"+time.strftime("%m")+"-"+time.strftime("%d")+"-"+title.strip("\n")+".md"
   filename = filename.strip("\n")
   print(f" : {filename}")
   #os.rename(mdfile,filename)
   print("[+] Done! ,pushing to github...")
   #push to github
   key = os.getenv("gh_Key")
   g = Github(key)
   repo = g.get_repo("GTec0/gtec0.github.io")
   
   repo.create_file(f"_posts/{filename}","create post",data,branch="master")
   print("Content :  "+data)
   print("[+] post created!")
   os.system("rm -rf content.md")
   print("[+] File deleted!")
   with open(img_name,"rb") as img:
   	bytes = img.read()
   	b64_data = base64.b64encode(bytes)
   repo.create_file(f"assets/img/{img_name}","upload img",b64_data,branch="master")
   print("[+] Banner image uploaded!")
   
print(f"Banner path : {bannerPath}")   
create_post("content.md",post_title,bannerPath)



