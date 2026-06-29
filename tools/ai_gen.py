import requests
import sys
import os
import urllib.parse
from datetime import datetime

def generate_ai_image(prompt, output_dir="generated_images"):
    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Enhance prompt for Manga style (Customizable)
    enhanced_prompt = f"{prompt}, manga style, high contrast, black and white, professional illustration"
    encoded_prompt = urllib.parse.quote(enhanced_prompt)
    
    # Using Pollinations.ai Image URL structure
    # Adding a random seed to ensure uniqueness and bypass cache
    import random
    seed = random.randint(0, 999999)
    url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1024&height=1024&seed={seed}&model=flux&nologo=true"
    
    print(f"🎨 Generating image for: '{prompt}'...")
    
    try:
        # Important: Use stream=True to handle large binary files
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            # Check content type to ensure it's an image
            content_type = response.headers.get('content-type', '')
            if 'image' not in content_type:
                print(f"⚠️ Warning: Received unexpected content type: {content_type}")
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"gen_{timestamp}.png"
            filepath = os.path.join(output_dir, filename)
            
            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            print(f"✅ Success! Image saved to: {filepath}")
            return filepath
        else:
            print(f"❌ Error: Failed to generate image (Status: {response.status_code})")
    except Exception as e:
        print(f"❌ Connection Error: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ai_gen.py 'your prompt here'")
    else:
        user_prompt = sys.argv[1]
        generate_ai_image(user_prompt)
