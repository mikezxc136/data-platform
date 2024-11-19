#Data Platform

### Branch Naming Convention

Để đảm bảo tính rõ ràng và dễ quản lý, các nhánh trong dự án được đặt tên theo quy tắc sau:

- **Nhánh chính (`prd`)**: Chứa mã nguồn ổn định, đã được kiểm duyệt, sẵn sàng triển khai.
- **Nhánh phát triển cá nhân (`dev/<tên>`)**: Ví dụ `dev/duy`, `dev/an`, nơi thành viên làm việc riêng.
- **Nhánh tính năng (`feature/<mô-tả-tính-năng>`)**: Ví dụ `feature/login-page`, dùng để phát triển tính năng cụ thể.
- **Nhánh sửa lỗi (`bugfix/<mô-tả-lỗi>`)**: Ví dụ `bugfix/fix-header`, sửa lỗi trong ứng dụng.

> **Lưu ý**: Mọi thay đổi cần thông qua Pull Request để đảm bảo chất lượng. Tránh đặt tên nhánh chung chung như `test` hoặc `update`.
