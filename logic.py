def recognize(photo):
  image = Image.open(photo).convert("RGB")
  image = ImageOps.fit(image, (224, 224), Image.Resampling.LANCZOS)
  image_array = np.asarray(image, dtype=np.float32)
  normalized_image = (image_array / 127.5) - 1
  data = np.expand_dims(normalized_image, axis=0)

  # Предсказание
  prediction = model.predict(data, verbose=0)
  index = np.argmax(prediction)
  class_name = class_names[index]
  confidence_score = float(prediction[0][index])

  # Вывод результатов
  result_class = class_name[2:].strip() if len(class_name) > 2 else class_name.strip()


  return result_class
