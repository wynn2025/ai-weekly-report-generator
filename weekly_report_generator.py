# -*- coding: utf-8 -*-
"""AI Weekly Report Generator v1.0"""
import sys, argparse
from datetime import datetime, timedelta
from pathlib import Path
VERSION = "1.0.0"

def get_week_range():
    today = datetime.now()
    monday = today - timedelta(days=today.weekday())
    friday = monday + timedelta(days=4)
    return monday.strftime("%m.%d") + "-" + friday.strftime("%m.%d")

def categorize_task(text):
    for cat, kws in [("开发",["开发","实现","编写","新增","重构"]),
                      ("修复",["修复","bug","异常","报错","崩溃"]),
                      ("优化",["优化","性能","提升","改进"]),
                      ("测试",["测试","验证","联调"]),
                      ("文档",["文档","README","接口文档"]),
                      ("会议",["会议","评审","讨论","站会"]),
                      ("学习",["学习","调研","研究"]),
                      ("部署",["部署","上线","发布","监控"])]:
        for kw in kws:
            if kw in text.lower(): return cat
    return "其他"

def estimate_hours(text):
    t = text.lower()
    if any(w in t for w in ["重构","架构","设计"]): return "8-16"
    if any(w in t for w in ["开发","实现","新增"]): return "4-8"
    if any(w in t for w in ["修复","bug","优化"]): return "1-4"
    if any(w in t for w in ["会议","评审"]): return "1-2"
    return "2-4"

def make_task(title):
    return {"title":title,"category":categorize_task(title),
            "hours":estimate_hours(title),"status":"已完成",
            "description":title+",按计划完成。","deliverable":"已提交"}

def parse_quick(text):
    return [make_task(s.strip()) for s in text.split(",") if s.strip()]

def gen_report(name, tasks, out=None):
    NL = chr(10)
    parts = ["# 周报 - %s - %s" % (name, get_week_range()), ""]
    # Summary
    parts.append("## 一、本周工作总结")
    if tasks:
        parts.append("本周共完成 %d 项工作:" % len(tasks))
        cc = {}
        for t in tasks: cc[t["category"]] = cc.get(t["category"],0)+1
        for c,n in sorted(cc.items(), key=lambda x:-x[1]):
            parts.append("- %s类 %d 项" % (c,n))
    else:
        parts.append("本周按计划推进各项工作。")
    parts.append("")
    # Detail
    parts.append("## 二、本周工作详情")
    for i,t in enumerate(tasks,1):
        parts.append("### %d. %s" % (i,t["title"]))
        parts.append("- 状态: %s | 类型: %s | 耗时: %sh" % (t["status"],t["category"],t["hours"]))
        parts.append("- 描述: %s" % t["description"])
        parts.append("- 产出: %s" % t["deliverable"])
        parts.append("")
    parts.append("")
    # Problems
    parts.append("## 三、遇到的问题与解决方案")
    probs = []
    for t in tasks:
        if t["category"] == "修复":
            probs.append("### " + t["title"] + NL + "- 影响: 功能使用" + NL + "- 方案: 定位根因并修复" + NL + "- 状态: 已解决")
        elif t["category"] == "优化":
            probs.append("### " + t["title"] + NL + "- 影响: 性能体验" + NL + "- 方案: 分析瓶颈优化" + NL + "- 状态: 已优化")
    parts.append(NL.join(probs) if probs else "本周工作顺利,无重大阻塞。")
    parts.append("")
    # Plan
    parts.append("## 四、下周工作计划")
    plans = []
    for t in tasks:
        if t["category"] in ["开发","优化"]: plans.append("- 继续推进%s后续工作" % t["title"])
        elif t["category"] == "修复": plans.append("- 关注%s相关稳定性" % t["title"])
    if not plans: plans = ["- 推进下周既定开发任务","- 持续优化现有功能","- 技术学习"]
    parts.extend(plans[:5])
    parts.append("")
    # Learning
    parts.append("## 五、学习与成长")
    items = []
    for t in tasks:
        c = t["category"]
        if c == "开发": items.append("- 通过%s,深入理解技术方案" % t["title"])
        elif c == "优化": items.append("- 在%s中积累了优化经验" % t["title"])
        elif c == "修复": items.append("- 排查%s,提升debug能力" % t["title"])
    if not items: items = ["- 持续学习,保持技术敏感度"]
    parts.extend(items[:3])
    parts.extend(["","---","*生成时间: %s | AI周报生成器 v%s*" % (datetime.now().strftime("%Y-%m-%d %H:%M"),VERSION)])
    report = NL.join(parts)
    if out:
        p = Path(out); p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(report, encoding="utf-8")
        print("[OK] Saved:", p)
    return report

def interactive():
    print("="*45)
    print("  AI Weekly Report Generator v"+VERSION)
    print("="*45)
    name = input("Name: ").strip() or "Developer"
    print("Enter tasks (done to finish):")
    tasks, idx = [], 1
    while True:
        t = input("  Task %d (or done): " % idx).strip()
        if t.lower() in ["done","q"]: break
        if t: tasks.append(make_task(t)); idx += 1
    report = gen_report(name, tasks)
    print(report)
    s = input("Save? (filename/n): ").strip()
    if s and s.lower() not in ["n","no"]:
        fn = s if s.endswith(".md") else "report_%s.md" % datetime.now().strftime("%Y%m%d")
        Path(fn).write_text(report, encoding="utf-8")
        print("[OK] Saved:", fn)

def main():
    p = argparse.ArgumentParser(description="AI Weekly Report Generator")
    p.add_argument("-i","--interactive",action="store_true")
    p.add_argument("-q","--quick",type=str)
    p.add_argument("-f","--input",type=str)
    p.add_argument("-o","--output",type=str)
    p.add_argument("-n","--name",default="Developer")
    a = p.parse_args()
    if a.interactive: interactive(); return
    tasks = []
    if a.quick: tasks = parse_quick(a.quick)
    elif a.input:
        if not Path(a.input).exists(): print("[ERROR] Not found:",a.input); sys.exit(1)
        for line in Path(a.input).read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#"): tasks.append(make_task(line))
    else: interactive(); return
    report = gen_report(a.name, tasks, a.output)
    if not a.output: print(report)

if __name__ == "__main__": main()
