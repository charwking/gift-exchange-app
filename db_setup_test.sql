CREATE DATABASE IF NOT EXISTS gift_app_test_db;
CREATE USER IF NOT EXISTS 'gift_app_test_user'@'localhost' IDENTIFIED BY 'gift_app_TEST_p4s$';
GRANT ALL PRIVILEGES ON gift_app_test_db.* TO 'gift_app_test_user'@'localhost';

FLUSH PRIVILEGES;
