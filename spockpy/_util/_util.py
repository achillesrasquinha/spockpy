from PIL import Image

def _resize_image(image, size, maintain_aspect_ratio = False):
    width, height = image.size

    if maintain_aspect_ratio:
        aspect_ratio = width / height

        if min(width, height) is width:
            width  = size[0]
            height = width  / aspect_ratio
        else:
            height = size[1]
            width  = height * aspect_ratio

    copy          = image.copy()

    copy.thumbnail((width, height), Image.ANTIALIAS)

    return copy