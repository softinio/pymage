import PIL
from PIL import Image as PILImage
from io import BytesIO


class Image(object):
    def resize_image(self, body, extension, width):
        """
        Resize and optimize image
        :param body: the image
        :param extension: image type ('.png' or '.jpg' or '.jpeg')
        :param width: image width
        :return: bytesIO with image resized
        """
        try:
            img = PILImage.open(BytesIO(body))
            wpercent = (width / float(img.size[0]))
            hsize = int((float(img.size[1]) * float(wpercent)))
            img = img.resize((width, hsize), PIL.Image.ANTIALIAS)

            buffer = BytesIO()

            if extension in ['.jpeg', '.jpg']:
                format = 'JPEG'
                img.save(buffer, format, quality=85, optimize=True)
            if extension in ['.png']:
                format = 'PNG'
                img.save(buffer, format, optimize=True)

            buffer.seek(0)

            return buffer
        except Exception as e:
            message = "resize_image FAIL: {}".format(e)
            print(message)
            return None

