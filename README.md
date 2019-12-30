# hugo_photo_gallery
A little python script that helps me to create a photo gallery post from an image directory.

# Preparation
Change the hugo_site_dir variable inside the gallery.py to your hugo site folder.

# Create a gallery
Run the gallery.py script:

  python3 gallery.py <galleryname> <picture_source_folder>

The script will create a new post using the hugo command.
It will then copy all the images (jpg, png, JPG) to the new posts folder.
It will create an index.md inside the posts folder with all the images.
