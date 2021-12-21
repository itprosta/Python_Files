from PIL import Image, ImageOps, ImageDraw

im = Image.open('image0.jpg') # Путь к фото
size = (500, 500)  # Размер итогового фото


mask = Image.new('L', size, 0) #L режим, размер, цвет (черный)
draw = ImageDraw.Draw(mask) # Переменная для рисования круга
draw.ellipse((0, 0) + size, fill=255) # Ресуем круг

im = im.resize(size) # Изменяем размеры фото

output = ImageOps.fit(im, mask.size, centering=(0.5, 0.5)) #0.0, 0.0
output.putalpha(mask) # Создаем альфа-слой


#output.thumbnail(size, Image.ANTIALIAS)
#создает красивые эскизы изображений JPEG
#с сохранением соотношений сторон с максимальным разрешением 128x128


output.save('image_output.png')# сохранение фото

