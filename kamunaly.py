#!python3
def connect(host='http://google.com'):
    try:
        import urllib.request
        urllib.request.urlopen(host)
        return True
    except:
        return False


from termcolor import cprint, colored

if connect():
    pass
elif not connect():
    cprint('No internet', 'red')
    exit()
from collections import OrderedDict
from types import MappingProxyType
from playsound import playsound
from pydub import AudioSegment
import concurrent.futures
import translators as ts
from tqdm import trange
from fpdf import FPDF
from sys import exit
import langdetect
import pdfplumber
import pyfiglet
import requests
import logging
import urllib3
import shutil
import random
import PyPDF2
import gtts
import time
import re
import os

# import pdb; pdb.set_trace()

logging.basicConfig(filename='./simuka.log', format="%(levelname)s %(asctime)s %(message)s",
                    datefmt='%d-%b-%y %H:%M:%S')
logger = logging.getLogger('kamunaly.py')
cprint('WELCOME TO'.rjust(25), 'blue', attrs=['bold'])
cprint(pyfiglet.figlet_format('KAMUNALY', font='shadow'), 'blue', attrs=['bold'])
cprint('Version: 1.0'.rjust(28), 'red')
cprint('Developed by TithoLinux'.rjust(33), 'red', attrs=['bold'])
cprint('IG https://www.instagram.com/titho.linux/'.rjust(30), 'magenta')
cprint("\nPDF TO AUDIO CONVERTER\n", 'blue')
cprint('Usage', color='green', attrs=['bold'])
cprint('Put PDF file into library folder and run KAMUNARY', 'green')
cprint("Only PDFs files allowed", 'red', attrs=['bold'])
print('\n')
time.sleep(0.25)

r = os.path.abspath('.')
library = './library/'
audio = './audio/'
concurrent_ = f'{r}/.concurrent'


def file():
    file_list = OrderedDict()
    os.makedirs(library) if not os.path.exists(library) else None
    os.makedirs(audio) if not os.path.exists(audio) else None
    os.makedirs(f'{concurrent_}/mp3') if not os.path.exists(f'{concurrent_}/mp3') else None
    os.makedirs(f'{concurrent_}/wav') if not os.path.exists(f'{concurrent_}/wav') else None
    os.makedirs(f'{concurrent_}/mp3_throw_away') if not os.path.exists(f'{concurrent_}/mp3_throw_away') else None
    if len(os.listdir(library)) != 0:
        cprint('List of Your files in library', 'green', attrs=['reverse', 'bold'])
        for index, filee in enumerate(sorted(os.listdir(library))):
            if os.path.isfile(f'{library}/{filee}'):
                file_list[index + 1] = filee
                print(colored(index + 1, 'yellow', attrs=['bold']), colored(filee, 'yellow'))
    else:
        cprint('INFO: No File available in your library', 'red')
        cprint('[:] Please import one and try again', 'blue')
        exit()
    while True:
        try:
            file_to_read = int(input('[:] Select a number of file # '))
            print('\n')
            if file_to_read == 'q':
                exit()
            return f'{library}/{file_list[file_to_read]}'
        except:
            print('INVALID input! ')
            continue


while True:
    books = file()
    file_name = os.path.basename(books)
    name_in_folder = file_name.split('.')
    name_of_file = os.path.join(f"{audio}{name_in_folder[0]}.mp3")
    langdetect.DetectorFactory.seed = 0
    if os.path.isfile(books) and re.findall(r'\w+.pdf$', books):
        break
    elif re.search(r'\w+.pdf$|.ppt?$|.xls$|.doc?$|.htm$|.txt$|.pptx$', books) is None:
        if len(books) <= 5000:
            cprint("Don't download in high speed", 'red')
            with open('./copied-text.txt', 'w')as txt:
                txt.write(books)
            with open("./copied-text.txt", "r") as f:
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=12)
                for x in f:
                    pdf.cell(200, 10, txt=x, ln=1)
                book_in_pdf = pdf.output("./copied-text.pdf")
            books = './copied-text.pdf'
            name_of_file = f"./audio/copied-text.mp3"
            break
        else:
            print("text is too long")
            continue
    else:
        cprint("ERROR! Invalid File\n", 'red', attrs=['bold'])
        continue

