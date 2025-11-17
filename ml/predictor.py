def analyze_scan(file_path: str, modality: str) -> dict:
    """
    file_path: путь к загруженному файлу (CT / MRI)
    modality: 'ct' или 'mri'

    Возвращает словарь с "результатами анализа".
    Сейчас – заглушка. ML-человек заменит на свою модель.
    """

    # TODO: заменить на реальный анализ с моделью
    fake_result = {
        "cancer_probability": 0.27,   # от 0 до 1
        "stage": "N/A (research only)",
        "tumor_type": "N/A (placeholder)",
        "recommendation": (
            "Undergo further and more in-depth examinations with a doctor for a final diagnosis. "
            "For any health concerns, consult a qualified physician."
        )
    }
    return fake_result
