from icrawler.builtin import BingImageCrawler
BingImageCrawler = BingImageCrawler(storage={'root_dir': 'images'})
BingImageCrawler.crawl(keyword = 'sad human faces', max_num = 5)