# hosts
g, b, ba, a, t, yo, s, d = ['google', 'bing', 'baidu', 'alibaba', 'tencent', 'youdao', 'sogou', 'deepl']
G, B, BA, A, T, YO, S, D = [ts.google, ts.bing, ts.baidu, ts.alibaba, ts.tencent, ts.youdao, ts.sogou, ts.deepl]
server = {'google': G, 'bing': B, 'baidu': BA, 'alibaba': A, 'tencent': T, 'youdao': YO, 'sogou': S, 'deepl': D}

# languages with the host they supported
hosts = MappingProxyType(
    {'english': [g, b, ba, a, t, yo, s, d], 'chinese': [g, b, ba, a, t, yo, s, d],
     'arabic': [g, b, ba, a, t, yo, s, d],
     'russian': [g, b, ba, a, t, yo, s, d], 'french': [g, b, ba, a, t, yo, s, d], 'german': [g, b, ba, t, s, d],
     'spanish': [g, b, ba, a, t, yo, s, d], 'portuguese': [g, b, ba, a, t, yo, s, d], 'italian': [g, b, ba, a,
                                                                                                  t, yo, s, d],
     'japanese': [g, b, ba, t, yo, s, d], 'korean': [g, b, ba, t, yo, s, d], 'greek': [g, b, ba, s],
     'dutch': [g, b, ba, yo, s, d], 'hindi': [g, b, t, s], 'turkish': [g, b, a, t, s, ], 'malay': [g, b, ba],
     'thai': [g, b, ba, a, t, s], 'vietnamese': [g, b, ba, a, t, yo, s], 'indonesian': [g, b, a, t, yo, s, ],
     'hebrew': [g, b, s], 'polish': [g, b, ba, s, d], 'mongolian': [g], 'czech': [g, b, ba, s],
     'hungarian': [g, b, ba, s], 'estonian': [g, b, ba, s], 'bulgarian': [g, b, ba, s], 'danish': [g, b, ba, s],
     'finnish': [g, b, ba, s], 'romanian': [g, b, ba, s], 'swedish': [g, b, ba, s], 'slovenian': [g, b, ba],
     'persian/farsi': [g, b, s], 'bosnian': [g, b, s], 'serbian': [g, b, s], 'fijian': [b, s],
     'filipino': [g, b, s], 'haitiancreole': [g, b, s], 'catalan': [g, b, s], 'croatian': [g, b, s],
     'latvian': [g, b, s], 'lithuanian': [g, b], 'urdu': [g, b, s], 'ukrainian': [g, b, s], 'welsh': [g, b, s],
     'tahiti': [b, s, d], 'tongan': [b, s, d], 'swahili': [g, b, s], 'samoan': [g, b, s], 'slovak': [g, b, s],
     'afrikaans': [g, b, s], 'norwegian': [g, b, s], 'bengali': [g, b, s], 'malagasy': [g, b, s],
     'maltese': [g, b, s],
     'queretaro otomi': [b, s], 'klingon/tlhingan hol': [b, s], 'gujarati': [g, b], 'tamil': [g, b],
     'telugu': [g, b],
     'punjabi': [g, b], 'amharic': [g], 'azerbaijani': [g], 'bashkir': [g, b], 'belarusian': [g],
     'cebuano': [g], 'chuvash': [b, g], 'esperanto': [g, b], 'basque': [g], 'irish': [g, b], 'emoji': [b, g]})

# All supported languages
languages = MappingProxyType(
    {'english': 'en', 'chinese': 'zh', 'arabic': 'ar', 'russian': 'ru', 'french': 'fr', 'german': 'de',
     'spanish': 'es', 'portuguese': 'pt', 'italian': 'it', 'japanese': 'ja', 'korean': 'ko', 'greek': 'el',
     'dutch': 'nl', 'hindi': 'hi', 'turkish': 'tr', 'malay': 'ms', 'thai': 'th', 'vietnamese': 'vi',
     'indonesian': 'id', 'hebrew': 'he', 'polish': 'pl', 'mongolian': 'mn', 'czech': 'cs', 'hungarian': 'hu',
     'estonian': 'et', 'bulgarian': 'bg', 'danish': 'da', 'finnish': 'fi', 'romanian': 'ro', 'swedish': 'sv',
     'slovenian': 'sl', 'persian/farsi': 'fa', 'bosnian': 'bs', 'serbian': 'sr', 'fijian': 'fj',
     'filipino': 'tl', 'haitiancreole': 'ht', 'catalan': 'ca', 'croatian': 'hr', 'latvian': 'lv',
     'lithuanian': 'lt', 'urdu': 'ur', 'ukrainian': 'uk', 'welsh': 'cy', 'tahiti': 'ty', 'tongan': 'to',
     'swahili': 'sw', 'samoan': 'sm', 'slovak': 'sk', 'afrikaans': 'af', 'norwegian': 'no', 'bengali': 'bn',
     'malagasy': 'mg', 'maltese': 'mt', 'queretaro otomi': 'otq', 'klingon/tlhingan hol': 'tlh',
     'gujarati': 'gu', 'tamil': 'ta', 'telugu': 'te', 'punjabi': 'pa', 'amharic': 'am', 'azerbaijani': 'az',
     'bashkir': 'ba', 'belarusian': 'be', 'cebuano': 'ceb', 'chuvash': 'cv', 'esperanto': 'eo', 'basque': 'eu',
     'irish': 'ga', 'emoji': 'emj'})

