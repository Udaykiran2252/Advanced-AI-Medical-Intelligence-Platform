def generate_report(prediction, confidence):

    if prediction == "NORMAL":
        return f"""
🩺 AI Medical Report

Prediction: {prediction}

Confidence: {confidence}%

Interpretation:
No significant signs of pneumonia were detected by the AI model.

Recommendation:
• Continue routine health monitoring.
• If symptoms such as fever, cough, or chest pain persist, consult a physician.
• This AI prediction is intended to assist and does not replace professional medical diagnosis.
"""

    return f"""
🩺 AI Medical Report

Prediction: {prediction}

Confidence: {confidence}%

Interpretation:
The uploaded chest X-ray contains features consistent with pneumonia.

Recommendation:
• Consult a physician as soon as possible.
• Additional clinical examination is recommended.
• This AI prediction should always be verified by a qualified radiologist.
"""