<<<<<<< HEAD
from .model import *
from PIL import Image
from torchvision import transforms

transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor(),
])


=======
>>>>>>> 3b382c45da8323694f1fe1498ba7637366756a68
def analyze_scan(file_path: str, modality: str) -> dict:
    """
    file_path: путь к загруженному файлу(CT/MRI)
    modality:'ct' или 'mri'
    Сейчас – заглушка. Даник здесь походу на свою модель заменишь
    """

<<<<<<< HEAD
    img = Image.open(file_path).convert("RGB")
    img_tensor = transform(img)  # [3, 128, 128]
    img_tensor = img_tensor.unsqueeze(0)  # [1, 3, 128, 128]
    with torch.no_grad():
        output = model(img_tensor.to(device))  # [1, 5]
        pred = output.argmax(1).item()

    print(output)
    print(pred)
    print(F.softmax(output))
    if int(pred)==4:
        # TODO: Замени на реальный анализ с моделью
        fake_result = {
            "cancer_probability":  float(1-float(F.softmax(output)[0][int(pred)])),  # от 0 до 1
            "stage": "No cancer",
            "tumor_type": "",
            "recommendation": (
                "Undergo further and more in-depth examinations with a doctor for a final diagnosis. "
                "For any health concerns, consult a qualified physician."
            )
        }
    else:
        fake_result = {
            "cancer_probability": float(1-float(F.softmax(output)[0][4])),  # от 0 до 1
            "stage": int(pred) + 1,
            "tumor_type": "",
            "recommendation": (
                "Undergo further and more in-depth examinations with a doctor for a final diagnosis. "
                "For any health concerns, consult a qualified physician."
            )
        }
=======
    # TODO: Замени на реальный анализ с моделью
    fake_result = {
        "cancer_probability": 0.27,   # от 0 до 1
        "stage": "N/A (research only)",
        "tumor_type": "N/A (placeholder)",
        "recommendation": (
            "Undergo further and more in-depth examinations with a doctor for a final diagnosis. "
            "For any health concerns, consult a qualified physician."
        )
    }
>>>>>>> 3b382c45da8323694f1fe1498ba7637366756a68
    return fake_result
