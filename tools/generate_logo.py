from PIL import Image, ImageDraw, ImageFont
import os

def create_manga_logo(text, output_path):
    # Canvas size
    width, height = 400, 200
    # High contrast B&W
    image = Image.new('L', (width, height), 255) # White background
    draw = ImageDraw.Draw(image)
    
    # Use one of the project's bold fonts
    font_path = 'assets/fonts/Lato-Heavy.ttf'
    if not os.path.exists(font_path):
        font = ImageFont.load_default()
    else:
        font = ImageFont.truetype(font_path, 80)
    
    # Calculate text position
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    
    # Draw Manga Shadow (Offset)
    shadow_offset = 6
    draw.text((x + shadow_offset, y + shadow_offset), text, font=font, fill=0)
    
    # Draw Thick Outline
    outline_range = 3
    for dx in range(-outline_range, outline_range + 1):
        for dy in range(-outline_range, outline_range + 1):
            draw.text((x + dx, y + dy), text, font=font, fill=0)
            
    # Draw Main Text (White to cut through the outline)
    draw.text((x, y), text, font=font, fill=255)
    
    # Draw inner black text for final manga look
    draw.text((x, y), text, font=font, fill=0)

    image.save(output_path)
    print(f"Manga logo saved to: {output_path}")

if __name__ == "__main__":
    create_manga_logo("FIX!!", "manga_fix_logo.png")
