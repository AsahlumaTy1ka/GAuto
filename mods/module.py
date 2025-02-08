import google.generativeai as genai
import os
from dotenv import load_dotenv
import string 
import random
from imagepig import ImagePig
import requests
load_dotenv()
myk = os.getenv('API_KEY')
genai.configure(api_key=myk)

# Generate an image
def generate_image(post_title):
    """
    Generates an image using the imagepig pipeline.
    """
    fname = str(''.join(random.choices(string.ascii_letters,k=7)))+ '.jpg'
    prompt = f"Image with title '{post_title}' ,blue and has coding icons"
    imagepig = ImagePig("9d526fa6-ad4e-4aea-9b2d-759e00721b0e")
    result = imagepig.flux(prompt)
    result.save(fname)
    return fname
    
    



def genCont():
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = '''Generate me a blog post about a random coding tutorial people or coders usually search about,markdown format and make it as long as possible(1000 words min) and do not take this as a chat plus dont put the markdown in a codeblock just return plain markdown and use {% highlight (language name here) linenos %} code here... {% endhighlight %} as codeblocks(this is an example) instead of code tags. Return the title of the post as just plain text at the beginning line and dont put special charecters like commas and slashes in it'''
    resp = model.generate_content(prompt)
    return resp.text



def genLabels(post_title):
    lblPrompt = f'Generate me labels for post with title {post_title} and return me a list,do not put it on code blocks ,return it like this example :[Label1,Label2,Labeln] . and it should not be greater than 4'
    model = genai.GenerativeModel('gemini-1.5-flash')
    labels = model.generate_content(lblPrompt)
    return labels.text


