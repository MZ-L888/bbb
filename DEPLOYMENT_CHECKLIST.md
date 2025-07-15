# Railway 部署检查清单

## ✅ 部署前检查

### 1. 文件准备
- [x] `railway.json` - Railway 配置文件
- [x] `railway.toml` - Railway 模板配置
- [x] `Dockerfile` - 已优化支持动态端口和SQLite
- [x] `start.sh` - 启动脚本
- [x] `.railwayignore` - 忽略不必要的文件
- [x] `.env.railway` - 环境变量模板
- [x] `RAILWAY_DEPLOYMENT.md` - 详细部署文档
- [x] `README_RAILWAY.md` - 快速部署指南

### 2. 代码修改
- [x] `app/main.py` - 支持动态端口 (PORT 环境变量)
- [x] `app/router/routes.py` - 增强健康检查端点
- [x] 数据库配置 - 默认使用 SQLite

### 3. 配置验证
- [x] 端口配置：支持 Railway 动态端口分配
- [x] 数据库配置：默认 SQLite，支持数据持久化
- [x] 环境变量：完整的配置模板
- [x] 健康检查：增强的 `/health` 端点

## 🚀 部署步骤

### 方法一：一键部署
1. 点击部署按钮：[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https%3A%2F%2Fgithub.com%2Fsnailyp%2Fgemini-balance)
2. 配置必需环境变量
3. 等待部署完成

### 方法二：手动部署
1. 登录 Railway
2. 创建新项目
3. 连接 GitHub 仓库
4. 配置环境变量
5. 部署

## 📋 必需环境变量

```bash
# 必需配置
API_KEYS=["your-gemini-api-key"]
ALLOWED_TOKENS=["sk-your-access-token"]
AUTH_TOKEN=sk-your-admin-token

# 数据库配置（已默认设置）
DATABASE_TYPE=sqlite
SQLITE_DATABASE=gemini_balance.db
```

## 🔧 可选环境变量

参考 `.env.railway` 文件中的完整配置选项。

## ✅ 部署后验证

### 1. 基础检查
- [ ] 应用成功启动
- [ ] 获取 Railway 分配的域名
- [ ] 访问健康检查端点：`https://your-app.up.railway.app/health`

### 2. 功能测试
- [ ] 访问管理界面：`https://your-app.up.railway.app`
- [ ] 使用 AUTH_TOKEN 登录
- [ ] 检查密钥状态页面
- [ ] 测试 API 调用

### 3. API 端点测试

#### OpenAI 格式测试
```bash
curl -X POST "https://your-app.up.railway.app/v1/chat/completions" \
  -H "Authorization: Bearer sk-your-token" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-2.5-pro",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

#### Gemini 格式测试
```bash
curl -X POST "https://your-app.up.railway.app/v1beta/models/gemini-2.5-pro:generateContent" \
  -H "Authorization: Bearer sk-your-token" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{"parts": [{"text": "Hello!"}]}]
  }'
```

#### 模型列表测试
```bash
curl -X GET "https://your-app.up.railway.app/v1/models" \
  -H "Authorization: Bearer sk-your-token"
```

## 🛠️ 故障排除

### 常见问题

1. **部署失败**
   - 检查 Dockerfile 语法
   - 验证环境变量格式
   - 查看 Railway 部署日志

2. **应用启动失败**
   - 检查 PORT 环境变量
   - 验证 API_KEYS 格式
   - 查看应用日志

3. **数据库连接错误**
   - 确认 DATABASE_TYPE=sqlite
   - 检查数据目录权限
   - 验证 SQLite 文件路径

4. **API 调用失败**
   - 验证 Gemini API Key 有效性
   - 检查 ALLOWED_TOKENS 配置
   - 确认请求格式正确

### 调试命令

```bash
# 查看应用日志
railway logs

# 查看环境变量
railway variables

# 重新部署
railway up

# 连接到容器
railway shell
```

## 📊 监控和维护

### 1. Railway 监控
- 查看 Metrics 页面
- 监控资源使用情况
- 设置告警通知

### 2. 应用监控
- 定期检查 `/health` 端点
- 监控 API 调用日志
- 检查密钥状态

### 3. 数据备份
- SQLite 数据库自动持久化
- 定期导出配置设置
- 备份重要日志

## 🔐 安全建议

1. **强密码**：使用复杂的访问令牌
2. **定期轮换**：定期更换 API 密钥
3. **访问控制**：限制令牌数量和权限
4. **监控日志**：定期检查访问日志
5. **HTTPS**：Railway 自动提供 HTTPS

## 📞 获取帮助

- 📖 [完整文档](./RAILWAY_DEPLOYMENT.md)
- 🐛 [GitHub Issues](https://github.com/snailyp/gemini-balance/issues)
- 💬 [Telegram 群组](https://t.me/+soaHax5lyI0wZDVl)
- 🚂 [Railway 文档](https://docs.railway.app/)

## 🎉 部署成功！

恭喜！您的 Gemini Balance 应用已成功部署到 Railway。

现在您可以：
- 使用 OpenAI 兼容的 API 格式
- 享受多密钥负载均衡
- 通过 Web 界面管理配置
- 监控 API 使用情况

---

**享受您的 AI API 代理服务！** 🚀
