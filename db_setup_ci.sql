CREATE DATABASE IF NOT EXISTS gift_app_ci_db;
CREATE USER IF NOT EXISTS 'gift_app_ci_user'@'%' IDENTIFIED BY 'gift_app_CI_p4s$';
GRANT ALL PRIVILEGES ON gift_app_ci_db.* TO 'gift_app_ci_user'@'%';

FLUSH PRIVILEGES;
