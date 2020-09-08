CREATE DATABASE IF NOT EXISTS gift_app_local_db;
CREATE USER IF NOT EXISTS 'gift_app_local_user'@'localhost' IDENTIFIED BY 'gift_app_LOCAL_p4s$';
GRANT ALL PRIVILEGES ON gift_app_local_db.* TO 'gift_app_local_user'@'localhost';

FLUSH PRIVILEGES;
