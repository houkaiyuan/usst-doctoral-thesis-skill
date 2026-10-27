# LaTeX 工作工程

主文件是 `main.tex`，编译器选择 **XeLaTeX**。这是依据2018年修订版规范制作的工作模板，不是学校正式封面或已通过格式审查的论文。

```bash
xelatex -interaction=nonstopmode -halt-on-error main.tex
xelatex -interaction=nonstopmode -halt-on-error main.tex
```

也可用 `latexmk -xelatex main.tex`，或 `tectonic --keep-logs main.tex`。后者首次可能下载所需宏包。默认使用内置文献列表，不依赖 Biber；正文用 `\cite{键}`，文末在 `references.tex` 中用 `\bibitem{键}`，按首次引用顺序排列。

编辑 `chapters/` 保存正文；在主文件中加入更多 `\input`。替换题目、中英文摘要和关键词占位，并按真实材料补全正式封面、声明、成果及致谢。单行表格使用 `\ussttablefont`，每行首个单元格加入 `\ussttablerow`，为该行增加上下各3 bp空间；多行单元格仍需单独检查。需要附录时使用 `\usstappendix`。

优先使用系统安装的 SimSun、SimHei、Times New Roman。也可自行将有权使用的字体放入 `fonts/`：`Simsun.ttc`、`SimHei.ttf`、`times.ttf`、`timesbd.ttf`、`timesi.ttf`、`timesbi.ttf`。本工程不附字体文件。缺少指定字体时，模板使用 Fandol/TeX Gyre Termes 预览，并在日志输出 `USST-FONT-STATUS: SUBSTITUTE`；字体替代状态不能作为符合学校字体要求的证明。

编译成功后仍须检查PDF中的目录、奇偶页页眉、页码、字号、图表、公式、参考文献对应关系及空白页。大表续表、长标题、长公式和行内公式特殊行距需按实际内容调整。不要将占位文字当作内容合规。
