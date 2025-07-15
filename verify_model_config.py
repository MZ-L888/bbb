#!/usr/bin/env python3
"""
简单的模型配置验证脚本
不依赖外部库，直接检查配置文件
"""

import json
import re
from pathlib import Path

def check_file_content(file_path, model_name="gemini-2.5-pro"):
    """检查文件是否包含指定模型"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            return model_name in content
    except Exception as e:
        print(f"❌ 读取文件 {file_path} 失败: {e}")
        return False

def extract_models_from_config(file_path, pattern):
    """从配置文件中提取模型列表"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        matches = re.findall(pattern, content)
        models = []
        for match in matches:
            try:
                # 尝试解析 JSON 数组
                model_list = json.loads(match)
                models.extend(model_list)
            except:
                # 如果不是有效的 JSON，跳过
                continue
        return models
    except Exception as e:
        print(f"❌ 解析文件 {file_path} 失败: {e}")
        return []

def main():
    """主函数"""
    print("🚀 开始验证 gemini-2.5-pro 模型配置...")
    print("=" * 60)
    
    project_root = Path(".")
    model_name = "gemini-2.5-pro"
    
    # 检查的文件列表
    files_to_check = [
        {
            "path": ".env.railway",
            "description": "Railway 环境变量模板"
        },
        {
            "path": ".env.example", 
            "description": "环境变量示例文件"
        },
        {
            "path": "railway.toml",
            "description": "Railway 配置文件"
        },
        {
            "path": "Dockerfile",
            "description": "Docker 配置文件"
        },
        {
            "path": "RAILWAY_DEPLOYMENT.md",
            "description": "Railway 部署文档"
        },
        {
            "path": "README_RAILWAY.md", 
            "description": "Railway 快速指南"
        }
    ]
    
    print("📄 检查配置文件:")
    all_passed = True
    
    for file_info in files_to_check:
        file_path = project_root / file_info["path"]
        if file_path.exists():
            if check_file_content(file_path, model_name):
                print(f"✅ {file_info['description']}: 包含 {model_name}")
            else:
                print(f"❌ {file_info['description']}: 未包含 {model_name}")
                all_passed = False
        else:
            print(f"❌ {file_info['description']}: 文件不存在")
            all_passed = False
    
    print("\n🔍 详细检查模型配置:")
    
    # 检查 .env.railway 中的模型配置
    env_railway = project_root / ".env.railway"
    if env_railway.exists():
        print(f"\n📋 {env_railway.name} 中的模型配置:")
        
        # 检查 IMAGE_MODELS
        image_pattern = r'IMAGE_MODELS=(\[.*?\])'
        image_models = extract_models_from_config(env_railway, image_pattern)
        if image_models:
            print(f"🖼️  IMAGE_MODELS: {image_models}")
            if model_name in image_models:
                print(f"✅ {model_name} 在 IMAGE_MODELS 中")
            else:
                print(f"❌ {model_name} 不在 IMAGE_MODELS 中")
                all_passed = False
        
        # 检查 SEARCH_MODELS
        search_pattern = r'SEARCH_MODELS=(\[.*?\])'
        search_models = extract_models_from_config(env_railway, search_pattern)
        if search_models:
            print(f"🔍 SEARCH_MODELS: {search_models}")
            if model_name in search_models:
                print(f"✅ {model_name} 在 SEARCH_MODELS 中")
            else:
                print(f"❌ {model_name} 不在 SEARCH_MODELS 中")
                all_passed = False
    
    # 检查 railway.toml
    railway_toml = project_root / "railway.toml"
    if railway_toml.exists():
        print(f"\n📋 {railway_toml.name} 中的模型配置:")
        
        # 检查 IMAGE_MODELS
        image_pattern = r'IMAGE_MODELS = \'(\[.*?\])\''
        image_models = extract_models_from_config(railway_toml, image_pattern)
        if image_models:
            print(f"🖼️  IMAGE_MODELS: {image_models}")
            if model_name in image_models:
                print(f"✅ {model_name} 在 IMAGE_MODELS 中")
            else:
                print(f"❌ {model_name} 不在 IMAGE_MODELS 中")
                all_passed = False
        
        # 检查 SEARCH_MODELS
        search_pattern = r'SEARCH_MODELS = \'(\[.*?\])\''
        search_models = extract_models_from_config(railway_toml, search_pattern)
        if search_models:
            print(f"🔍 SEARCH_MODELS: {search_models}")
            if model_name in search_models:
                print(f"✅ {model_name} 在 SEARCH_MODELS 中")
            else:
                print(f"❌ {model_name} 不在 SEARCH_MODELS 中")
                all_passed = False
    
    print("\n" + "=" * 60)
    
    if all_passed:
        print("🎉 所有检查通过！gemini-2.5-pro 模型已正确配置")
        print("\n✨ 下一步:")
        print("1. 部署到 Railway")
        print("2. 配置环境变量中的 API_KEYS 和 ALLOWED_TOKENS")
        print("3. 测试模型功能:")
        print("   - 标准聊天: gemini-2.5-pro")
        print("   - 图像处理: gemini-2.5-pro-image") 
        print("   - 搜索功能: gemini-2.5-pro-search")
    else:
        print("❌ 部分检查未通过，请检查上述错误")
    
    print("\n📚 相关文档:")
    print("- 查看 MODEL_UPDATE_NOTES.md 了解详细使用说明")
    print("- 查看 RAILWAY_DEPLOYMENT.md 了解部署步骤")

if __name__ == "__main__":
    main()
