# Railway 部署指南

本指南将帮助您将 Gemini Balance 项目部署到 Railway 平台。

## 🚀 快速部署

### 方法一：一键部署 (推荐)

点击下面的按钮直接部署到 Railway：

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https%3A%2F%2Fgithub.com%2Fsnailyp%2Fgemini-balance)

### 方法二：从 GitHub 仓库部署

1. **登录 Railway**
   - 访问 [Railway.app](https://railway.app)
   - 使用 GitHub 账号登录

2. **创建新项目**
   - 点击 "New Project"
   - 选择 "Deploy from GitHub repo"
   - 选择您的 Gemini Balance 仓库

3. **配置环境变量**
   - 在项目设置中添加环境变量
   - 参考下面的环境变量配置部分

## 📋 环境变量配置

### 必需配置

在 Railway 项目的 Variables 页面中添加以下环境变量：

```bash
# 数据库配置
DATABASE_TYPE=sqlite
SQLITE_DATABASE=gemini_balance.db

# Gemini API Keys (必需)
API_KEYS=["AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"]

# 访问令牌 (必需)
ALLOWED_TOKENS=["sk-your-access-token-here"]

# 管理员令牌
AUTH_TOKEN=sk-your-admin-token-here
```

### 可选配置

```bash
# API 配置
BASE_URL=https://generativelanguage.googleapis.com/v1beta
TEST_MODEL=gemini-1.5-flash

# 功能配置
IMAGE_MODELS=["gemini-2.0-flash-exp", "gemini-2.5-pro"]
SEARCH_MODELS=["gemini-2.0-flash-exp", "gemini-2.5-pro"]
TOOLS_CODE_EXECUTION_ENABLED=false

# 日志配置
LOG_LEVEL=INFO
AUTO_DELETE_ERROR_LOGS_ENABLED=true
AUTO_DELETE_ERROR_LOGS_DAYS=7
```

完整的环境变量配置请参考项目根目录下的 `.env.railway` 文件。

## 🔧 部署配置

项目已包含以下配置文件以支持 Railway 部署：

### railway.json
```json
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "DOCKERFILE",
    "dockerfilePath": "Dockerfile"
  },
  "deploy": {
    "numReplicas": 1,
    "sleepApplication": false,
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
```

### Dockerfile 优化
- 支持 Railway 动态端口分配
- 默认使用 SQLite 数据库
- 优化了数据持久化

## 📊 数据库选择

### SQLite (推荐)
- **优点**: 无需额外配置，数据自动持久化
- **适用**: 中小型应用，个人使用
- **配置**: 
  ```bash
  DATABASE_TYPE=sqlite
  SQLITE_DATABASE=gemini_balance.db
  ```

### Railway PostgreSQL (可选)
如果需要更强的数据库性能，可以添加 Railway PostgreSQL 插件：

1. 在项目中添加 PostgreSQL 插件
2. 修改环境变量：
   ```bash
   DATABASE_TYPE=postgresql
   DATABASE_URL=${{Postgres.DATABASE_URL}}
   ```

## 🌐 访问应用

部署完成后：

1. **获取应用URL**
   - 在 Railway 项目页面查看生成的域名
   - 格式通常为: `https://your-app-name.up.railway.app`

2. **首次访问**
   - 访问应用URL
   - 使用配置的 `AUTH_TOKEN` 登录管理界面

3. **API 端点**
   - OpenAI 兼容: `https://your-app.up.railway.app/v1`
   - Gemini 原生: `https://your-app.up.railway.app/v1beta`

## 🔐 安全配置

### 1. 更改默认令牌
```bash
# 生成强密码作为访问令牌
ALLOWED_TOKENS=["sk-$(openssl rand -hex 32)"]
AUTH_TOKEN=sk-$(openssl rand -hex 32)
```

### 2. API Key 安全
- 不要在代码中硬编码 API Key
- 定期轮换 Gemini API Key
- 监控 API 使用情况

### 3. 访问控制
- 限制 `ALLOWED_TOKENS` 的数量
- 定期检查访问日志

## 📈 监控和维护

### 1. 应用监控
- Railway 提供内置的应用监控
- 查看 Metrics 页面了解资源使用情况

### 2. 日志查看
- 在 Railway 项目的 Deployments 页面查看日志
- 应用内置日志管理功能

### 3. 数据备份
- SQLite 数据库文件会自动持久化
- 建议定期导出重要配置

## 🛠️ 故障排除

### 常见问题

1. **应用启动失败**
   - 检查环境变量配置是否正确
   - 确认 API_KEYS 和 ALLOWED_TOKENS 格式正确

2. **数据库连接错误**
   - 确认 DATABASE_TYPE 设置正确
   - SQLite 模式下检查文件权限

3. **API 调用失败**
   - 验证 Gemini API Key 是否有效
   - 检查网络连接和代理设置

### 调试步骤

1. **查看部署日志**
   ```bash
   # 在 Railway 项目页面查看 Deployments 日志
   ```

2. **检查环境变量**
   ```bash
   # 确认所有必需的环境变量都已设置
   ```

3. **测试 API 连接**
   ```bash
   curl -X GET "https://your-app.up.railway.app/health"
   ```

## 📞 支持

如果遇到问题：

1. 查看项目 [GitHub Issues](https://github.com/snailyp/gemini-balance/issues)
2. 加入 [Telegram 群组](https://t.me/+soaHax5lyI0wZDVl)
3. 参考原项目文档

## 🔄 更新部署

当项目有更新时：

1. **自动部署**: 如果连接了 GitHub，推送代码会自动触发部署
2. **手动部署**: 在 Railway 项目页面点击 "Deploy" 按钮
3. **回滚**: 在 Deployments 页面可以回滚到之前的版本

---

**注意**: 请确保遵守 Gemini API 的使用条款和 Railway 的服务条款。
