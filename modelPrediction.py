import torch
from torch import nn
from torchvision import transforms
import torchvision
from pathlib import Path
from PIL import Image
class digitRecognitionModel(nn.Module):
  def __init__(self,
               input_size:int,
               hidden_units:int,
               output_size:int):
    super().__init__()
    self.convolutionalLayer1=nn.Sequential(
        nn.Conv2d(in_channels=input_size,
                  out_channels=hidden_units,
                  kernel_size=3,
                  padding=1,
                  stride=1),
        nn.ReLU(),
        nn.Conv2d(in_channels=hidden_units,
                  out_channels=hidden_units,
                  kernel_size=3,
                  padding=1,
                  stride=1),
        nn.ReLU(),
        nn.MaxPool2d(kernel_size=2))
    self.convolutionalLayer2=nn.Sequential(
        nn.Conv2d(in_channels=hidden_units,
                  out_channels=hidden_units,
                  kernel_size=3,
                  padding=1,
                  stride=1),
        nn.ReLU(),
        nn.Conv2d(in_channels=hidden_units,
                  out_channels=hidden_units,
                  kernel_size=3,
                  padding=1,
                  stride=1),
        nn.ReLU(),
        nn.MaxPool2d(kernel_size=2)
    )
    self.classifier=nn.Sequential(
        nn.Flatten(),
        nn.Linear(in_features=hidden_units*7*7,
                  out_features=output_size)
    )
  def forward(self,x:torch.Tensor):
    x=self.convolutionalLayer1(x)
    x=self.convolutionalLayer2(x)
    classification=self.classifier(x)
    return classification
model = digitRecognitionModel(1,10,10)
modelPath=Path("C:/Users/Vanshika/PycharmProjects/digit recognition/model.pth")
model.load_state_dict(torch.load(modelPath))

def get_number(image):
    transform=transforms.Compose([transforms.ToTensor(),transforms.Normalize((0.5,),(0.5,))])
    image_tensor = transform(image)
    model.eval()
    with torch.inference_mode():
        prediction=model(image_tensor.unsqueeze(0))
        return torch.argmax(prediction, dim=1).item()
