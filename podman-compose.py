import sys
from podman_compose import main

sys.argv = ["podman-compose", "up"]  # Thay "up" bằng lệnh bạn muốn sử dụng
main()
