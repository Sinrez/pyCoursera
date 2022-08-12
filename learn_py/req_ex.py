import pprint
import requests

urls = ('http://headfirstlabs.com', 'http://oreilly.com', 'http://twitter.com')


# for resp in (requests.get(url) for url in urls):
#     print(len(resp.content), '->', resp.status_code, '->', resp.url)


def gen_from_urls(urls: tuple) -> tuple:
    for resp in (requests.get(url) for url in urls):
        yield len(resp.content), resp.status_code, resp.url


if __name__ == '__main__':
    urls_res = {url: [size, status] for size, status, url in gen_from_urls(urls)}
    pprint.pprint(urls_res)
