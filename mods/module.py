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
 You’re a tech blogger using Beautiful Jekyll by deanatalli. Generate one original, 1100+-word tutorial post in plain Markdown (no fenced code blocks). Follow these rules:

1. Title  
   - First line only: the post title, plain text, no commas/slashes/colons.

2. Topic & Scope  
   - Pick a single, clear problem and show how to solve it end-to-end.  
   - Choose a domain not yet covered on GTEC (https://gtec0.github.io): e.g. containerizing apps with Docker & Kubernetes, securing a Node.js API, building a simple Go CLI, creating a Flutter widget, DevSecOps pipeline in GitHub Actions, or training a basic ML model in TensorFlow.  
   - Python automation may appear at most once per three posts—don’t let it dominate.

3. Language & Tools Diversity  
   - Use at least two different technologies or languages (e.g. Bash + JavaScript, Go + YAML, Flutter + Dart).  
   - Mention Python only if it adds value, but primary examples should use the chosen languages.

4. Structure & Formatting  
   - Introduction (3–5 sentences): hook with a real-world scenario and state the goal.  
   - Use `##` and `###` subheadings to break into logical sections.  
   - Keep paragraphs to 3–5 sentences each.  
   - Use bullet or numbered lists for step sequences or key points.  
   - Insert image placeholders where diagrams/screenshots would help:  
     `![alt text](path/to/image.png)`

5. Code Snippets  
   - Use `{% highlight <language> linenos %}` … `{% endhighlight %}` for every snippet.  
   - Ensure each snippet is copy-and-paste ready and explained in the adjacent text.

6. SEO & Readability  
   - Weave 2–3 relevant keywords naturally into headings and body (e.g. “Docker tutorial”, “Kubernetes deployment”, “DevSecOps pipeline”).  
   - Vary your verbs—e.g. “Building,” “Exploring,” “Automating,” “Securing,” “Deploying.”

7. Internal Linking  
   - Add 1–2 links to related GTEC posts or the homepage.  
     Example: `[See our Docker basics guide](https://gtec0.github.io/docker-basics/)`

8. Conclusion & CTA  
   - Summarize what the reader built or learned.  
   - End with a call-to-action: invite comments, social follows, or linking to another GTEC tutorial.
   
Produce the Markdown output directly.
     '''
    resp = model.generate_content(prompt)
    return resp.text



def genLabels(post_title):
    lblPrompt = f'Generate me labels for post with title {post_title} and return me a list,do not put it on code blocks ,return it like this example :[Label1,Label2,Labeln] . and it should not be greater than 4'
    model = genai.GenerativeModel('gemini-1.5-flash')
    labels = model.generate_content(lblPrompt)
    return labels.text


