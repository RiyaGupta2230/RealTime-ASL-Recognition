Below is the updated README file reflecting the revised project details:

---

# Real-Time Sign Language Recognition Using Deep Learning Techniques

This project implements a real-time sign language recognition system using Python, OpenCV, and a convolutional neural network (CNN). The goal is to build a neural network that can identify both alphabets (A–Z) and numeric digits (0–9) from American Sign Language (ASL) gestures, and translate them into text and voice in real time.

## Dataset

The primary data source is the compiled American Sign Language (ASL) dataset from [Kaggle](https://www.kaggle.com/ayuraj/american-sign-language-dataset) citeturn0search0. The original dataset contains 18,200 images of 200x200 pixels, organized into 26 classes corresponding to the letters A-Z. For this project, the dataset has been extended to include numeric digits (0–9), expanding the classification problem to 36 classes. This extension increases the system’s versatility, enabling recognition of both alphabets and numbers.

<p align="center">
  <img width="600" src="https://github.com/parakh-gupta/Sign_language_alphabet_recognizer/blob/master/alphabet.png">
</p>

## Requirements

- Python 3.x
- OpenCV
- NumPy
- Pandas
- TensorFlow
- Keras
- (Optional) Matplotlib and scikit-learn for visualization and additional evaluation

All the requirements can be installed via the `requirements.txt` file:

```
pip install -r requirements.txt
```