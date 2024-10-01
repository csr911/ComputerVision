def apply_clahe(images):
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    return [clahe.apply(image) for image in images]

X_train_clahe = apply_clahe(X_train)
X_test_clahe = apply_clahe(X_test)
