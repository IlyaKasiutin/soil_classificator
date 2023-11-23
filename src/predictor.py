import PIL
from PIL import Image
import IPython
import os
import torch
import torchvision
from torch import nn
import torchvision.transforms as transforms
from torchvision.models import mobilenet_v3_small


model = mobilenet_v3_small(weights=None)
model.classifier[3] = nn.Linear(in_features=1024, out_features=64, bias=True)
model.classifier.append(nn.Linear(in_features=64, out_features=4, bias=True))
device = torch.device('cpu')
model.load_state_dict(torch.load('model_params', map_location=device))
model.eval()


img_size = (256, 256)
test_transformation = transforms.Compose([
        transforms.Resize(size=img_size),
        transforms.ToTensor()
    ])

idx_to_class = {0: 'Alluvial soil',
                1: 'Black Soil',
                2: 'Red soil',
                3: 'Clay soil'}


def predict(model, img):
    model.eval()
    with torch.no_grad():
        input_data = test_transformation(img)
        output = model(torch.unsqueeze(input_data, 0))
        class_idx = torch.argmax(output.flatten(), dim=0).item()
        ans = idx_to_class[class_idx]
        return ans


def get_text_size(text, image, font):
    im = Image.new('RGB', )


def insert_label(orig_image, label, font_scale=0.25):
    draw = PIL.ImageDraw.Draw(orig_image)
    box = (10, 10, font_scale * orig_image.size[0], 0.5 * font_scale * orig_image.size[1])
    draw.rectangle(box, outline='#000', fill=(156, 156, 156))
    fontsize = 1
    font = PIL.ImageFont.truetype("arial.ttf", fontsize)
    while font.getlength(label) < box[2] - box[0]:
        fontsize += 1
        font = PIL.ImageFont.truetype("arial.ttf", fontsize)
    fontsize -= 1
    font = PIL.ImageFont.truetype("arial.ttf", fontsize)
    draw.text((box[0], box[1]), label, font=font, fill=(255, 0, 0))
    return orig_image


directory = 'images'
new_directory = 'labeled_images'

for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    image = Image.open(file_path)
    prediction = predict(model, image)
    image = insert_label(image, prediction)
    if not os.path.isdir(new_directory):
        os.mkdir(new_directory)
    image.save(os.path.join(new_directory, filename))
