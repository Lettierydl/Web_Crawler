BOT_NAME = 'hotel'
SPIDER_MODULES = ['scraper_app.spiders']
ITEM_PIPELINES = ['scraper_app.coneccao.Coneccao']