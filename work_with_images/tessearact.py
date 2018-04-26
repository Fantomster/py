from PIL import Image
import subprocess

def cleanFile(filePath, newFilePath):
    image = Image.open(filePath)
    # Задаём пороговое значение для данного изображения и сохраняем
    image = image.point(lambda x: 0 if x<143 else 255)
    image.save(newFilePath)

    #Вызываем tesseract, чтобы выполнить OCR вновь созданного изображения
    subprocess.call(['tesseract', newFilePath, 'output'])

    #Открываем и читаем полученный в результате файл данных
    outputFile = open('output.txt', 'r')
    print(outputFile.read())
    outputFile.close()

cleanFile('123.jpg', 'text_2_clean.jpg')