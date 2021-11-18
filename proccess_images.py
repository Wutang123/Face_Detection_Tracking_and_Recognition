from PIL import Image
import os


def rename_dir(name, images):
    for i, filename in enumerate(os.listdir(images)):
        os.rename(images + "/" + filename, images + "/" + name + "_" + str(i) + ".jpg")

def resize_dir(name, dir_orig, dir_resize):
    for count, filename in enumerate (os.listdir(dir_orig)):
        orig_filepath = os.path.join(dir_orig, filename)
        image = Image.open(orig_filepath)
        image = image.convert('RGB')
        image = image.resize((640, 640))
        image_name = "Justin_" + str(count) + ".jpg"
        new_filepath = os.path.join(dir_resize, image_name)
        image.save(new_filepath)

def main():
    name   = "Justin"
    images = "images"
    resize = "resize_images"

    # Program does not work on .HEIC files
    #rename_dir(name, images)       # Will replace the original file name
    #resize_dir(name, images, resize)

if __name__ == "__main__":
    main()