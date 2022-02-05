import os


class Config:
    PROXY_WEBPAGE = "https://free-proxy-list.net/"

    TESTING_URL = "https://google.com"

    REDIS_HOST = f"{os.getenv('REDIS_HOST', '127.0.0.1')}"
    REDIS_PORT = f"{os.getenv('REDIS_HOST', '6379')}"

    KAFKA_HOST = f"{os.getenv('KAFKA_HOST', '127.0.0.1')}"
    KAFKA_PORT = f"{os.getenv('KAFKA_PORT', '9092')}"

    BOOTSTRAP_SERVERS = [f"{KAFKA_HOST}:{KAFKA_PORT}"]
    TOPIC_NEWS = "data_bank_topic_news"

    REDIS_CONFIG = {
        "host": REDIS_HOST,
        "port": REDIS_PORT,
        "db": 0
    }

    REDIS_KEY = "proxies"

    MAX_WORKERS = 50

    NUMBER_OF_PROXIES = 50

    RSS_FEEDS = {
        "en": [
            "https://www.goal.com/feeds/en/news",
            "https://www.eyefootball.com/football_news.xml",
            "https://www.101greatgoals.com/feed/",
            "https://sportslens.com/feed/",
            "https://deadspin.com/rss"
        ],
        "es": [
            "https://as.com/rss/tags/ultimas_noticias.xml",
            "https://e00-marca.uecdn.es/rss/futbol/mas-futbol.xml",
            "https://www.futbolred.com/rss-news/liga-de-espana.xml",
            "https://www.futbolya.com/rss/noticias.xml"
        ],
    }

    VALIDATOR_CONFIG = {
        "description_length": 10,
        "languages": [
            "en", "es"
        ]
    }
