# StatisticCollector
Collects statistic from Web Scraper

Запустить перед запуском WebScraper

Описание путей:\
api/v1/collect - Принимает Post запрос вида:\

	"url" : "https://spb.hh.ru/search/vacancy?text=scala&area=2",
	"num_of_responses": 55,\
	"last_mod": "today",\
	"status": "create"\
}\
И обновляет или сохраняет новые данные\
api/v1/plot - Принимает Post запрос вида:\
{\
"url" : url\
}\
И строит статистический график для полученного url
