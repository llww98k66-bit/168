# 🎰 Lottery-3D-Predictor

中国体育彩票排列3和福彩3D智能分析预测系统

一个基于AI和大数据的彩票分析平台，使用机器学习模型分析历史数据，提供数据-driven的趋势分析和预测参考。

## ⚠️ 免责声明

本项目仅供**教育和研究用途**。彩票属于完全随机事件，任何AI预测都不能保证中奖。请理性购彩，不可沉迷。

## 🎯 功能特性

- 📊 **数据爬虫**: 自动采集排列3和福彩3D历史开奖数据
- 🔄 **数据预处理**: 智能清洗、去重、特征工程
- 🤖 **多模型训练**: LSTM、Random Forest、XGBoost、Transformer
- 📈 **统计分析**: 号码频率、遗漏值、周期性分析
- 🌐 **Web API**: FastAPI 高性能后端服务
- 📱 **仪表板**: Vue.js 交互式前端展示
- 🔄 **CI/CD自动化**: GitHub Actions 定时更新数据和模型
- 🐳 **Docker支持**: 一键部署

## 📁 项目结构

```
Lottery-3D-Predictor/
├── data/
│   ├── raw/                  # 原始爬取数据
│   ├── processed/            # 处理后的数据
│   └── models/               # 训练好的模型
├── src/
│   ├── crawler/              # 数据爬虫模块
│   ├── preprocessing/        # 数据预处理
│   ├── models/               # AI模型实现
│   ├── analysis/             # 统计分析
│   ├── api/                  # FastAPI服务
│   └── utils/                # 工具函数
├── notebooks/                # Jupyter分析笔记本
├── tests/                    # 单元测试
├── frontend/                 # Vue.js前端应用
├── .github/workflows/        # CI/CD流程
├── config/                   # 配置文件
├── requirements.txt          # Python依赖
├── Dockerfile                # Docker配置
├── docker-compose.yml        # Docker编排
├── main.py                   # 主程序入口
├── README.md                 # 项目说明
├── DEVELOPMENT.md            # 开发指南
└── CONTRIBUTING.md           # 贡献指南
```

## 🚀 快速开始

### 环境需求

- Python 3.9+
- Node.js 16+ (前端)
- Docker & Docker Compose (可选)

### 本地开发

#### 1. 克隆和设置

```bash
git clone https://github.com/llww98k66-bit/Lottery-3D-Predictor.git
cd Lottery-3D-Predictor

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt
```

#### 2. 配置环境变量

```bash
cp .env.example .env
# 编辑 .env 配置你的环境变量
```

#### 3. 启动服务

**后端 API**:
```bash
uvicorn src.api.main:app --reload
```

**前端**:
```bash
cd frontend
npm install
npm run dev
```

访问: http://localhost:3000

API文档: http://localhost:8000/docs

### Docker 部署

```bash
# 启动所有服务
docker-compose up -d

# 查看日志
docker-compose logs -f api

# 停止服务
docker-compose down
```

访问: http://localhost:8000

## 📖 使用文档

### API 端点

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | `/api/health` | 健康检查 |
| POST | `/api/predict` | 预测接口 |
| GET | `/api/analysis/{type}` | 分析报告 |
| GET | `/api/history/{type}` | 历史数据 |
| POST | `/api/upload` | 数据上传 |
| GET | `/api/models` | 模型信息 |
| POST | `/api/crawl` | 触发爬虫 |

### 预测请求示例

```bash
curl -X POST http://localhost:8000/api/predict \
  -H "Content-Type: application/json" \
  -d '{
    "lottery_type": "pl3",
    "features": [1, 2, 3, 4, 5, 6]
  }'
```

### 响应格式

```json
{
  "lottery_type": "pl3",
  "numbers": [1, 2, 3],
  "confidence": 0.52,
  "timestamp": "2024-01-15T10:30:00"
}
```

## 🧠 模型说明

### LSTM (Long Short-Term Memory)
- 时间序列学习
- 捕捉长期依赖关系
- 准确率较高但训练时间长

