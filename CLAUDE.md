# CLAUDE.md — psychtest-review

## Repo 用途
hai 的「心理測驗」（高玉靜老師，1151）每週複習 PWA（手機為主）。骨架複製自 `exp-methods-review`：單頁 `index.html` ＋ runtime fetch JSON，無 build、無框架。已部署：公開 repo `github.com/Tuanzilee/psychtest-review`，Pages `tuanzilee.github.io/psychtest-review`（main 分支根目錄，2026-10-07 上線，push 後 1–2 分鐘更新）。每次 push 前一律先問 hai（公開 repo，內容不放講義或課本原文）。`samples/` 試聽檔不進 repo（.gitignore）。

## 檔案結構
```
index.html     ← 全部 UI 與邏輯（首頁、每週重點、概念卡、情境題）
concepts.json  ← 概念卡
quiz.json      ← 情境題（4 選 1，附解析）
weeks.json     ← 每週重點摘要與待辦
sw.js / manifest.json / icon-*.png（圖示是米色底加單一漢字：心理測驗用「測」、實驗法用「驗」；LINE 預覽用 index.html 的 og:image 抓 icon-512.png，換圖示後 LINE 可能要一段時間才更新快取）
tools/gen_audio.py ← 產生音檔（雲哲男聲 zh-TW-YunJheNeural）：`~/.venvs/tts/bin/python tools/gen_audio.py`
audio/         ← {概念卡id}.mp3、{題目id}.mp3、W{週}.mp3
check.py       ← 資料檢查（含音檔齊全）：python3 check.py
```
預覽：母資料夾 `.claude/launch.json` 的 `psychtest-review`，埠 8767。

## 資料 schema（與實驗法相同，id 前綴改 P）
- `concepts.json`：`id`（P_W{週}_C{兩位數}，不要改既有 id，進度綁 id）、`week`、`topic`、`term`、`en`、`def`、`example`、`tags`
- `quiz.json`：`id`（P_W{週}_Q{兩位數}）、`week`、`q`、`options`（4 個）、`answer`、`why`、`concept`
- `weeks.json`：`week`、`date`、`title`、`summary`、`points[]`、`todo[]`、`concepts[]`
- **範圍篩選**：「週次」由 `weeks.json` 自動產生；「主題」由 `concepts.json` 的 `topic` 欄位自動產生（所以 topic 名稱要一致，新增卡片優先沿用既有主題）。目前主題：測驗基本概念、測量理論、測驗與評估、測驗類型與方法、倫理與公平、構念與操作化、智力理論、智力測量、興趣與人格
- `index.html` 的 `MID_WEEK = 8`（期中範圍到決策效度，見下方「週次編號」）

## 週次編號
週次＝學期第幾週，與 Plaud 檔名 W{nn} 一致。W1＝9/18；W2＝9/25 中秋放假週（放 10/1 的補充教材，自學）；W3＝10/2；W4＝10/9 國慶放假；W5＝10/16 量尺轉換與常模；W6＝10/23 信度；W7＝10/30 信度 II 與測量效度；W8＝11/6 決策效度；W9＝11/13 試題分析（第一個作業）；W10＝11/20 期中考。
**期中範圍：到決策效度（W8）**（hai 確認 2026-10-07）。`index.html` 的 `MID_WEEK = 8`；試題分析（W9）不在期中範圍。

## 題型
概念選擇題為主，另有簡單計算（比率 IQ）與分類辨認（Holland 六型、智力理論是誰提的、測量方法匹配）。信度類型、效度證據分類、CTT 公式、IRT 等還沒上，上到再加。

## 介面風格
同實驗法：暖米色底、深棕字、大圓角、單一主行動首頁、浮動線條圖示導覽列。

## 每週新增內容（hai 說「更新心理測驗 W{n}」）
1. 讀 `~/Desktop/P. 進行中專案/FJU psy/02_修課/1151/1151_心理測驗/` 當週的 `*_W{nn}_Plaud逐字稿.md`（摘要區已分好知識點）與講義 PDF；有考前整理的 docx 優先讀
2. **Plaud 轉錄未經核聽**：專有名詞、數字以講義與課本（Kaplan & Saccuzzo，在 `_課本/`）校正；講義 `20260918_心理測驗w1導論.pdf` 是圖片檔沒有文字層，需要時另外看圖；不確定處列給 hai 確認
3. 以「一張卡一個概念」追加 concepts.json；情境題用課堂案例改寫；更新 weeks.json
4. **用自己的話改寫，不要貼講義或課本原文**
5. 跑 `~/.venvs/tts/bin/python tools/gen_audio.py` 補音檔，再跑 `python3 check.py`；bump `sw.js` 的 `CACHE` 版本號
6. 本機預覽驗證後 commit；**push 前一律先問 hai**

## 查證紀錄（2026-10-07）
- **Guilford 180 種**：完整版 6 操作（認知、記憶記錄、記憶保存、發散產生、聚斂產生、評價）× 5 內容（視覺、聽覺、符號、語意、行為）× 6 產物（單位、類別、關係、系統、轉換、涵義）＝180；早期 120 → 150 → 180。講義列的是簡化版（5 操作、4 內容、6 產物）。來源：網路搜尋整理的二手資料（維基百科、教學網站），尚未對照 Guilford 原著
- **托福適性測驗**：ETS／富布萊特韓國辦公室公告，TOEFL iBT 自 2026 年 1 月起閱讀、聽力為多階段適性（中途依表現調整難度），不是每題即時調整。IRT 與電腦適性測驗的關係，課本 Kaplan & Saccuzzo 第 6 章有寫
- **「測驗」與「量表」**：W1 講義（OCR 讀出）p.9 說，『測驗』一詞只用在反應依正確性或品質評分的程序，不計對錯的叫量表、問卷、調查、檢核表、評定表、投射技術；p.18 另有 scale（同一變項依難度或強度排序的一組題目）與 scaling 的心理計量用法。兩個用法都有，Plaud 摘要的說法與講義 p.9 一致
- **歷史人物**：Galton、J. M. Cattell（1890 提出 mental test）、Goddard（1908 翻譯 Binet–Simon）、Terman（1916 Stanford–Binet）、Army Alpha／Beta，課本 Kaplan & Saccuzzo 第 1–2 章有對應。顱相學、劍橋分析、高達德的移民篩選與優生學細節，是補充教材與課堂提到的名詞，卡片只寫課堂層級
- **W1 講義**：`20260918_心理測驗w1導論.pdf` 是圖片檔，用 macOS Vision 做 OCR（腳本在工作暫存區，沒進 repo），30 頁都讀得出來，內容已用來校正 W1 的卡片

## 待確認
- 佛瑞實驗 4.3 分來自雜誌文章《未來少年》2024.08，未回頭查原始研究（Forer 1949）
- 托福以外的 Plaud 摘要細節（例如各理論的細節）以講義為準；Plaud 轉錄未經核聽
- 尚未用 Consensus 逐條查證心理學主張；上完信度、效度後再補
