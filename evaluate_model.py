def dice_coefficient(y_true, y_pred):
    smooth = 1e-7
    intersection = tf.reduce_sum(y_true * y_pred)
    return (2 * intersection + smooth) / (tf.reduce_sum(y_true) + tf.reduce_sum(y_pred) + smooth)

# Evaluate models
dice_nu = dice_coefficient(y_test, model_nu.predict(X_test_clahe))
dice_au = dice_coefficient(y_test, model_au.predict(X_test_clahe))
