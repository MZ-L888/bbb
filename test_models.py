#!/usr/bin/env python3
"""
模型配置测试脚本
用于验证 gemini-2.5-pro 模型是否正确配置
"""

import os
import sys
import json
from pathlib import Path

# 添加项目根目录到 Python 路径
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

def test_config_import():
    """测试配置导入"""
    try:
        from app.config.config import settings
        print("✅ 配置导入成功")
        return settings
    except Exception as e:
        print(f"❌ 配置导入失败: {e}")
        return None

def test_model_configuration(settings):
    """测试模型配置"""
    print("\n📋 模型配置检查:")
    
    # 检查 SEARCH_MODELS
    print(f"🔍 SEARCH_MODELS: {settings.SEARCH_MODELS}")
    if "gemini-2.5-pro" in settings.SEARCH_MODELS:
        print("✅ gemini-2.5-pro 已添加到 SEARCH_MODELS")
    else:
        print("❌ gemini-2.5-pro 未在 SEARCH_MODELS 中")
    
    # 检查 IMAGE_MODELS
    print(f"🖼️  IMAGE_MODELS: {settings.IMAGE_MODELS}")
    if "gemini-2.5-pro" in settings.IMAGE_MODELS:
        print("✅ gemini-2.5-pro 已添加到 IMAGE_MODELS")
    else:
        print("❌ gemini-2.5-pro 未在 IMAGE_MODELS 中")
    
    # 检查 FILTERED_MODELS
    print(f"🚫 FILTERED_MODELS: {settings.FILTERED_MODELS}")
    if "gemini-2.5-pro" not in settings.FILTERED_MODELS:
        print("✅ gemini-2.5-pro 未被过滤")
    else:
        print("❌ gemini-2.5-pro 被错误过滤")

def test_model_service():
    """测试模型服务"""
    try:
        from app.service.model.model_service import ModelService
        model_service = ModelService()
        
        print("\n🔧 模型服务测试:")
        
        # 测试模型支持检查
        models_to_test = [
            "gemini-2.5-pro",
            "gemini-2.5-pro-search", 
            "gemini-2.5-pro-image"
        ]
        
        for model in models_to_test:
            # 注意：这里需要模拟，因为实际检查需要 API 密钥
            print(f"📝 测试模型: {model}")
            # 这里只是检查配置，不进行实际 API 调用
        
        print("✅ 模型服务导入成功")
        
    except Exception as e:
        print(f"❌ 模型服务测试失败: {e}")

def test_environment_files():
    """测试环境变量文件"""
    print("\n📄 环境变量文件检查:")
    
    files_to_check = [
        ".env.railway",
        ".env.example", 
        "railway.toml"
    ]
    
    for file_path in files_to_check:
        full_path = project_root / file_path
        if full_path.exists():
            try:
                content = full_path.read_text(encoding='utf-8')
                if "gemini-2.5-pro" in content:
                    print(f"✅ {file_path}: 包含 gemini-2.5-pro")
                else:
                    print(f"❌ {file_path}: 未包含 gemini-2.5-pro")
            except Exception as e:
                print(f"❌ {file_path}: 读取失败 - {e}")
        else:
            print(f"❌ {file_path}: 文件不存在")

def test_dockerfile():
    """测试 Dockerfile 配置"""
    print("\n🐳 Dockerfile 检查:")
    
    dockerfile_path = project_root / "Dockerfile"
    if dockerfile_path.exists():
        try:
            content = dockerfile_path.read_text(encoding='utf-8')
            if "gemini-2.5-pro" in content:
                print("✅ Dockerfile: 包含 gemini-2.5-pro")
            else:
                print("❌ Dockerfile: 未包含 gemini-2.5-pro")
        except Exception as e:
            print(f"❌ Dockerfile: 读取失败 - {e}")
    else:
        print("❌ Dockerfile: 文件不存在")

def main():
    """主函数"""
    print("🚀 开始模型配置测试...")
    print("=" * 50)
    
    # 设置环境变量以避免配置错误
    os.environ.setdefault("API_KEYS", '["test-key"]')
    os.environ.setdefault("ALLOWED_TOKENS", '["test-token"]')
    os.environ.setdefault("DATABASE_TYPE", "sqlite")
    
    # 测试配置导入
    settings = test_config_import()
    if not settings:
        print("❌ 无法继续测试，配置导入失败")
        return
    
    # 测试模型配置
    test_model_configuration(settings)
    
    # 测试模型服务
    test_model_service()
    
    # 测试环境变量文件
    test_environment_files()
    
    # 测试 Dockerfile
    test_dockerfile()
    
    print("\n" + "=" * 50)
    print("🎉 模型配置测试完成!")
    print("\n💡 提示:")
    print("- 如果所有检查都通过，说明 gemini-2.5-pro 模型已正确配置")
    print("- 实际使用时需要确保 API 密钥支持该模型")
    print("- 部署后可以通过 /v1/models 端点查看可用模型列表")

if __name__ == "__main__":
    main()
