# 植物科学论文写作 Skill 套件

当前版本：**v0.4**

本仓库包含四个可在 Codex 中使用的技能，覆盖植物科学论文写作、综述写作和文献证据核查。建议一起安装，便于入口技能按任务自动分流；也可以单独调用具体技能。

## 当前技能

| 技能 | 用途 |
|---|---|
| `plant-article-writing` | 识别任务类型，将不明确的请求交给合适的技能。 |
| `reading-literature` | 核查科学论点与引文、精读论文或审查研究思维导图；领域知识更新和图像素材积累需另行明确提出。 |
| `plant-research-article` | 撰写或修改植物科学原创研究论文，按请求处理段落、章节或完整稿件。 |
| `plant-review-article` | 撰写或修改植物科学综述、观点文章、系统综述、范围综述及荟萃分析。 |

## 工作原则

段落或章节修改只处理所请求的内容。新建完整论文时，两套写作技能会先建立提纲与证据计划；若提纲已获批准，或作者已授权直接继续，则不重复确认。科学主张必须与证据、作物材料和实验条件相符，不虚构数据、方法或文献。

两套写作技能会围绕最有证据支持的贡献组织叙事，减少无谓的自我削弱，同时准确呈现不利结果、证据分歧和重要局限。

## 完整论文交付

请求完整论文套件时，默认在 `deliverables/` 下交付四份 Word 文件：

1. `01_plant_article_bilingual.docx`：英文论文及学术中文版本；英文部分按目标期刊要求终审。
2. `02_claim_citation_audit_bilingual.docx`：论点、数据与引文核查。
3. `03_peer_review_and_response_bilingual.docx`：同行评审、逐点回复与复核。
4. `04_journal_compliance_audit_bilingual.docx`：期刊要求、术语、格式及投稿准备状态核查。

期刊终审需要明确的目标期刊、论文类型和当前官方要求。缺少关键要求时，可以继续不依赖它的写作，但不能声称稿件已达到投稿状态。完整论文以外的任务不会自动生成四文件套件。

## 安装

在仓库根目录运行以下 PowerShell 命令：

```powershell
$skills = 'plant-article-writing','reading-literature','plant-research-article','plant-review-article'
$skills | ForEach-Object { Copy-Item -Recurse -Force ".\$_" "$env:USERPROFILE\.codex\skills\" }
```

论文套件生成脚本依赖 `python-docx`。生成 Word 文件后，仍需根据目标期刊要求修改并进行页面视觉检查。Zotero 写入需要可用的连接，以及针对相应条目或批次的用户授权。

旧版独立终审技能和高影响力文献综合指南保存在 [`legacy/`](legacy/) 中供查阅；当前两套写作技能已集成期刊终审。

新增的叙事与语气原则参考了 [anti-defensive-writing-Skill](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill)。版权说明见[第三方声明](THIRD_PARTY_NOTICES.md)。
