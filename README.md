# PDF2MD (`pdf2md.fun` / `pdf2fun`) — Convert PDF to Clean Markdown for AI

[![Online Web Tool](https://img.shields.io/badge/Live_Web_App-pdf2md.fun-0f766e?style=for-the-badge)](https://pdf2md.fun)
[![Markdown to PDF](https://img.shields.io/badge/Reverse-Markdown_to_PDF-115e59?style=for-the-badge)](https://pdf2md.fun/markdown-to-pdf-online)

**[PDF2MD (https://pdf2md.fun)](https://pdf2md.fun)** (also searched as **`pdf2md`** or **`pdf2fun`**) is a fast, privacy-first online converter that turns PDF documents into clean, structured **Markdown (`.md`)** with headings (`#`, `##`, `###`), bullet lists, and paragraphs preserved — ready to paste straight into **ChatGPT**, **Claude**, **Obsidian**, **Notion**, or **RAG / LLM pipelines**.

👉 **Try it in your browser (No sign-up required):** **[https://pdf2md.fun](https://pdf2md.fun)**

---

## ✨ Why [PDF2MD (pdf2md.fun)](https://pdf2md.fun)?

When you copy and paste directly from a PDF into ChatGPT, Claude, or a Markdown note app:
1. **Line breaks shatter mid-sentence** and hyphenated words break apart.
2. **Heading hierarchy disappears**, so LLMs cannot distinguish section titles from body text.
3. **Context window tokens are wasted** on noisy layout artifacts.

**[PDF2MD (`pdf2md.fun`)](https://pdf2md.fun)** reconstructs `# H1 / H2 / H3` headings and clean paragraph flow from font geometry, producing compact `.md` output that AI models and note apps understand natively.

---

## 🚀 Dedicated Workflows & Use Cases

| Use Case | Direct Tool Link | Description |
| :--- | :--- | :--- |
| **PDF2MD / pdf2fun Online** | **[pdf2md.fun/pdf2md](https://pdf2md.fun/pdf2md)** | Fast browser-based **PDF ⇄ Markdown** converter with 1 free trial and no account required. |
| **PDF to Markdown for ChatGPT** | **[pdf2md.fun/pdf-to-markdown-chatgpt](https://pdf2md.fun/pdf-to-markdown-chatgpt)** | Turn long PDFs into clean, token-efficient Markdown prompts for **ChatGPT & GPT-4o**. |
| **PDF to Markdown for Claude** | **[pdf2md.fun/pdf-to-markdown-claude](https://pdf2md.fun/pdf-to-markdown-claude)** | Convert heavy PDFs into lightweight `.md` files for **Claude Projects** & knowledge bases. |
| **PDF to Obsidian & Notion** | **[pdf2md.fun/pdf-to-obsidian-markdown](https://pdf2md.fun/pdf-to-obsidian-markdown)** | Import PDF books, handouts, and docs into **Obsidian Vaults**, **Notion**, or **Logseq**. |
| **Academic Paper PDF → MD** | **[pdf2md.fun/academic-pdf-to-markdown](https://pdf2md.fun/academic-pdf-to-markdown)** | Extract structured sections from **arXiv papers**, literature reviews, and technical reports. |
| **Markdown to PDF (`MD → PDF`)** | **[pdf2md.fun/markdown-to-pdf-online](https://pdf2md.fun/markdown-to-pdf-online)** | Paste Markdown notes or AI output and export a clean, printable **PDF** (with CJK & table support). |
| **PDF to Markdown for RAG / LLM** | **[pdf2md.fun/pdf-to-markdown-rag-llm](https://pdf2md.fun/pdf-to-markdown-rag-llm)** | Prepare heading-structured `.md` chunks for **Dify**, **LangChain**, **LlamaIndex**, and **FastGPT**. |

---

## 💻 Quick CLI Usage (`pdf2md_cli.py`)

This repository also includes a lightweight Python CLI wrapper (`pdf2md_cli.py`) that converts local PDF files to Markdown or renders Markdown to PDF via **[https://pdf2md.fun](https://pdf2md.fun)**:

```bash
# Convert a local PDF file to Markdown (.md)
python3 pdf2md_cli.py pdf2md sample.pdf -o sample.md

# Convert a local Markdown (.md) file to PDF
python3 pdf2md_cli.py md2pdf notes.md -o notes.pdf
```

---

## 🇨🇳 中文介绍：PDF2MD (`pdf2md.fun` / `pdf2fun`) 在线 PDF ⇄ Markdown 转换器

**[PDF2MD (https://pdf2md.fun/?lang=zh)](https://pdf2md.fun/?lang=zh)** 是一款极简、无需注册的在线 **PDF 转 Markdown (`PDF → MD`)** 与 **Markdown 转 PDF (`MD → PDF`)** 双向转换工具：

- **保留结构**：按字号与版面自动识别并重建 `#` / `##` / `###` 标题层级、列表与段落。
- **即刻可用**：打开 **[https://pdf2md.fun](https://pdf2md.fun)** 即可免费体验，转换完成后临时文件立即销毁，绝不留存文档。
- **热门场景直达**：
  - [PDF2MD 在线转换 (pdf2md / pdf2fun)](https://pdf2md.fun/pdf2md?lang=zh)
  - [PDF 转 ChatGPT 提示词格式](https://pdf2md.fun/pdf-to-markdown-chatgpt?lang=zh)
  - [PDF 转 Claude Projects 知识库](https://pdf2md.fun/pdf-to-markdown-claude?lang=zh)
  - [PDF 转 Obsidian / Notion 笔记 (.md)](https://pdf2md.fun/pdf-to-obsidian-markdown?lang=zh)
  - [学术论文与文献 PDF 转 Markdown](https://pdf2md.fun/academic-pdf-to-markdown?lang=zh)
  - [Markdown 在线转 PDF（支持中文排版与表格）](https://pdf2md.fun/markdown-to-pdf-online?lang=zh)
  - [RAG 知识库（Dify / FastGPT / LangChain）PDF 清洗](https://pdf2md.fun/pdf-to-markdown-rag-llm?lang=zh)

---

## 🇯🇵 日本語：PDF2MD (`pdf2md.fun`) — AI 向け PDF ⇄ Markdown オンライン変換

**[PDF2MD (https://pdf2md.fun/?lang=ja)](https://pdf2md.fun/?lang=ja)** は、PDF 文書を見出し構造（`#` / `##`）や箇条書きを保ったままクリーンな **Markdown (`.md`)** に変換するウェブツールです。

- [PDF2MD オンライン変換](https://pdf2md.fun/pdf2md?lang=ja)
- [ChatGPT 向け PDF Markdown 変換](https://pdf2md.fun/pdf-to-markdown-chatgpt?lang=ja)
- [Claude Projects 向け PDF Markdown 変換](https://pdf2md.fun/pdf-to-markdown-claude?lang=ja)
- [PDF を Obsidian・Notion 用 Markdown に変換](https://pdf2md.fun/pdf-to-obsidian-markdown?lang=ja)
- [Markdown から PDF へ変換（日本語対応）](https://pdf2md.fun/markdown-to-pdf-online?lang=ja)

---

## 📄 License

MIT License · Web Service: **[https://pdf2md.fun](https://pdf2md.fun)**
