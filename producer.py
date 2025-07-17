# producer - сервис, который отправляет сообщения в брокер
import time
from pika import BlockingConnection, ConnectionParameters

# Настройка подключения к брокеру
connection = BlockingConnection(ConnectionParameters('localhost'))
channel = connection.channel() # канал, с которым работает соединение

# Создаём очередь (если не существует)
channel.queue_declare(queue='notifications')

for i in range(1000):
    # Отправляем сообщение
    channel.basic_publish(
        exchange='',
        routing_key='notifications',
        body=f'Hello, RabbitMQ {i}'
    )
    print("Сообщение отправлено!")
    time.sleep(1)

# Закрываем соединение
connection.close()