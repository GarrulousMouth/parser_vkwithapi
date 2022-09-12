import parser.params as params
import httplib2
import shutil
import requests
import os

def parse_img(domain, links_img, post_id):
    resource = httplib2.Http('.cache')
    for i, img in enumerate(links_img):
        if 'photo' in img:
            size = img['photo']['sizes'][-1]
            _, content = resource.request(size['url'])
            with open(f'img_{domain}/img{post_id}_{i}.jpg', 'wb') as f:
                f.write(content)
    shutil.rmtree('.cache')


def parse(link, parser_img=False, parser_links=False, count=1):
    domain = link.split('/')[-1]
    if parser_img:
        if not os.path.exists(f'img_{domain}'):
            os.makedirs(f'img_{domain}')
    answer = requests.get(f'https://api.vk.com/method/wall.get?domain={domain}&count={count}&access_token={params.SERVICE_TOKEN}&v=5.131')
    print(answer.json())
    with open(f'text{domain}.txt', 'w', encoding='utf-8') as f:
        for post in answer.json()['response']['items']:
            from_id = post['from_id']
            id = post['id']
            if 'is_pinned' not in post:
                f.write(f'Пост {post["id"]}\n{post["text"]}\n')
                if parser_links:
                    f.write(f'https://vk.com/wall{from_id}_{id}\n')
                f.write('\n')
                if parser_img:
                    if 'attachments' in post and 'photo' in post['attachments'][0]:
                        parse_img(domain, post['attachments'], post["id"])

if __name__ == '__main__':
    parse(link='https://vk.com/panama56', parser_img=True, parser_links=True)
