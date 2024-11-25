from celery import Celery

# Tạo một ứng dụng Celery
app = Celery("tasks", broker="amqp://guest:guest@rabbitmq:5672//")


# Định nghĩa một task đơn giản
@app.task
def add(x, y):
    return x + y
