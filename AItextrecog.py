import cv2
import pytesseract
import os

# Tesseract installation path (Windows)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Image path
image_path = r"C:\Users\Sri Charan\Desktop\AI text recognization system\images\sample.png"
# Read image
image = cv2.imread(image_path)

# Check image
if image is None:
    print("Error: Image not found!")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Extract text
text = pytesseract.image_to_string(gray)

print("\n========== EXTRACTED TEXT ==========\n")
print(text)

# Create output folder if not exists
os.makedirs("output", exist_ok=True)

# Save extracted text
with open("output/extracted_text.txt", "w", encoding="utf-8") as file:
    file.write(text)

print("\nText saved successfully!")
print("Location: output/extracted_text.txt")