# top level domain
any_ = ['com.au', 'co.uk', 'com', 'ca', 'co.in', 'ie', 'co.za', 'ca', 'fr', 'com.br', 'pt', 'com.mx', 'es', 'com']
random.shuffle(any_)
domain = {  # Mandarin is viceVersa
    "en": {'English (Australia)': 'com.au', 'English (United Kingdom)': 'co.uk', 'English (United States)': 'com',
           'English (Canada)': 'ca', 'English (India)': 'co.in', 'English (Ireland)': 'ie',
           'English (South Africa)': 'co.za'},
    "fr": {'French (Canada)': 'ca', 'French (France)': 'fr'},
    "pt": {'Portuguese (Brazil)': 'com.br', 'Portuguese (Portugal)': 'pt'},
    "es": {'Spanish (Mexico)': 'com.mx', 'Spanish (Spain)': 'es', 'Spanish (United States)': 'com'},
    "sw": {'swahili': 'com', 'swahili2': 'com', 'swahili3': 'com'},
    'Mandarin (China Mainland)': ['zh-CN', any_[0]], 'Mandarin (Taiwan)': ['zh-TW', any_[0]]}


def choose_hosts():
    global lang_trans, serv
    host_in_use = OrderedDict()
    while True:
        try:
            lang_trans = input("[:] Translate into which language? ").lower()
            cprint(f'[:] {lang_trans.title()} supported by the following Hosts', 'green', attrs=['bold'])
            for num, host in enumerate(hosts[lang_trans], start=1):
                print(colored(num, 'yellow', attrs=['bold']), colored(host, 'yellow'))
                host_in_use[num] = host
            cprint("[:] if you get incorrect results select another host recommended ('google, alibaba)", 'magenta')
        except:
            cprint(f"{lang_trans.title()} not available! check languages list and try again..", 'red', attrs=['bold'])
            continue
        else:
            break

    while True:
        host_to_use = input("\n[:]Choose a number of host to use or press [ENTER] to use the default host ")
        print('\n')
        if host_to_use != '' and len(host_to_use) > 0:
            if int(host_to_use) in range(len(host_in_use) + 1):
                serv = host_in_use[int(host_to_use)]
                serv = server[serv]
                break
            else:
                cprint("ERROR! invalid Host", 'red')
                continue
        elif not host_to_use:
            serv = G
            break
        else:
            continue
    return serv, lang_trans


def language_detect(text2):
    try:
        lang_sample = random.sample(list(text2.values()), 1)
        lang_og = langdetect.detect(lang_sample[0])
    except:
        while True:
            print("% failed to detect the language please enter your language code  or "
                  "type 'list' to see the available languages codes ")
            lang_og = input(': ')
            if lang_og in languages.values():
                lang_og = lang_og
                break
            elif lang_og == 'list':
                for i in range(len(languages)):
                    print(sorted(list(languages.values()))[i], ' ', sorted(list(languages.keys()))[i])
                continue
            else:
                continue
    return lang_og


def delete_none(text2):
    for list_of_text in text2.values():
        if list_of_text == '':
            del text2[list(text2.keys())[list(text2.values()).index(list_of_text)]]
    return text2


def list_languages():
    while True:
        in_lang = input(colored('[:] List available Languages [yes/no]? ', 'green', attrs=['bold']))
        if in_lang.lower() not in ('yes', 'no'):
            continue
        if in_lang == 'yes':
            for index, lang in enumerate(sorted(languages), start=1):
                print(colored(index, 'yellow', attrs=['bold']), colored(lang, 'yellow'))
            break
        else:
            break
    return None


