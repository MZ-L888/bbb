#!/bin/bash

# Railway 启动脚本
# 确保数据目录存在并设置正确权限

echo "Starting Gemini Balance on Railway..."

# 创建数据目录
mkdir -p /app/data
chmod 755 /app/data

# 设置默认端口（如果未设置）
export PORT=${PORT:-8000}

echo "Port: $PORT"
echo "Database Type: $DATABASE_TYPE"
echo "SQLite Database: $SQLITE_DATABASE"

# 启动应用
exec python -m app.main
