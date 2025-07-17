from abc import ABC
from aiokafka import AIOKafkaProducer
from web.src import config
import asyncio

# Получаем текущий событийный цикл asyncio, который будет использоваться для асинхронных операций с Kafka
event_loop = asyncio.get_event_loop()


# Класс-оболочка над нашим "продьюсером"
class AIOWebProducer(object):
    def __init__(self):
        self.__producer = AIOKafkaProducer(
            bootstrap_servers=config.KAFKA_BOOTSTRAP_SERVERS,
            # loop — это объект, который управляет асинхронными задачами в Python. Здесь мы указываем, какой цикл событий использовать для работы с Kafka.
            loop=event_loop,
        )
        self.__produce_topic = config.PRODUCE_TOPIC

    async def start(self) -> None:
        await self.__producer.start()

    async def stop(self) -> None:
        await self.__producer.stop()
