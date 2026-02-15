import torch.nn as nn
import torch
import os
import neuropan_ai.settings as settings
import torch.nn.functional as F
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class CancerCNN(nn.Module):
    def __init__(self, num_classes=5):
        super().__init__()

        self.conv = nn.Sequential(
            nn.Conv2d(3, 16, 3),
            nn.ReLU(),
            nn.MaxPool2d(2),

            nn.Conv2d(16, 32, 3),
            nn.ReLU(),
            nn.MaxPool2d(2),
        )

        self.fc = nn.Sequential(
            nn.Flatten(),
            nn.Linear(32 * 30 * 30, 128),
            nn.ReLU(),
            nn.Linear(128, num_classes)  # ← 5 классов
        )

    def forward(self, x):
        x = self.conv(x)
        return self.fc(x)


model = CancerCNN(num_classes=5)
model_path = os.path.join(settings.BASE_DIR, "ml\cancer_model2.pth")
model.load_state_dict(torch.load(model_path, map_location=device, weights_only=True))
model.to(device)
model.eval()

