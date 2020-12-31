import Crawler.Crawler as crawler
import Topic_Modeling.topic_modeler as topic_modeler
import tts.tts as tts
import sys
import os

def generate_images(file_address):
    if os.system("rm images/*") != 0:
        pass

    if os.system("./translation/translate.sh") != 0:
        raise Exception("Error to translate")

    #download wordnet if it not exists
    topic_modeler.setup()

    topic_list = topic_modeler.topic_lists(file_address)

    for topic in topic_list:
        crawler.getImages(theme, topic[0], 1)

def generate_audio(file_address, theme, language):
    if os.system(f"./translation/translate.sh {language}") != 0:
        raise Exception("quebrou")

    if os.system("rm audios/*") != 0:
        pass

    tts.generate_audio(f"{theme}.wav", file_address)


if __name__ == "__main__":
    #Default params
    file_address = 'translation/text-out.txt'
    language = "en"

    #python3 main.py giant-snail -l es -f translation/text-out2.txt

    params = sys.argv[1:]
    #params = giant-snail, -l, es, -f, translation/text-out2.txt

    theme = params.pop(0)
    #params = -l, es, -f, translation/text-out2.txt

    for flag in params:
        if flag == "--file-address" or flag == "-f":
            file_address = params[1]
            params = params[2:]
        elif flag == "--language" or flag == "-l":
            language = params[1]
            params = params[2:]

    generate_images(file_address)
    generate_audio(file_address, theme, language)



