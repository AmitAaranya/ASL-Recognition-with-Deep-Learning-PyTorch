import os
import torch
import numpy as np
from PIL import Image
import torchvision.transforms as transforms


def load_datasets(folder = "datasets",train_or_test_folder = "Train_Alphabet",size = 50):
    x, labels = [],[]
    train_dataset_folder = os.path.join(folder,train_or_test_folder)
    print("Loading datasets: ",end = " ")
    for each_label in sorted(os.listdir(train_dataset_folder)):
        lable_folder = os.path.join(train_dataset_folder,each_label)
        for file_name in os.listdir(lable_folder):
            file_path = os.path.join(lable_folder,file_name)
            image_tensor = image_to_tensor(load_image(filename=file_path,size = size)) 
            x.append(image_tensor)
            labels.append(each_label)
        print(each_label,end = " ")
    print("\n")
    return torch.stack(x),labels

def load_image(filename,size):
    "Load image with defined size"
    img = Image.open(filename).resize((size,size))
    return img

def image_to_tensor(img):
    """Convert PIL image to Tensor"""
    return transforms.ToTensor()(img)


def alphabet_to_num(alphabet):
    conversion_dict = {char: ord(char)-ord('a') for char in "abcdefghijklmnopqrstuvwxyz"}
    return conversion_dict.get(alphabet.lower(),26)