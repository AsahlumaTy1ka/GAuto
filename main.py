import os
import json
from datetime import datetime
from mods import module
from github import Github
from dotenv import load_dotenv
import base64
from time import sleep

# Load environment variables
load_dotenv()

# Generate content and write to the content.md file
htmlcont1 = module.genCont()
with open("content.md", "w") as f:
    f.write(htmlcont1)

# Read content from the content.md file
with open('content.md', 'r+') as htmlcont:
    markd = htmlcont.readlines()

    # Handle the case where the first line is empty
    if markd[0] == '':
        post_title = markd[1]
        htmlcont.seek(0)
        for li in markd:
            if li != post_title:
                htmlcont.write(li)
        htmlcont.truncate()
    else:
        post_title = markd[0]
        htmlcont.seek(0)
        for li in markd:
            if li != post_title:
                htmlcont.write(li)
        htmlcont.truncate()

# Generate labels and banner path
Labls = module.genLabels(post_title=post_title).strip("\n")
bannerPath = module.generate_image(post_title=post_title)

# Function to create the upper part of the post
def UpperFi(post_title, Labls, fname):
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

# Write the upper part to the content.md file
upperText = UpperFi(post_title.strip("\n"), Labls, bannerPath)
with open("content.md", "r") as f:
    lines = f.readlines()

lines[0] = lines[0].strip() + upperText + '\n'

with open("content.md", "w") as f:
    f.writelines(lines)

# Function to create the post on GitHub
def create_post(mdfile, post_t, img_name):
    with open(mdfile, "r") as f:
        data = f.read()

    # Generate filename using current date and post title
    time = datetime.now()
    title = post_t.replace(" ", "-")
    filename = time.strftime("%Y") + "-" + time.strftime("%m") + "-" + time.strftime("%d") + "-" + title.strip("\n") + ".md"
    filename = filename.strip("\n")

    print(f" : {filename}")
    print("[+] Done! ,pushing to github...")

    # Push to GitHub
    key = os.getenv("gh_Key")
    g = Github(key)
    repo = g.get_repo("GTec0/gtec0.github.io")

    # Create the post file on GitHub
    repo.create_file(f"_posts/{filename}", "create post", data, branch="master")
    print("Content :  " + data)
    print("[+] Post created!")

    # Remove the content.md file locally
    os.system("rm -rf content.md")
    print("[+] File deleted!")

    sleep(120)

    # Upload the banner image to GitHub
    with open(img_name, "rb") as img:
        bytes = img.read()

    repo.create_file(f"assets/img/{img_name}", "upload img", bytes, branch="master")
    print("[+] Banner image uploaded!")

# Call create_post to push the content and banner image to GitHub
print(f"Banner path: {bannerPath}")
create_post("content.md", post_title, bannerPath)
