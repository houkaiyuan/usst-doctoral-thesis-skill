# LaTeX生成与转换

本模式生成可编辑论文工程并编译核验。排版参数仍以[规则表](rules.md)为准；模板是工作实现，不是学校发布的官方LaTeX模板。

## 输入和文件

识别用户需要空白模板、Word/PDF转换，还是基于研究材料生成论文。保留原输入；缺少内容时使用明确占位，不假装完成论文。新工程从技能目录运行 `python3 scripts/init_latex.py <新目录> --title "题目"`；已有目录拒绝覆盖。已有LaTeX工程先识别主文件、文献系统和自定义样式，不强制重建。

正文放入 `chapters/`，图片放入 `images/`，从 `main.tex` 使用相对路径引用。包含所有编译必需的 `.tex`、`.sty`、图片和文献源后打包，不分发本机绝对路径、缓存或个人材料。

DOCX转换须检查真实段落、表格、公式、脚注和图片，保留数学含义、图表来源及注释；可恢复的公式不改成截图。PDF提取不完整时说明缺失位置。完成后比较源稿与目标稿的内容、章节、图表和引用数量。

## 样式与引用

- 模板采用 `ctexbook`、`openany`，避免强制插入空白偶数页。前置页罗马数字、正文从1开始为工作选择，见R04。
- 正文12 bp/固定20 bp、参考文献12 bp/固定16 bp；`bp` 对应Word使用的1/72英寸点。标题、图表和公式各自配置。行内公式段落、跨页续表、复杂公式和长标题需按实际内容处理。
- 默认 `cite` + `\cite{key}` 生成方括号上标，`references.tex` 中的 `\bibitem{key}` 按首次引用顺序排列。重复引用复用key；每次增加、删除或调换引文后核对正文与列表。不得将测试文献复制为用户的真实引用。
- 可以保留用户已有BibTeX/Biber系统。引入 `gbt7714` 或 `biblatex-gb7714-2015` 时核验可用版本和编译链，不将宏包默认格式称为学校最新要求。著者—出版年制与顺序编码制应全文一致。
- 模板封面、摘要、正文及文献占位仅是提示；缺少个人信息、签名或研究结果时保持待补。正式封面按已核实的博士模板替换。

## 字体和编译

优先使用宋体、黑体及Times New Roman。`fonts.tex` 支持安装字体及项目 `fonts/` 内本地授权字体，不分发字体文件。无指定字体时用Fandol/TeX Gyre Termes预览，日志输出 `USST-FONT-STATUS: SUBSTITUTE`；此时只能报告预览编译成功，不能报告符合学校字体要求。

使用已有XeLaTeX/latexmk；Codex环境可用内置编译工具或可用的latex-compile技能，其他环境不能假定存在这些工具。默认文献列表不依赖Biber。

```bash
latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex
# 没有latexmk时运行两次：
xelatex -interaction=nonstopmode -halt-on-error main.tex
xelatex -interaction=nonstopmode -halt-on-error main.tex
# Tectonic会自动处理多轮交叉引用：
tectonic --keep-logs main.tex
```

编译器或宏包缺失时保留源码并说明准确缺项，不把源码完成说成PDF完成。Tectonic缓存受限时，可按[官方文档](https://tectonic-typesetting.github.io/book/latest/getting-started/first-document.html)设置 `TECTONIC_CACHE_DIR` 指向工作区。安装完整TeX发行版须取得用户授权。

## 验收与交付

检查错误、缺字、未定义引用、目录需重跑和Overfull警告，修复后重新编译；连续修复最多三轮，剩余问题明确报告。逐页检查PDF的尺寸、字体、目录页码、奇偶页页眉、正文、图表题、公式编号、参考文献及空白页。

交付源码ZIP和经确认生成的PDF，用户只要源码时遵从其要求。报告编译器/版本、字体、页数和实际检查范围，分别列出字体替代、占位、内容待补和未检查项。空白模板的摘要占位不满足字数要求，模板验证不能扩展为任何新论文的验收。
