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
    prompt = ''' 
You’re a tech blogger using Beautiful Jekyll by deanatalli. Generate one fresh, original blog post in plain Markdown (no fenced code blocks), with these rules:

1. Title  
   - On the very first line, output only the post title (plain text, no commas/slashes/colons).

2. Length & Markup  
   - At least 1,500 words.  
   - Use `{% highlight <language> linenos %}` … `{% endhighlight %}` for code.  
   - Don’t wrap the whole thing in a code-block.

3. Topic Selection (pick exactly one)  
   - 🔲 **Emerging AI & ML** (new open-source models, fine-tuning, ethical implications)  
   - 🔲 **JavaScript Frameworks** (React/Next.js tips, Svelte, real-world case studies)  
   - 🔲 **Cloud & DevOps** (Kubernetes patterns, serverless best practices, CI/CD pipelines)  
   - 🔲 **Mobile Development** (Flutter, React Native, PWA tricks)  
   - 🔲 **Cybersecurity** (hands-on pentesting, DevSecOps, secure coding)  
   - 🔲 **Data Science & Visualization** (Pandas alternatives, interactive dashboards)  
   - 🔲 **IoT & Hardware Hacks** (Raspberry Pi, Arduino projects)  

   _Only one in every three posts may be Python automation._  

4. Structure  
   - **Introduction**: Hook with a real problem or question.  
   - **Sections**: Use `##`/`###` headings.  
   - **Code Snippets**: Ready-to-copy with `{% highlight %}`.  
   - **Internal Links**: When you refer to something you’ve covered on GTec, link to it (e.g. `[See our React hooks guide](https://gtec0.github.io/2025-04-20-hooks-react-guide/)`).  

5. SEO & Engagement  
   - Sprinkle 2–3 relevant keywords in headings/body.  
   - Vary verbs: “Exploring,” “Building,” “Automating,” “Understanding.”  
   - End with a **Conclusion + Call to Action**.

6. Originality  
   - Never repeat an existing GTec topic.  
   - Bring fresh examples or data.

Produce the Markdown output directly. 
    '''
    resp = model.generate_content(prompt)
    return resp.text



def genLabels(post_title):
    lblPrompt = f'Generate me labels for post with title {post_title} and return me a list,do not put it on code blocks ,return it like this example :[Label1,Label2,Labeln] . and it should not be greater than 4'
    model = genai.GenerativeModel('gemini-1.5-flash')
    labels = model.generate_content(lblPrompt)
    return labels.text