class Extract:
    def __init__(self, book):
        self.book = book

    def pdf_files(self):
        while True:
            translate = input('[:] Translate a file [yes/no]? ').lower()
            if translate not in ['yes', 'no']:
                continue
            else:
                break
        with open(self.book, 'rb') as pdf:
            pdf_reader = PyPDF2.PdfFileReader(pdf)
            cprint(f'\n **** File have {pdf_reader.numPages} pages ****', 'magenta')
            while True:
                start = input('[:] Type "ALL" to read all pages or type "NO" to read specific pages: ').lower()
                if start not in ['all', 'no']:
                    continue
                elif start == 'all':
                    data_usage = round(1.5 * pdf_reader.numPages)
                    if translate == 'yes':
                        list_languages()
                        _serv, _lang_trans = choose_hosts()
                        with pdfplumber.open(self.book) as pdf1:
                            text2 = OrderedDict()
                            for number, page in enumerate(trange(pdf_reader.numPages)):
                                text1 = pdf1.pages[page].extract_text()
                                if type(text1) != str:
                                    continue
                                text1 = _serv(text1, 'auto', languages[_lang_trans])
                                text2[number] = text1
                            text2 = delete_none(text2)
                            text = ' '.join(list(text2.values()))
                            return text, text2, _lang_trans, data_usage
                    elif translate == "no":
                        with pdfplumber.open(self.book) as pdf1:
                            text2 = OrderedDict()
                            for number, page in enumerate(trange(pdf_reader.numPages)):
                                text1 = pdf1.pages[page].extract_text()
                                if type(text1) != str:
                                    continue
                                text2[number] = text1
                            text2 = delete_none(text2)
                            text = ' '.join(list(text2.values()))
                            lang_og = language_detect(text2)
                            lang_og = list(languages)[list(languages.values()).index(lang_og)]
                            return text, text2, lang_og, data_usage
                elif start == 'no':
                    if translate == "yes":
                        list_languages()
                        _serv, _lang_trans = choose_hosts()
                        while True:
                            try:
                                start_page = int(input("[:] Translate from page number? "))
                                end_page = int(input("[:] to page number? "))
                            except ValueError:
                                cprint('ERROR! invalid numbers', 'red')
                                continue
                            else:
                                break
                        with pdfplumber.open(self.book) as pdf1:
                            text2 = OrderedDict()
                            for number, page in enumerate(trange(start_page - 1, end_page)):
                                text1 = pdf1.pages[page].extract_text()
                                if type(text1) != str:
                                    continue
                                text1 = _serv(text1, 'auto', languages[_lang_trans])
                                text2[number] = text1
                            data_usage = round(1.5 * len(text2))
                            text2 = delete_none(text2)
                            try:
                                text = ' '.join(list(text2.values()))
                            except (requests.exceptions.HTTPError, KeyError, requests.exceptions.ConnectionError,
                                    urllib3.exceptions.ProtocolError, ConnectionResetError):
                                cprint('INFO: Host is too slow please choose another one', 'red')
                                exit()
                            return text, text2, _lang_trans, data_usage
                    elif translate == "no":
                        start_page = int(input("[:] Convert from page number? "))
                        end_page = int(input("[:] to page number? "))
                        with pdfplumber.open(self.book) as pdf1:
                            text2 = OrderedDict()
                            for number, page in enumerate(trange(start_page - 1, end_page)):
                                text1 = pdf1.pages[page].extract_text()
                                if type(text1) != str:
                                    continue
                                text2[number] = text1
                            data_usage = round(1.5 * len(text2))
                            text2 = delete_none(text2)
                            text = ' '.join(list(text2.values()))
                            lang_og = language_detect(text2)
                            lang_og = list(languages)[list(languages.values()).index(lang_og)]
                            return text, text2, lang_og, data_usage


def top_level_domain(in_language, out_language):
    not_code = ['Mandarin (China Mainland)', 'Mandarin (Taiwan)']

    def lang_in_code():
        if out_language in domain.keys():
            cprint(f'\n[:] The followings are {in_language.capitalize()}-language accents select one', 'green',
                   attrs=['bold'])
            for num, accents in enumerate(domain[out_language].keys(), start=1):  # print languages
                print(colored(num, 'yellow', attrs=['bold']), colored(accents, 'yellow'))
            tld = int(input('\n[:] Language Number? '))
            dic = OrderedDict()
            for num, accents in enumerate(domain[out_language].keys(), start=1):
                dic[num] = accents
            tld = domain[out_language][dic[tld]]
            return tld
        else:
            return 'com'

    def lang_not_code():
        cprint(f'\n[:] The followings are {in_language.capitalize()}-language accents select one', 'green',
               attrs=['bold'])
        dic = OrderedDict()
        for num, accents in enumerate(not_code, start=1):
            print(num, accents)
            dic[num] = accents
        tld = int(input('\n[:] Language Number? '))
        tld = domain[dic[tld]][1][0]
        return tld

    if in_language == "chinese":
        return lang_not_code
    elif in_language not in not_code:
        return lang_in_code


