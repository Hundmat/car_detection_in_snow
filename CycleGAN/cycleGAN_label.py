import os
import shutil
import cv2

# === CONFIG ===
SOURCE_FOLDER = "/Volumes/LaCie/nvd_dataset_small/images/train"
CLEAR_FOLDER = "trainA"
SNOWY_FOLDER = "trainB"

# Create target folders if they don’t exist
os.makedirs(CLEAR_FOLDER, exist_ok=True)
os.makedirs(SNOWY_FOLDER, exist_ok=True)

# Get all image paths
images = [f for f in os.listdir(SOURCE_FOLDER) if f.lower().endswith(('.jpg', '.png', '.jpeg'))]
print(f"Found {len(images)} images to label.\nPress 'c' for clear, 's' for snowy, or 'q' to quit.")

for img_name in images:
    img_path = os.path.join(SOURCE_FOLDER, img_name)
    img = cv2.imread(img_path)

    if img is None:
        print(f"Could not load: {img_path}")
        continue

    cv2.imshow("Label This Image", img)
    key = cv2.waitKey(0)

    if key == ord('c'):
        shutil.move(img_path, os.path.join(CLEAR_FOLDER, img_name))
        print(f"[CLEAR] → {img_name}")
    elif key == ord('s'):
        shutil.move(img_path, os.path.join(SNOWY_FOLDER, img_name))
        print(f"[SNOWY] → {img_name}")
    elif key == ord('q'):
        print("Quitting.")
        break
    else:
        print("Invalid key. Skipping.")

cv2.destroyAllWindows()