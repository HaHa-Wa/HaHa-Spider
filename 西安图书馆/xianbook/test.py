from scrapy import cmdline


name = 'book'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())
