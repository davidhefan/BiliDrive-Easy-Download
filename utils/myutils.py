import os
import cv2
import numpy as np

IS_RESIZE = 1
MAX_PIXEL = 3000

IS_REMOVE_BORDER = 1
BORDER_PIXEL = 40

# 遍历文件夹
def walkFile(file, file_paths, suffix):
    # print('111111: ', file)
    for root, dirs, files in os.walk(file):
        # print(root, dirs, files)
        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list

        # 遍历文件
        for f in files:
            # print(f)
            # if f.endswith('.xlsx') or f.endswith('.xls'):
            if f.endswith(suffix):
                # temp = f.split('.')
                file_paths.append((os.path.join(root, f), f, os.path.splitext(os.path.basename(os.path.join(root, f)))[0]))
                # print('file: ', os.path.join(root, f))
        # 遍历文件夹
        for dir in dirs:
            # print('dir: ', dir)
            walkFile(os.path.join(root, dir), file_paths, suffix)
        return file_paths

# walkExcelFile('/Users/davidhe/Downloads/source_res')

def compose_two_image_with_hstack(left, right):
    img1 = cv2.imread(left)
    img2 = cv2.imread(right)
    image = np.hstack((img1, img2))
    return image


def compose_two_image_with_vstack(up, down):
    img1 = cv2.imread(up)
    img2 = cv2.imread(down)
    image = np.vstack((img1, img2))
    return image


def compose_images_with_hstack(imgs):
    image = np.hstack((imgs))
    return image


def compose_images_with_vstack(imgs):
    image = np.vstack((imgs))
    return image


def compose_images_with_hstack_has_vertex(imgs):
    image = np.hstack((map(lambda x: x[0], imgs)))
    return image


def compose_images_with_vstack_has_vertex(imgs):
    image = np.vstack((list(map(lambda x: x[0], imgs))))
    return image

# 图片组拼接为一张图(背景白)
def compose_imgs_with_vstack_has_vertex(imgs):
    imgs = list(map(lambda x: x[0], imgs))
    max_width = 0  # find the max width of all the images
    total_height = 0  # the total height of the images (vertical stacking)
    channels = 3
    for img in imgs:
        if img.ndim == 2:  # 2维度表示长宽
            channels = 1  # 单通道(grayscale)
        if img.shape[1] > max_width:
            max_width = img.shape[1]
        total_height += img.shape[0]
    # create a new array with a size large enough to contain all the images
    if channels == 1:
        final_image = np.zeros((total_height, max_width), dtype=np.uint8)
    else:
        final_image = np.zeros((total_height, max_width, 3), dtype=np.uint8)
    final_image[:] = 255
    current_y = 0  # keep track of where your current image was last placed in the y coordinate
    for image in imgs:
        # add an image to the final array and increment the y coordinate
        if channels == 1:
            final_image[current_y:image.shape[0] + current_y, :image.shape[1]] = image
        else:
            final_image[current_y:image.shape[0] + current_y, :image.shape[1], :] = image
        current_y += image.shape[0]

    return final_image


# 图片组拼接为一张图（背景黑）
def compose_imgs_with_vstack_has_vertex_black(imgs):
    imgs = list(map(lambda x: x[0], imgs))
    max_width = 0  # find the max width of all the images
    total_height = 0  # the total height of the images (vertical stacking)
    channels = 3
    for img in imgs:
        if img.ndim == 2:  # 2维度表示长宽
            channels = 1  # 单通道(grayscale)
        if img.shape[1] > max_width:
            max_width = img.shape[1]
        total_height += img.shape[0]
    # create a new array with a size large enough to contain all the images
    if channels == 1:
        final_image = np.zeros((total_height, max_width), dtype=np.uint8)
    else:
        final_image = np.zeros((total_height, max_width, 3), dtype=np.uint8)
    final_image[:] = 0
    current_y = 0  # keep track of where your current image was last placed in the y coordinate
    for image in imgs:
        # add an image to the final array and increment the y coordinate
        if channels == 1:
            final_image[current_y:image.shape[0] + current_y, :image.shape[1]] = image
        else:
            final_image[current_y:image.shape[0] + current_y, :image.shape[1], :] = image
        current_y += image.shape[0]

    return final_image

# 改变图片大小
def resize_image(final_image):
    if IS_RESIZE:
        height, width = final_image.shape[0], final_image.shape[1]
        width_new, height_new = width, height
        # 判断图片的长宽比率
        if width >= height:
            if width > MAX_PIXEL:
                width_new = MAX_PIXEL
                height_new = int(height * MAX_PIXEL / width)
        else:
            if height > MAX_PIXEL:
                width_new = int(width * MAX_PIXEL / height)
                height_new = MAX_PIXEL
        final_image = cv2.resize(final_image, (width_new, height_new))

    return final_image

# 裁剪边框
def remove_boder_image(image):
    if IS_REMOVE_BORDER:
        height, width = image.shape[0], image.shape[1]
        image = image[BORDER_PIXEL: height-BORDER_PIXEL-1, BORDER_PIXEL: width-BORDER_PIXEL-1]
    return image