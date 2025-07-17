# consumer - сервис, который читает сообщения из брокера
from pika import BlockingConnection, ConnectionParameters

# Настройка подключения к брокеру
connection = BlockingConnection(ConnectionParameters('localhost'))
channel = connection.channel()

# Создаём очередь (если не существует)
channel.queue_declare(queue='notifications')

# Функция для обработки полученного сообщения
def callback(ch, method, properties, body):
    print(f"Получено сообщение: {body.decode()}")

# Настраиваем получение сообщений из очереди
channel.basic_consume(
    queue='notifications',
    on_message_callback=callback,
    auto_ack=True
)

print("Ожидание сообщений...")
channel.start_consuming()