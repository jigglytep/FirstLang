import scrapy


class QuotesSpider(scrapy.Spider):
    name = "lang"

    def start_requests(self):
        urls = [
        'https://www.dice.com/jobs?q=Junior+Developer&l=10025'
        ]

        for i,x in enumerate(response.css('a.dice-btn-link').extract()):
            if x.__contains__("position"):
                a.append(response.css('a.dice-btn-link::attr(href)')[i].extract())

        import nltk
        from nltk.corpus import stopwords
        from nltk.tokenize import sent_tokenize, word_tokenize

        a = response.css('div.iconsiblings::text').extract()#
        data = a[0].strip().replace('(','').replace(')','').lower()

        stopWords = set(stopwords.words('english'))
        words = word_tokenize(data)
        wordsFiltered = []
 
        for w in words:
            if w not in stopWords:
                wordsFiltered.append(w)

        print(wordsFiltered)

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
