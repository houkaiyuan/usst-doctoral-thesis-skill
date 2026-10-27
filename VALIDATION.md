# v1.1.0 验证记录

验证日期：2026-10-27。新增可编辑LaTeX工程生成与编译流程；学校依据仍为2018年修订版，没有将模板版本当成规范修订年份。

## 已执行

| 检查 | 结果与范围 |
|---|---|
| Skill结构校验 | `skill-creator` 的 `quick_validate.py` 通过；技能入口及资源链接完整 |
| 生成器自动测试 | 3项通过：创建完整工程、题目特殊字符按文本转义、拒绝覆盖已有目录 |
| 空白工作模板编译 | Tectonic 0.17.0（XeTeX引擎）成功生成6页A4 PDF |
| 独立使用测试 | 从技能说明建立两章演示工程，包含图、表、公式、附录A及真实学校规范引用；编译生成10页A4 PDF |
| 引用编号 | 同一真实来源在正文引用3次，均显示方括号上标 `[1]`；文末对应1条带 `[1]` 的条目 |
| 日志核查 | 指定字体的两份工程最终无编译错误、缺字、未定义引用、Overfull/Underfull或页眉页脚尺寸警告 |
| 页面检查 | 检查空白模板全部6页及演示全部10页；核对目录页码、正文连续页码、奇偶页页眉、图下题、表上题、公式编号、附录和文献。没有强制插入的空白页或可见裁切 |
| 字体 | 指定字体测试使用本地授权的SimSun、SimHei和Times New Roman，并核对PDF字体资源；字体文件未打包 |
| 字体缺失 | 没有项目字体文件时另编译成功，使用Fandol中文字体与本机Times New Roman，日志标记 `USST-FONT-STATUS: SUBSTITUTE`。这是预览通过，不是字体合规通过 |
| 原始依据 | 官方PDF保持原始569581字节、13页；SHA-256与 `references/source.json` 一致 |
| 发布内容 | 不包含用户论文、作者信息、字体文件、登录凭据、编译缓存或机器绝对路径 |

## 可复跑的基本检查

在技能根目录运行：

```bash
python3 -m unittest discover -s tests -v
python3 scripts/init_latex.py /path/to/new-thesis --title "排版验证"
cd /path/to/new-thesis
tectonic --keep-logs main.tex
# 或在安装了XeLaTeX的机器上编译两遍：
xelatex -interaction=nonstopmode -halt-on-error main.tex
xelatex -interaction=nonstopmode -halt-on-error main.tex
```

## 验证边界

- 本次实际编译器为Tectonic；没有声称在独立XeLaTeX安装或Overleaf上完成运行测试。
- 这是模板与流程验证。摘要、个人信息、正式封面等占位不满足最终论文内容要求；不能据此判断用户论文已合规或可提交。
- Word/PDF转LaTeX由技能指导代理检查和迁移实际内容，初始化脚本只创建工程，不是全自动DOCX转换器。
- 引用重复测试覆盖1个文献键，未扩展为大量文献、各种文献类型或BibTeX/Biber测试。
- 长表续表、多行单元格、长标题、特殊数学字体、行内大公式及其他真实论文复杂版式，须逐稿检查。
- 字体缺失测试仍使用了本机Times New Roman；未声称在无任何指定字体的环境下完成端到端测试。
