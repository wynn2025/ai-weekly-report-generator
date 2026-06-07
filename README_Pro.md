# AI Weekly Report Generator Pro v2.0

> 一键生成专业周报，支持Git记录解析、终端彩色输出、HTML报告导出

## 特性

- **一键生成** - 输入任务列表，自动生成完整周报
- **Git集成** - 自动提取本周Git提交记录
- **终端彩色** - 分类高亮，视觉效果拉满
- **HTML导出** - 生成精美HTML报告，可分享给团队
- **智能分类** - 自动识别开发/修复/优化/测试等7大类别
- **零依赖** - Python 3.7+ 直接运行，无需安装第三方包

## 安装

```bash
git clone https://github.com/wynn2025/ai-weekly-report-generator.git
cd ai-weekly-report-generator
```

## 使用

### 快速模式
```bash
python weekly_report_pro.py -q "完成用户模块开发,优化数据库性能|进行中,修复登录bug,编写API文档" -n "张三"
```

### Git集成
```bash
python weekly_report_pro.py --git /path/to/repo --git-author "yourname" --html weekly.html
```

### 任务文件
```bash
# tasks.txt
完成用户模块
优化查询性能|进行中
修复登录bug
编写API文档

python weekly_report_pro.py -f tasks.txt -n "张三" -o report.md --html report.html
```

## 输出示例

```
# 周报 - 张三 - 06.08-06.12

## 一、本周工作总结
本周共处理 4 项工作（已完成 3, 进行中 1）：
- 开发类：2 项
- 优化类：1 项
- 修复类：1 项

## 二、已完成事项
1. **完成用户模块开发** [开发]
2. **修复登录bug** [修复]
3. **编写API文档** [开发]

## 三、进行中事项
1. **优化查询性能** - 预计下周完成

## 四、Git 提交记录
本周共提交 **12** 次：
```
  a1b2c3d feat: add user module (2026-06-08)
  e4f5g6h fix: login bug resolved (2026-06-09)
```
```

## 参数说明

| 参数 | 说明 |
|------|------|
| `-q, --quick` | 逗号分隔任务列表，`|` 指定状态 |
| `-f, --input` | 任务文件路径 |
| `-o, --output` | Markdown输出路径 |
| `--html` | HTML报告导出路径 |
| `-n, --name` | 姓名（默认 Developer）|
| `--git` | Git仓库路径 |
| `--git-author` | Git作者过滤 |
| `--no-color` | 禁用彩色输出 |

## 许可证

MIT License
