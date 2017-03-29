import requests
from bs4 import BeautifulSoup
import urlparse

def images():
    url = "https://www.walmart.com/ip/54649026"
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    
  
    image = []

    # This will look for a meta tag with the og:image property
    og_image = (soup.find('meta', property='og:image') or
                        soup.find('meta', attrs={'name': 'og:image'}))
    if og_image and og_image['content']:
        print og_image['content']
        pass
        #image.append(og_image['content'])
        
    
    # This will look for a link tag with a rel attribute set to 'image_src'
    thumbnail_spec = soup.find('link', rel='image_src')
    if thumbnail_spec and thumbnail_spec['href']:
        print thumbnail_spec['href']
        #print ''
        pass
        #image.append(thumbnail_spec['href'])
        
        
        for ima in soup.findAll("img", src=True):
            image.appends(image["src"])
        
    
        return image
       
print images()
        
