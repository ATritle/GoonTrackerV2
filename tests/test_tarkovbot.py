from poller.collectors.tarkovbot import TarkovBotCollector

collector = TarkovBotCollector()

result = collector.poll()

print(result)