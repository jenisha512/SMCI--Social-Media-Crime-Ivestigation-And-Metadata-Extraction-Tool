from PIL import Image
from PIL.ExifTags import TAGS

def get_exif_data(image_path):
    """Extracts available EXIF metadata from an image."""
    try:
        image = Image.open(image_path)
        exif_data = image.getexif()
        
        info_dict = {}
        if exif_data:
            for tag, value in exif_data.items():
                decoded = TAGS.get(tag, tag)
                # Filter out extremely long binary data (like thumbnails)
                if isinstance(value, bytes) and len(value) > 100:
                    value = "<Binary Data>"
                info_dict[decoded] = value
        
        if not info_dict:
            return {"Status": "No Metadata Found (Likely scrubbed by social media)"}
            
        return info_dict

    except Exception as e:
        return {"Error": str(e)}