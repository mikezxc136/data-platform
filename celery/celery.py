from celery import Celery

# Khởi tạo ứng dụng Celery
app = Celery("app")

# Cấu hình Celery từ file settings hoặc trực tiếp
app.conf.broker_url = "amqp://guest:guest@rabbitmq:5672//"
app.conf.result_backend = "rpc://"

# Tự động phát hiện các task từ các module khác
app.autodiscover_tasks(["app"])
