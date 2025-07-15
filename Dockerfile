FROM python:3.10-slim

WORKDIR /app

# 复制所需文件到容器中
COPY ./requirements.txt /app
COPY ./VERSION /app

RUN pip install --no-cache-dir -r requirements.txt
COPY ./app /app/app
COPY ./start.sh /app/start.sh

# 创建数据目录用于SQLite数据库，并设置权限
RUN mkdir -p /app/data && chmod 755 /app/data && chmod +x /app/start.sh

# 设置默认环境变量 - Railway部署时使用SQLite
ENV DATABASE_TYPE=sqlite
ENV SQLITE_DATABASE=gemini_balance.db
ENV API_KEYS='["your_api_key_1"]'
ENV ALLOWED_TOKENS='["your_token_1"]'
ENV BASE_URL=https://generativelanguage.googleapis.com/v1beta
ENV TOOLS_CODE_EXECUTION_ENABLED=false
ENV IMAGE_MODELS='["gemini-2.0-flash-exp", "gemini-2.5-pro"]'
ENV SEARCH_MODELS='["gemini-2.0-flash-exp", "gemini-2.5-pro"]'
ENV URL_NORMALIZATION_ENABLED=false
ENV CLOUDFLARE_IMGBED_UPLOAD_FOLDER=""

# Expose port (Railway会动态分配端口)
EXPOSE $PORT

# Run the application - 使用启动脚本
CMD ["/app/start.sh"]