def mp3(text, number):
    tts1 = gtts.gTTS(text=text, lang=use_lang, tld=tld1)
    tts1.save(f'{concurrent_}/mp3_throw_away/{number}.mp3')


def wav():
    mp3_path = f"{concurrent_}/mp3/"
    wav_path = f"{concurrent_}/wav/"
    music = []
    for _mp in os.listdir(mp3_path):
        os.remove(f'{mp3_path}{_mp}') if os.path.getsize(f'{mp3_path}{_mp}') == 0 else None
    for _mp3 in sorted(os.listdir(mp3_path)):
        try:
            AudioSegment.from_mp3(f'{mp3_path}{_mp3}').export(f"{wav_path}{_mp3.split('.')[0]}.wav", format="wav")
        except:
            logger.exception("exception occurs")
            _ = [os.remove(a) for a in os.listdir(mp3_path)] if os.listdir(mp3_path) == True else None
            _ = [os.remove(b) for b in os.listdir(wav_path)] if os.listdir(wav_path) == True else None
            playsound(f'{r}/.Try Again [Sound Effect].opus')
            exit()
        finally:
            os.remove(f"{mp3_path}{_mp3}")
            music.append(AudioSegment.from_wav(f"{wav_path}{_mp3.split('.')[0]}.wav"))
            os.remove(f"{wav_path}{_mp3.split('.')[0]}.wav")
    combined = AudioSegment.empty()
    for fname in music:
        combined += fname
    combined.export(f"{r}/audio/{name_in_folder[0]}.wav", format='wav')
    AudioSegment.from_wav(f"{r}/audio/{name_in_folder[0]}.wav") \
        .export(f"{r}/audio/{name_in_folder[0]}.mp3", format='mp3')
    os.remove(f"{r}/audio/{name_in_folder[0]}.wav")
    playsound(f'{r}/mixkit-melodical-flute-music-notification-2310.wav')
    cprint(f'[:] Download Finished. File saved to {name_of_file}', 'yellow', attrs=['bold', 'blink'])


if __name__ == '__main__':
    try:
        output_text, text_fast, output_lang, DataUsage = Extract(books).pdf_files()
        os.remove(f'{r}/copied-text.pdf') if os.path.exists(f'{r}/copied-text.pdf') else None
        os.remove(f'{r}/copied-text.txt') if os.path.exists(f'{r}/copied-text.txt') else None
        use_lang = list(gtts.lang.tts_langs().keys())[
            list(gtts.lang.tts_langs().values()).index(output_lang.capitalize())]
        tld1 = top_level_domain(output_lang, use_lang)()
        cprint(f'Data usage approximate {DataUsage}MB', 'magenta')
        cprint('DOWNLOADING please wait....', 'red', attrs=['reverse', 'blink', 'bold'])
        with concurrent.futures.ThreadPoolExecutor(max_workers=None) as executor:
            gear = 10  # gear changer
            if len(text_fast) < gear:
                gear = len(text_fast)
            while len(text_fast) != 0:
                for i in range(1):
                    executor.map(mp3, list(text_fast.values())[:gear], list(text_fast.keys())[:gear])
                for _ in range(gear):
                    try:
                        del text_fast[list(text_fast.keys())[0]]
                    except IndexError:
                        pass
                file_size = [0 * g for g in range(gear)]
                while True:
                    file_size_sum = sum(file_size)
                    time.sleep(60)
                    for num_file, files in enumerate(os.listdir(f'{concurrent_}/mp3_throw_away/')):
                        file_size[num_file] = os.path.getsize(f'{concurrent_}/mp3_throw_away/{files}')
                    file_size_sum1 = sum(file_size)
                    if file_size_sum == file_size_sum1:
                        for move_file in os.listdir(f'{concurrent_}/mp3_throw_away/'):
                            shutil.move(f'{concurrent_}/mp3_throw_away/{move_file}', f'{concurrent_}/mp3')
                        break
                    else:
                        continue
            wav()
    except KeyboardInterrupt:
        print('Thanks for using Kamunaly :)')
