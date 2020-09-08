import requests
from bs4 import BeautifulSoup
import sys



def is_supported(lang):
    supported_languages = ['Arabic', 'German', 'English',
                           'Spanish', 'French', 'Hebrew',
                           'Japanese', 'Dutch', 'Polish',
                           'Portuguese', 'Romanian', 'Russian',
                           'Turkish', 'All']
    if lang.capitalize() in supported_languages:
        return lang
    else:
        return False

def reverso_search(from_language, to_language, word):
    base_url = 'https://context.reverso.net/translation/'
    direction = from_language.lower() + '-' + to_language.lower() + '/'
    url = base_url + direction + word
    user_agent = 'Mozilla/5.0'
    response = requests.get(url, headers={'User-Agent': user_agent})
    # if response.ok:
    #     print(f'{response.status_code} OK\n')
    # else:
    #     print('Something wrong with your internet connection')

    soup = BeautifulSoup(response.content, 'html.parser')
    translations = soup.find_all('a', class_="translation")
    translation_word_list = []
    for p in translations:
        translation_word_list.append(p.text.strip())
        # print(p.text.strip())

    # print('Context examples:\n')
    print(f'{to_language} Translations:')
    if len(translation_word_list) < 5:
        for i in range(len(translation_word_list)):
            print(translation_word_list[i])
    else:
        for i in range(1, 6):
            print(translation_word_list[i])

    example_translations = soup.select(".example .text")
    translation_example_list = []
    for p in example_translations:
        translation_example_list.append(p.text.strip())
        # print(p.text.strip())

    print(f'\n{to_language} Examples:')
    if len(translation_example_list) < 10:
        for i in range(0, len(translation_example_list), 2):
            print(translation_example_list[i])
            print(translation_example_list[i + 1])
            print('')
    else:
        for i in range(0, 10, 2):
            print(translation_example_list[i])
            print(translation_example_list[i + 1])
            print('')
    pass


def reverso_file(from_language, to_language, word, out_file):
    base_url = 'https://context.reverso.net/translation/'
    direction = from_language.lower() + '-' + to_language.lower() + '/'
    url = base_url + direction + word
    user_agent = 'Mozilla/5.0'
    try:
        response = requests.get(url, headers={'User-Agent': user_agent})
    except requests.exceptions.ConnectionError:
        print('Something wrong with your internet connection')
        exit()

    # if response.ok:
    #     print(f'{response.status_code} OK\n')
    # else:
    #     print('Something wrong with your internet connection')

    soup = BeautifulSoup(response.content, 'html.parser')
    translations = soup.find_all('a', class_="translation")
    translation_word_list = []
    for p in translations:
        translation_word_list.append(p.text.strip())
        # print(p.text.strip())
    # print('Context examples:\n')
    print(f'{to_language} Translations:', file=out_file, flush=True)
    if len(translation_word_list) > 1:
        print(translation_word_list[1], file=out_file, flush=True)
    elif translation_word_list:
        print(translation_word_list[0], file=out_file, flush=True)
    else:
        print('No translations found')

    example_translations = soup.select(".example .text")
    translation_example_list = []
    for p in example_translations:
        translation_example_list.append(p.text.strip())
        # print(p.text.strip())

    print(f'\n{to_language} Examples:', file=out_file, flush=True)
    if len(translation_example_list) > 1:
        print(translation_example_list[0], file=out_file, flush=True)
        print(translation_example_list[1], file=out_file, flush=True)
    print('', file=out_file, flush=True)
    print('', file=out_file, flush=True)
    pass


def is_jabberwocky(word):
    jabberwocky_words = ['brrrrrrrrrrr']
    if word in jabberwocky_words:
        return True
    else:
        return False


def main_menu(*args):
    menu_items = ['Arabic', 'German', 'English',
                  'Spanish', 'French', 'Hebrew',
                  'Japanese', 'Dutch', 'Polish',
                  'Portuguese', 'Romanian', 'Russian',
                  'Turkish']
    if len(args) == 3:
        if is_supported(args[0]):
            from_language = is_supported(args[0])
        else:
            print(f"Sorry, the program doesn't support {args[0]}")
            exit()
        if is_supported(args[1]):
            to_language = is_supported(args[1])
        else:
            print(f"Sorry, the program doesn't support {args[1]}")
            exit()
        if is_jabberwocky(args[2]):
            print(f'Sorry, unable to find {args[2]}')
            exit()
        else:
            word_to_translate = args[2]

        if to_language == 'all':
            my_file = open(f'{word_to_translate}.txt', 'w')
            menu_items.remove(from_language.capitalize())
            for to_language in menu_items:
                reverso_file(from_language, to_language, word_to_translate, my_file)
            my_file.close()
            f = open(f'{word_to_translate}.txt', 'r')
            file_contents = f.read()
            print(file_contents)
            f.close()
        elif from_language and to_language:
            reverso_search(from_language, to_language, word_to_translate)
    else:
        print("Hello, welcome to the translator. Translator supports:")
        for i, item in enumerate(menu_items, 1):
            print(f'{i}. {item}')
        print('Type the number of your language: ')
        from_choice = int(input())
        print('Type the number of a language you want to translate to or "0" to translate to all languages: ')
        to_choice = int(input())
        print('Type the word you want to translate:')
        word_to_translate = input()
        print('')
        from_language = menu_items[from_choice - 1]
        if to_choice == 0:
            my_file = open(f'{word_to_translate}.txt', 'w')
            menu_items.remove(from_language)
            for to_language in menu_items:
                reverso_file(from_language, to_language, word_to_translate, my_file)
            my_file.close()
            f = open(f'{word_to_translate}.txt', 'r')
            file_contents = f.read()
            print(file_contents)
            f.close()
        else:
            to_language = menu_items[to_choice - 1]
            # print(f'from {from_language}')
            # print(f'to {to_language}')
            reverso_search(from_language, to_language, word_to_translate)


sargs = sys.argv

# if len(args) != 4:
#     print("The script should be called with 3 arguments ex: python translator.py english french hello")
#
# else:
if len(sargs) == 4:
    a = sargs[1]
    b = sargs[2]
    c = sargs[3]
    main_menu(a, b, c)
else:
    main_menu()
