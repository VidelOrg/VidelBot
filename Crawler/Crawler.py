import os
from icrawler.builtin import BingImageCrawler
def getImages(theme, image, num=1):
    crawler = BingImageCrawler(storage={'root_dir': f'images'})
    crawler.crawl(keyword = theme+' '+image, max_num = num)
    os.system(f"mv images/000001.jpg images/{image}.jpg")