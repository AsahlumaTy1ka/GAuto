import os
import json
from mods import module

blog_id = 7302333189972766248




#htmlcont =  module.genCont()
htmlcont = open('./file.html','r+')
markd = htmlcont.readlines()
if markd[0] == '':
  post_title = markd[1]
else:
  post_title = markd[0]
Labls = module.genLabels(post_title=post_title)
bannerPath = ""
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
  
# Define the SCOPES
SCOPES = ['https://www.googleapis.com/auth/blogger']


def postCont(blog_id, title, content, schedule_post=False, schedule_time=None):
    """
    Posts content to a Blogger blog and optionally schedules weekly posts.

    Parameters:
        blog_id (str): The ID of the Blogger blog.
        title (str): The title of the blog post.
        content (str): The content of the blog post in HTML format.
        schedule_post (bool): Whether to schedule the post weekly. Default is False.
        schedule_time (str): Time to post if scheduling, in HH:MM (24-hour) format. Default is None.
    """


def create_post(markdown,img_name):
   pass

print(f"Labels : {Labls}")
#print(f"Banner Path : {bannerPath}")
create_post(sevice, blog_id, post_title, post_body,Labls)


