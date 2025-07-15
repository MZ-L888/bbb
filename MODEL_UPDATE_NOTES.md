# 模型更新说明

## 🆕 新增模型：gemini-2.5-pro

### 更新内容

已将 `gemini-2.5-pro` 模型添加到支持的模型列表中，现在支持以下功能：

#### ✅ 支持的功能
- **图像处理** (`IMAGE_MODELS`)
- **搜索功能** (`SEARCH_MODELS`)
- **标准聊天对话**

#### 📋 更新的配置文件

1. **`app/config/config.py`** - 核心配置
2. **`.env.railway`** - Railway 环境变量模板
3. **`.env.example`** - 环境变量示例
4. **`railway.toml`** - Railway 模板配置
5. **`Dockerfile`** - Docker 默认环境变量
6. **`app/static/js/config_editor.js`** - 前端默认配置
7. **部署文档** - 更新了相关说明

### 🚀 如何使用

#### 1. 标准聊天
```bash
curl -X POST "https://your-app.up.railway.app/v1/chat/completions" \
  -H "Authorization: Bearer sk-your-token" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-2.5-pro",
    "messages": [
      {"role": "user", "content": "Hello!"}
    ]
  }'
```

#### 2. 图像处理功能
```bash
curl -X POST "https://your-app.up.railway.app/v1/chat/completions" \
  -H "Authorization: Bearer sk-your-token" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-2.5-pro-image",
    "messages": [
      {"role": "user", "content": "分析这张图片"}
    ]
  }'
```

#### 3. 搜索功能
```bash
curl -X POST "https://your-app.up.railway.app/v1/chat/completions" \
  -H "Authorization: Bearer sk-your-token" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-2.5-pro-search",
    "messages": [
      {"role": "user", "content": "搜索最新的AI新闻"}
    ]
  }'
```

### 📊 模型特性

| 模型 | 功能 | 描述 |
|------|------|------|
| `gemini-2.5-pro` | 标准聊天 | 高性能对话模型 |
| `gemini-2.5-pro-image` | 图像处理 | 支持图像分析和生成 |
| `gemini-2.5-pro-search` | 网络搜索 | 支持实时网络搜索 |

### 🔧 配置说明

#### 环境变量配置
```bash
# 支持图像功能的模型
IMAGE_MODELS=["gemini-2.0-flash-exp", "gemini-2.5-pro"]

# 支持搜索功能的模型
SEARCH_MODELS=["gemini-2.0-flash-exp", "gemini-2.5-pro"]
```

#### 管理界面配置
1. 登录管理界面：`https://your-app.up.railway.app`
2. 进入配置页面
3. 在模型配置部分可以看到新增的 `gemini-2.5-pro` 选项
4. 根据需要启用或禁用相关功能

### 🔄 升级现有部署

#### Railway 部署
如果你已经在 Railway 上部署了应用：

1. **自动更新**：如果连接了 GitHub，推送代码会自动触发重新部署
2. **手动更新**：在 Railway 项目页面点击 "Deploy" 按钮
3. **环境变量**：无需修改现有环境变量，新模型会自动可用

#### 本地部署
```bash
# 拉取最新代码
git pull origin main

# 重启应用
docker-compose down
docker-compose up -d
```

### ⚠️ 注意事项

1. **API Key 要求**：确保你的 Gemini API Key 支持 `gemini-2.5-pro` 模型
2. **配额限制**：新模型可能有不同的配额和费率限制
3. **功能测试**：建议先测试基本功能，再启用高级功能

### 🐛 故障排除

#### 模型不可用
```json
{
  "error": "Model gemini-2.5-pro is not supported"
}
```

**解决方案**：
1. 检查 API Key 是否支持该模型
2. 确认模型名称拼写正确
3. 查看应用日志获取详细错误信息

#### 功能模型不工作
如果 `gemini-2.5-pro-image` 或 `gemini-2.5-pro-search` 不工作：

1. 检查环境变量配置
2. 确认模型在 `IMAGE_MODELS` 或 `SEARCH_MODELS` 列表中
3. 重启应用使配置生效

### 📞 获取帮助

- 📖 [完整文档](./RAILWAY_DEPLOYMENT.md)
- 🐛 [GitHub Issues](https://github.com/snailyp/gemini-balance/issues)
- 💬 [Telegram 群组](https://t.me/+soaHax5lyI0wZDVl)

---

**享受新的 gemini-2.5-pro 模型！** 🎉
