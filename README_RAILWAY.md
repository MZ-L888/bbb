# Gemini Balance - Railway 一键部署

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https%3A%2F%2Fgithub.com%2Fsnailyp%2Fgemini-balance)

## 🚀 快速开始

1. **点击上方按钮一键部署到 Railway**
2. **配置必需的环境变量**：
   ```
   API_KEYS=["your-gemini-api-key"]
   ALLOWED_TOKENS=["sk-your-access-token"]
   ```
3. **等待部署完成**
4. **访问您的应用**

## 📋 必需环境变量

| 变量名 | 说明 | 示例 |
|--------|------|------|
| `API_KEYS` | Gemini API 密钥列表 | `["AIzaSyXXXXXXXXXXXXXXXXXX"]` |
| `ALLOWED_TOKENS` | 访问令牌列表 | `["sk-your-token"]` |
| `AUTH_TOKEN` | 管理员令牌 | `sk-admin-token` |

## 🔧 可选配置

```bash
# 功能开关
TOOLS_CODE_EXECUTION_ENABLED=false
SHOW_SEARCH_LINK=true
URL_NORMALIZATION_ENABLED=false

# 模型配置
IMAGE_MODELS=["gemini-2.0-flash-exp", "gemini-2.5-pro"]
SEARCH_MODELS=["gemini-2.0-flash-exp", "gemini-2.5-pro"]
TEST_MODEL=gemini-1.5-flash

# 日志配置
LOG_LEVEL=INFO
AUTO_DELETE_ERROR_LOGS_ENABLED=true
```

## 🌐 API 端点

部署完成后，您可以通过以下端点访问 API：

- **OpenAI 兼容格式**: `https://your-app.up.railway.app/v1`
- **Gemini 原生格式**: `https://your-app.up.railway.app/v1beta`
- **管理界面**: `https://your-app.up.railway.app`

## 📖 使用示例

### OpenAI 格式调用

```bash
curl -X POST "https://your-app.up.railway.app/v1/chat/completions" \
  -H "Authorization: Bearer sk-your-token" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-1.5-flash",
    "messages": [
      {"role": "user", "content": "Hello!"}
    ]
  }'
```

### Gemini 格式调用

```bash
curl -X POST "https://your-app.up.railway.app/v1beta/models/gemini-1.5-flash:generateContent" \
  -H "Authorization: Bearer sk-your-token" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {"parts": [{"text": "Hello!"}]}
    ]
  }'
```

## 🔐 安全建议

1. **使用强密码**: 生成复杂的访问令牌
2. **定期轮换**: 定期更换 API 密钥和访问令牌
3. **监控使用**: 定期检查 API 调用日志
4. **限制访问**: 只分享必要的访问令牌

## 📊 功能特性

- ✅ **多密钥负载均衡**: 支持多个 Gemini API 密钥轮询
- ✅ **双协议兼容**: 同时支持 OpenAI 和 Gemini API 格式
- ✅ **可视化管理**: Web 界面管理密钥和配置
- ✅ **自动重试**: 智能错误处理和重试机制
- ✅ **流式响应**: 支持流式输出优化
- ✅ **图像处理**: 支持图像生成和编辑
- ✅ **Web 搜索**: 集成搜索功能
- ✅ **数据持久化**: SQLite 数据库自动备份

## 🛠️ 故障排除

### 常见问题

1. **部署失败**: 检查环境变量格式是否正确
2. **API 调用失败**: 验证 Gemini API 密钥是否有效
3. **访问被拒绝**: 确认访问令牌配置正确

### 获取帮助

- 📖 [完整文档](./RAILWAY_DEPLOYMENT.md)
- 🐛 [GitHub Issues](https://github.com/snailyp/gemini-balance/issues)
- 💬 [Telegram 群组](https://t.me/+soaHax5lyI0wZDVl)

## 📄 许可证

本项目采用 CC BY-NC 4.0 许可证，禁止商业用途。

---

**享受您的 Gemini API 代理服务！** 🎉
