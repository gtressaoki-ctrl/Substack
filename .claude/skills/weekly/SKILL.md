---
name: weekly
description: Phase 2の週次ループ。sources.yaml巡回→signals記録→上位3件選定→編集長への質問で停止→（回答後）outline/draft/factcheck/final/promo を作成し公開前チェックリストで停止。「weekly」「今週の号」で使う。
---
README.md の「Phase 2」に厳密に従う。

前半（1回目の呼び出し）
1. `config/sources.yaml` を巡回し候補10件を `signals/YYYY-Www.md`（ISO週）に記録：日本語要約・出典URL・日付。
2. `config/persona.md` の読者にとっての so what で採点し上位3件と選定理由。
3. 3件について現場感・見解を引き出す質問を3つ出して **停止**。

後半（回答を受けて）— `issues/YYYY-MM-DD-slug/` に作成
4. `outline.md`：冒頭2文で今週の一番大事なことを言い切る
5. `draft.md`：600〜900 words、背景を1〜2文で補う。要約＋出典＋独自解釈（全文翻訳禁止）
6. `factcheck.md`：全数字・固有名詞・主張 ↔ 出典URL表。未確認は一覧化、本文に `[要確認]`
7. 英語編集パス：和製英語・直訳調・冗長を修正。タイトル5案・サブタイトル3案
8. `final.md`：Substackに貼れる形。末尾に有料版への自然な導線1つ
9. `promo.md`：Notes 5本・LinkedIn 2本・X 3本（各々単独で価値がある切り口）
10. 公開前チェックリストを表示して **停止**（非公開情報なし／出典あり／独自価値1つ以上／煽りなし／要確認ゼロ or 明示）。
`config/voice.md` に従う。
