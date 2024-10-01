image_paths = sorted(glob.glob('path_to_data/images/*'))
mask_paths = sorted(glob.glob('path_to_data/masks/*'))

images = []
masks = []

for img_path, mask_path in zip(image_paths, mask_paths):
    if os.path.exists(mask_path):  # Check for corresponding mask
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
        if img is not None and mask is not None:
            images.append(img)
            masks.append(mask)

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(images, masks, test_size=0.2, random_state=42)
