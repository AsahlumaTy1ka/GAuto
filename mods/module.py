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
    You are a tech blogger using Beautiful Jekyll by deanatalli. Write a single, original blog post in plain Markdown (no fenced code blocks), with the following requirements:

1. **Title**  
   - First line only: the post title, as plain text.  
   - No punctuation like commas, slashes or colons in the title.

2. **Length & Format**  
   - Minimum 1,100 words.  
   - Use Jekyll’s `{% highlight language linenos %}` … `{% endhighlight %}` for all code examples.  
   - Do not wrap the entire Markdown in a code block.

3. **Topic & Tone**  
   - Pick a tech topic that people actively search for—mix it up between:  
     - Practical coding tutorials (e.g., Python automation scripts)  
     - Emerging trends (e.g., AI tools, DevOps best practices, serverless architectures)  
     - Opinion pieces or deep dives (e.g., why code reviews matter, the ethics of AI)  
   - Avoid overusing “Mastering” in the title or headings; vary your verbs (e.g., “Exploring,” “Building,” “Automating,” “Understanding”).  
   - Write in an engaging, conversational tone that keeps readers scrolling.

4. **Structure**  
   - **Introduction**: Hook the reader with a real‑world problem or question.  
   - **Subheadings**: Break into clear sections (use `##` and `###`).  
   - **Code Examples**: Show copy‑and‑paste‑ready snippets using `{% highlight %}` tags.  
   - **Links to Your Site**: Whenever you reference a topic you’ve covered before, link to the specific GTec post (e.g. “See how we built a Termux script [here](https://gtec0.github.io/your-post-slug/)”).  
   - **Visual Aids**: Suggest where images or diagrams could go (e.g., `![diagram of workflow](path/to/image.png)`).

5. **SEO & Readability**  
   - Include 2–3 relevant keywords naturally in headings and body.  
   - Add a brief conclusion with a call to action (e.g., “Try this script and let me know your results in the comments!”).

6. **Originality**  
   - No repetition of existing GTec posts.  
   - Offer fresh insights or examples that differ from previous content.

Produce the finished Markdown post directly.```

Feel free to tweak any bullet or requirement—this should guide the AI to generate longer, more engaging, SEO‑friendly GTec articles without overusing “Mastering.”

    '''
    resp = model.generate_content(prompt)
    return resp.text



def genLabels(post_title):
    lblPrompt = f'Generate me labels for post with title {post_title} and return me a list,do not put it on code blocks ,return it like this example :[Label1,Label2,Labeln] . and it should not be greater than 4'
    model = genai.GenerativeModel('gemini-1.5-flash')
    labels = model.generate_content(lblPrompt)
    return labels.text


