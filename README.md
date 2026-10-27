# 上海理工大学博士论文 Skill

面向Codex的上海理工大学（USST）博士论文技能，支持规范问答、Word排版、LaTeX工程生成与格式审查。

依据《博士、硕士研究生学位论文写作规范（2018年修订版）》，原文件来自管理学院2026年通知附件。本项目是依据官方文档整理的工具，**不是学校发布或认证的技能，也不宣称2018版始终是最新要求**。

## 安装与使用

将完整仓库放入个人技能目录，文件夹命名为 `usst-doctoral-thesis`，使 `SKILL.md` 位于根目录：

```bash
git clone https://github.com/houkaiyuan/usst-doctoral-thesis-skill.git "${CODEX_HOME:-$HOME/.codex}/skills/usst-doctoral-thesis"
```

已有同名技能时先备份再更新，不覆盖尚未保存的修改。也可以下载ZIP后按上述结构放置。

> 使用 $usst-doctoral-thesis，检查这份博士论文的标题、图表、参考文献和页眉，并给出带依据页码的修改清单。

> 使用 $usst-doctoral-thesis，把这份Word论文整理成LaTeX工程，采用上标引用编号，交付源码ZIP和编译后的PDF。

## LaTeX工程

在仓库目录运行：

```bash
python3 scripts/init_latex.py /path/to/new-thesis --title "论文题目"
cd /path/to/new-thesis
latexmk -xelatex main.tex
```

生成器只创建新目录。编译采用XeLaTeX，也支持Tectonic。工程包含中英文摘要、目录、章节样式、奇偶页页眉、图表公式样式及上标引用；正文和个人信息按真实材料补齐。无正式博士封面时保留工作稿标识。详见[LaTeX流程](references/latex-workflow.md)。

字体优先使用SimSun、SimHei及Times New Roman；字体缺失时允许预览编译并明确提示替代状态。本仓库不附商业字体、用户论文或个人研究材料。

## 文件与依据

- [技能入口](SKILL.md)
- [27项规范规则](references/rules.md)
- [来源、歧义与版本](references/provenance.md)
- [原始规范PDF](references/official-writing-standard-2018.pdf)
- [LaTeX模板](assets/latex/main.tex)
- [本版本验证记录](VALIDATION.md)

原始规范PDF保留原始字节及来源署名，SHA-256见[source.json](references/source.json)。学校规范与本项目的技能指引、生成脚本和工作模板为不同来源材料。查询本届要求、查重/AIGC阈值、成果门槛或答辩资格时，应另查适用的官方文件。
