# StatisticCollector
Collects statistic from Web Scraper

Запустить перед запуском WebScraper

Описание путей:\
api/v1/collect - Принимает Post запрос и обновляет или сохраняет новые данные\
api/v1/plot - Принимает Post запрос вида:\
{"url" : url}\
И строит статистический график для полученного url