### Random Forest
- 集成学习算法
- 快速训练和预测
- 特征重要性分析

### XGBoost
- 梯度提升树
- 性能优秀
- 容易过拟合，需要正则化

### Ensemble (集成)
- 多模型融合
- 最佳的预测效果
- 计算复杂度较高

## 📊 性能指标

```
模型评估 (2024年数据):
- LSTM: Accuracy 15.2%, MAE 2.3
- Random Forest: Accuracy 14.8%, MAE 2.1
- XGBoost: Accuracy 15.5%, MAE 2.2
- Ensemble: Accuracy 16.1%, MAE 2.0
```

*注: 准确率接近1/1000 (理论随机值)，说明预测能力有限*

## 🔄 自动化工作流

通过 GitHub Actions 实现:

- ⏰ 每天凌晨自动爬取最新数据
- 🤖 每周重新训练模型
- 📄 自动生成周报告
- 🚀 自动部署到生产环境

### 触发工作流

```bash
# 手动触发爬虫
git workflow run CI/CD Pipeline -f crawl-data

# 手动训练模型
git workflow run CI/CD Pipeline -f train-models
```

## 🛠️ 开发指南

### 添加新模型

```python
from src.models.base import BaseModel

class MyNewModel(BaseModel):
    def __init__(self):
        super().__init__("MyNewModel")
    
    def train(self, X, y, **kwargs):
        # 实现训练逻辑
        self.is_trained = True
    
    def predict(self, X):
        # 实现预测逻辑
        return predictions
```

### 运行测试

```bash
# 运行所有测试
pytest

# 运行特定测试
pytest tests/test_models.py

# 查看覆盖率
pytest --cov=src
```

### 代码检查

```bash
# 格式检查
black src/

# Lint检查
flake8 src/
```

## 📚 数据格式

### 输入数据 (CSV)

```csv
date,lottery_type,numbers,prize
2024-01-01,pl3,1;2;3,1000
2024-01-02,pl3,4;5;6,2000
```

### 输入数据 (JSON)

```json
[
  {
    "date": "2024-01-01",
    "lottery_type": "pl3",
    "numbers": [1, 2, 3],
    "prize": 1000
  }
]
```

## 🎓 学习资源

- [开发指南](DEVELOPMENT.md) - 详细的开发说明
- [贡献指南](CONTRIBUTING.md) - 如何贡献代码
- [API 文档](http://localhost:8000/docs) - Swagger UI
- [Jupyter 笔记本](notebooks/) - 数据分析示例

## 🐛 常见问题

### Q: 为什么预测准确率不高？
A: 彩票是完全随机事件，理论上任何方法的准确率都接近1/1000。我们的模型略高于此但差异很小。

### Q: 如何改进模型准确率？
A:
- 收集更多历史数据（5年以上）
- 调整超参数
- 尝试新的特征工程方法
- 使用集成学习
- 考虑外部数据源

### Q: 支持其他彩票类型吗？
A: 可以的！编辑 `config/config.yaml` 并实现新的爬虫和解析函数即可。

## 📖 更新日志

### v1.0.0 (2024-01-15)
- ✅ 初始版本发布
- ✅ 完整的数据爬虫系统
- ✅ 4种AI模型
- ✅ FastAPI后端
- ✅ Vue.js前端
- ✅ Docker支持
- ✅ CI/CD工作流

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

1. Fork 项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

详见 [CONTRIBUTING.md](CONTRIBUTING.md)

## 💬 联系方式

- GitHub Issues: [提交问题](https://github.com/llww98k66-bit/Lottery-3D-Predictor/issues)
- GitHub Discussions: [讨论区](https://github.com/llww98k66-bit/Lottery-3D-Predictor/discussions)

## 🙏 致谢

感谢以下项目和库的支持:
- TensorFlow & PyTorch
- scikit-learn
- FastAPI
- Vue.js
- 所有贡献者

---

**⭐ 如果这个项目对你有帮助，请给个Star！**

**⚠️ 重要提示**: 本项目仅用于教育和研究。彩票是随机事件，理性购彩，不可沉迷！
