X_train_clahe = np.array(X_train_clahe) / 255.0
X_test_clahe = np.array(X_test_clahe) / 255.0

# Data Augmentation
datagen = ImageDataGenerator(rotation_range=10, width_shift_range=0.1,
                             height_shift_range=0.1, shear_range=0.1,
                             zoom_range=0.1, horizontal_flip=True)

# Fit the generator
datagen.fit(X_train_clahe.reshape(-1, 256, 256, 1))  # Reshape based on your image size
