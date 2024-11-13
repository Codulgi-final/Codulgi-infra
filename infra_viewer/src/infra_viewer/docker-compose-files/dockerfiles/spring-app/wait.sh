#!/bin/sh

# MariaDB가 준비될 때까지 반복하여 연결을 시도
until nc -z -v -w30 mariadb 3306; do
  echo "Waiting for MariaDB to start on port 3306..."
  sleep 5
done

echo "MariaDB is up - executing command"
exec "$@"