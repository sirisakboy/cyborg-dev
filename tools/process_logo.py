from PIL import Image

def process_logo(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    data = img.getdata()

    new_data = []
    # Project theme colors
    neon_blue = (0, 240, 255, 255) # #00F0FF
    
    for item in data:
        # If pixel is close to white (background), make it transparent
        if item[0] > 200 and item[1] > 200 and item[2] > 200:
            new_data.append((255, 255, 255, 0))
        else:
            # Otherwise, apply neon blue to all non-transparent pixels
            new_data.append(neon_blue)
            
    img.putdata(new_data)
    img.save(output_path, "PNG")
    print(f"Processed neon logo saved to: {output_path}")

if __name__ == "__main__":
    process_logo("manga_fix_logo.png", "cyborg_nexus_icon.png")
