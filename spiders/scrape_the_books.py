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
        all_books = response.css('ol.row li')
        for book in all_books:
            img_src = book.css('article.product_pod a img::attr(src)').get()
            title = book.css('article.product_pod h3 a::attr(title)').get()
            price = book.css('div.product_price p.price_color::text').get()

            result = {
                'img_src': img_src,
                'title': title,
                'price': price
            }
            yield  result








