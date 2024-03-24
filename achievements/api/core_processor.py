from googletrans import Translator


translator = Translator()


def string_translate(string, dest):
    try:
        translation = translator.translate(string, dest)
    except AttributeError as e:
        return 'Translation failed: ' + str(e)
    return translation.text
