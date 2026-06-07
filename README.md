# AI Weekly Report Generator (AI周报生成器)

Zero dependency Python tool that generates professional weekly reports from task lists. Colored terminal output, Markdown/HTML/JSON export, smart task categorization, and history tracking.

## Features

- **Smart Categorization**: Auto-categorize tasks (开发/修复/优化/测试/文档/会议/学习/部署)
- **Flexible Input**: Interactive mode, comma-separated, or file-based
- **Markdown Output**: Professional formatted weekly report with tables
- **Customizable**: Name, date range, task descriptions all configurable

## Quick Start

### Interactive Mode
```bash
python weekly_report_generator.py --interactive
```

### Quick Mode (comma-separated tasks)
```bash
python weekly_report_generator.py -q "开发登录模块,修复搜索bug,优化查询性能,编写接口文档" -n 张三
```

### File Input Mode
Create a tasks.txt:
```
# This week tasks
开发用户认证模块|完成JWT认证
修复搜索结果排序异常
优化首页加载性能
编写API接口文档
参加技术评审会议
```

```bash
python weekly_report_generator.py -f tasks.txt -n 张三 -o report.md
```

## Sample Output

```markdown
# 周报 - 张三 - 06.02-06.06

## 一、本周工作总结
本周共完成 5 项工作。

- 开发类 2 项
- 修复类 1 项
- 优化类 1 项
- 文档类 1 项

## 二、本周工作详情
### 1. 开发用户认证模块
- 状态: 已完成 | 类型: 开发 | 耗时: 4-8h
- 描述: 完成JWT认证, 按计划完成。
- 产出: 已提交

...
```

## Command Line Options

| Option | Description |
|--------|-------------|
| -i, --interactive | Interactive input mode |
| -q, --quick | Comma-separated tasks |
| -f, --input | Read tasks from file |
| -o, --output | Output file path |
| -n, --name | Your name (default: Developer) |
| -v, --version | Show version |

## Requirements

- Python 3.7+
- No external dependencies!

## License

MIT License - Free to use and modify.

---

## Get the Pro Version (获取专业版)

This is the free open-source basic version. For advanced features:

- AI-powered report enhancement (DeepSeek API)
- Multi-format export (HTML, JSON)  
- Priority scoring and analysis
- Team report aggregation
- Week-over-week comparison
- Visualization dashboard with progress bars

Search on 闲鱼: **AI周报生成器** for the professional version!

> Keywords: AI周报生成器, 工作周报, 周报工具, Python周报

---

**If this tool helps you, please give it a Star!**
