import glob
import markdown
import os
import requests
from markdown.treeprocessors import Treeprocessor
from markdown.extensions import Extension

from pymagecli.s3 import S3
from pymagecli.utils import get_file_and_resize

def get_file_link_list(file_name):

    class ImgExtractor(Treeprocessor):
        def run(self, doc):
            "Find all images and append to markdown.images. "
            self.markdown.images = []
            for image in doc.findall('.//img'):
                self.markdown.images.append(image.get('src'))

    class ImgExtExtension(Extension):
        def extendMarkdown(self, md, md_globals):
            img_ext = ImgExtractor(md)
            md.treeprocessors.add('imgext', img_ext, '>inline')

    md = markdown.Markdown(extensions=[ImgExtExtension()])
    with open(file_name) as f:
        content = f.read()
        if 'googleusercontent.com' in content:
            md.convert(content)
            return md.images
    return []

def get_all_files_in_dir(directory_path):
    return glob.glob(os.path.join(directory_path, '*.md'))


def fetch_photo_and_save_to_s3(bucket_name, photo_url):
    if 'googleusercontent.com' in photo_url:
        s3 = S3()
        key = photo_url.split("/")[-1]
        try:
            r = requests.get(photo_url, allow_redirects=True)
            s3.put_object(bucket_name=bucket_name, key=key, body=r.content)
            print("Resizing: {} Bucket: {}".format(key, bucket_name))
            get_file_and_resize(bucket_name=bucket_name, file_name=key)
            return key
        except Exception as e:
            print("fetch_photo_and_save_to_s3: failed to get file: {} error: {}".format(photo_url, e))
            return None
    else:
        print("fetch_photo_and_save_to_s3: skipping: {}".format(photo_url))
        return None


def inplace_change(filename, old_string, new_string):
    with open(filename) as f:
        s = f.read()
        if old_string not in s:
            return

    with open(filename, 'w') as f:
        s = s.replace(old_string, new_string)
        f.write(s)


def move_all_photos(bucket_name, directory_path, base_url):
    all_files = get_all_files_in_dir(directory_path=directory_path)
    for file_name in all_files:
        print("FILE: {}".format(file_name))
        link_list = get_file_link_list(file_name=file_name)
        for link in link_list:
            key = fetch_photo_and_save_to_s3(bucket_name=bucket_name, photo_url=link)
            if key:
                new_url = "{}/{}".format(base_url, key)
                inplace_change(filename=file_name, old_string=link, new_string=new_url)


def move_all_photos_file(bucket_name, file_name, base_url):
    print("FILE: {}".format(file_name))
    link_list = get_file_link_list(file_name=file_name)
    for link in link_list:
        key = fetch_photo_and_save_to_s3(bucket_name=bucket_name, photo_url=link)
        if key:
            new_url = "{}/{}".format(base_url, key)
            inplace_change(filename=file_name, old_string=link, new_string=new_url)
