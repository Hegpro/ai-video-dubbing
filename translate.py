from deep_translator import GoogleTranslator

def translate_text(text):
    translated = GoogleTranslator(source='en', target='kn').translate(text)
    
    return translated