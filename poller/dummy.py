from .collector import Collector


class DummyCollector(Collector):

    def poll(self):

        return {
            "source": "Dummy",

            "boss": "Goons",

            "current_map": "Customs",

            "confidence": 1.0
        }
