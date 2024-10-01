model_nu = nested_unet()
model_au = attention_unet()

model_nu.compile(optimizer='adam', loss='binary_crossentropy', metrics=[tf.keras.metrics.AUC()])
model_au.compile(optimizer='adam', loss='binary_crossentropy', metrics=[tf.keras.metrics.AUC()])

history_nu = model_nu.fit(datagen.flow(X_train_clahe.reshape(-1, 256, 256, 1), y_train, batch_size=16), epochs=50, validation_data=(X_test_clahe.reshape(-1, 256, 256, 1), y_test))
history_au = model_au.fit(datagen.flow(X_train_clahe.reshape(-1, 256, 256, 1), y_train, batch_size=16), epochs=50, validation_data=(X_test_clahe.reshape(-1, 256, 256, 1), y_test))
