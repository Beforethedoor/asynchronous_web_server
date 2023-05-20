from time import time

import requests

URL = "https://loremflickr.com/320/240/paris,girl/all"
COUNT_PICTURE_TO_DOWNLOAD = 10


def get_file(url):
    response = requests.get(url=url, allow_redirects=True)
    return response


def write_file(response):
    file_name = response.url.split("/")[-1]
    with open(file_name, "wb") as file:
        file.write(response.content)


def main():
    for _ in range(COUNT_PICTURE_TO_DOWNLOAD):
        write_file(get_file(URL))


if __name__ == "__main__":
    start_time = time()
    main()
    print(time() - start_time)
