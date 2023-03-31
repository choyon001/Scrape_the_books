from pathlib import Path
import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"

    def start_requests(self):
        urls = [
            'https://books.toscrape.com/catalogue/page-1.html'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-1]
        filename = f'books-{page}'
        Path(filename).write_bytes(response.body)
        self.log(f'Saved file {filename}')




