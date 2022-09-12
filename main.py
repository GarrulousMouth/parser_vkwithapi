import re
from parser import parser_post

def main():
    links = []
    print('Вставьте ссылку на группу или введите «n», чтобы продолжить: ')
    link = input().rstrip()
    while re.fullmatch(r'https://.*vk.com/.+', link) is not None:
        parser_img = (False, True)[input('Парсинг изображений +/-: ') == '+']
        parser_links = (False, True)[input('Парсинг ссылок на пост +/-: ') == '+']
        links.append((link, parser_img, parser_links))
        print('\nВставьте ссылку на группу или введите «n», чтобы продолжить: ')
        link = input().rstrip()

    count = input('Количество постов(максимум 100): ')
    while not count.isdigit():
        print('Должно быть число')
        count = input('Количество постов(максимум 100): ')
    if len(links) == 0:
        return print('Нечего парсить')

    for link in links:
        parser_post.parse(*link, count)


if __name__ == '__main__':
    main()