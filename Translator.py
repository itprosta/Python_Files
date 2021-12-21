from googletrans import Translator
import googletrans 

print(googletrans.LANGUAGES)

translator = Translator()

#print(translator.translate('안녕하세요.'))

text = translator.translate("Привет, как у вас дела?", dest='de')
print(text)
print(text.text)

langs = translator.detect(['한국어', '日本語', 'English', 'le français'])
for lang in langs:
	print(lang.lang, lang.confidence)

print(translator.detect('hi'))

translations = translator.translate(['Hello World', 'Subscribe to the Prosta channel', 'python is a good programming language'], dest='ru')
for translation in translations:
	print(translation.origin, ' -> ', translation.text)
