from gtts import gTTS
from googletrans import Translator
import os

with open ("MUSOC.txt","r") as fp:
    content=fp.read()

lang_dict={'Afrikaans': 'af',
'Albanian'	:'sq',
'Amharic'	:'am',
'Arabic'	:'ar',
'Armenian'  :'hy',
'Basque'	:'eu',
'Belarusian'	:'be',
'Bosnian'	:'bs',
'Bulgarian'	:'bg',
'Catalan'	:'ca',
'Cebuano'	:'ceb (ISO-639-2)',
'Chichewa'	:'ny',
'Chinese (Simplified)'	:'zh-CN (BCP-47)',
'Chinese (Traditional)'	:'zh-TW (BCP-47)',
'Corsican'	:'co',
'Croatian'	:'hr',
'Czech'	:'cs',
'Danish'	:'da',
'Dutch'	:'nl',
'English'	:'en',
'French'	:'fr',
'Frisian'	:'fy',
'Galician'	:'gl',
'Georgian'	:'ka',
'German'	:'de',
'Greek'	:'el',
'Hawaiian':	'haw (ISO-639-2)',
'Hebrew':	'iw',
'Hindi':	'hi',
'Hmong':	'hmn (ISO-639-2)',
'Hungarian':	'hu',
'Icelandic':	'is',
'Igbo':	'ig',
'Indonesian':	'id',
'Irish':	'ga',
'Italian':	'it',
'Japanese':	'ja',
'Korean':	'ko',
'Kurdish':	'ku',
'Latin':	'la',
'Latvian':	'lv',
'Lithuanian':	'lt',
'Macedonian':	'mk',
'Maltese':	'mt',
'Mongolian':	'mn',
'Burmese':	'my',
'Polish':	'pl',
'Portuguese':	'pt',
'Romanian'	:'ro',
'Russian':'ru',
'Serbian':	'sr',
'Spanish':	'es',
'Swedish':	'sv',
'Thai':	'th',
'Turkish':	'tr',
'Ukrainian':	'uk',
'Urdu':	'ur',
'Uzbek':	'uz',
'Vietnamese':	'vi',
'Welsh':	'cy',
'Yiddish':	'yi',
'Yoruba':	'yo',
}

translator=Translator()
a=input("In which language would you like to translate the content?")
print (translator.translate(content, dest=lang_dict[str(a)]).text)
myobj=gTTS(text=translator.translate(content, dest=lang_dict[str(a)]).text,lang=lang_dict[str(a)],slow=False)
myobj.save("translated.mp3")
os.system("mpg321 welcome.mp3")
