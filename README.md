# ODM Quality Guard

**基于流式处理的日志分析引擎 (Stream-based Log Analyzer)**

> 此组件是 [ODM Distributed Test System](https://github.com/your-infra-repo) 的分析单元。

## 1. 设计理念 (Design Philosophy)
不同于传统的 grep 脚本，本模块采用**代码即配置 (Configuration as Code)** 的思路，将日志分析逻辑封装为可测试、可扩展的 Python 对象。

## 2. 核心技术栈
* **Python 3.10**: 类型提示 (Type Hints) 支持。
* **Pytest**: 用于驱动测试规则执行。
* **Allure**: 生成可视化的质量门禁报告。

## 3. 架构亮点 (Architecture Highlights)

### 3.1 内存安全的日志加载 (Memory Safety)
针对 ODM 场景下可能出现的 GB 级 Logcat 文件，底层 `FileLoader` 放弃了 `readlines()`，转而使用 Python **生成器 (Generator)** 模式 (`yield`) 实现流式读取。这确保了无论日志多大，内存占用始终保持在 O(1) 级别。

### 3.2 规则引擎解耦
日志解析逻辑与测试断言分离。`LogParser` 类支持注入自定义规则集 (Rules List)，目前内置了 CRITICAL (Crash) 和 HIGH (Memory Leak) 等级别的检测模式。

## 4. 扩展指南
新增一条过滤规则只需在 `core/parse.py` 中添加字典配置，无需修改核心循环逻辑：

```python
{
    "pattern": "ANR Input dispatching timed out",
    "level": "CRITICAL",
    "category": "Performance"
}