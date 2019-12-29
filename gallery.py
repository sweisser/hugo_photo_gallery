#!/usr/bin/python
import sys
import os
from datetime import datetime

# Examples:
# 
# python3 gallery.py <galleryname> <picture_source_folder>

hugo_site_dir = "/home/stefan/Documents/homepage_hugo"

hugo_gallery_postname = sys.argv[1]
picture_source_folder = sys.argv[2]
hugo_post_path = hugo_site_dir + "/content/posts/" + hugo_gallery_postname
hugo_post_index= hugo_site_dir + "/content/posts/" + hugo_gallery_postname + "/index.md"
hugo_post_index2 = "posts/" + hugo_gallery_postname + "/index.md"

# Generate and execute hugo command
def generate_post_directory():
    cmd = "cd " + hugo_site_dir + "; " + "hugo new " + hugo_post_index2
    print(cmd)
    os.system(cmd)

# Generate and execute copy commands
def copy_images():
    for (file_short, file_long) in files:
        target = os.path.join(hugo_post_path, file_short)
        cmd = "cp %s %s" % (file_long, target)
        print("Copying file %s", file_long)
        os.system(cmd)

# Write index.md
def write_post_index(content):
    f = open(hugo_post_index, "w")
    f.write(content)

    for (file_short, file_long) in files:
        # If you need more logic, add here
        hugo_image_relpath = file_short
        line = "![%s](%s)\n" % (file_short, hugo_image_relpath) 
        f.write(line)
    f.close()

# Generate hugo index.md
# Some of the metadata here is used for the 'aether' theme, that I use for hugo.
def generate_post_content():
    featured_image_name = files[0][0]
    today = datetime.utcnow()
    content = """---
title: "%s"
categories: []
date: %s
dropCap: true
displayInMenu: false
displayInList: true
draft: true
resources:
- name: featuredImage
  src: "%s"
  params:
    description: "%s"
---
""" % (hugo_gallery_postname, today, featured_image_name, featured_image_name)
    return content


print("Gallery name:         %s" % (hugo_gallery_postname))
print("Hugo site dir:        %s" % (hugo_site_dir))
print("Using image_path:     %s" % (picture_source_folder))
print("Using hugo_post_path: %s" % (hugo_post_path))

ready = input("Ready to rumble (y/n)?")
if (ready == 'y'):
    # Collect tuples here
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(picture_source_folder):
        for file in f:
            if '.png' in file or '.jpg' in file or '.JPG' in file:
                file_long = os.path.join(r, file)
                file_short = file
                files.append((file_short, file_long))

    generate_post_directory()
    copy_images()
    content = generate_post_content()
    write_post_index(content)
