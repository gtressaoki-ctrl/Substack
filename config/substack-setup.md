# Substack 開設シート（コピペ用）

作成：2026-10-08　／　媒体名・ペンネームは編集長の指示に基づく。価格は承認待ちの案。

---

## 1. 開設前に用意するもの（身バレ防止）

- [ ] **新しいメールアドレス**（例：Gmailで `japanhandover.steve@…` など）。本名・勤務先と紐づかないもの
- [ ] そのメールで Substack アカウントを作る（既存のSubstack/Google/Appleアカウントでのログインはしない）
- [ ] Stripe接続時、受取人の氏名は本名（法的に必要）。**明細書表記（statement descriptor）は媒体名「JAPAN HANDOVER」に設定**し、読者のカード明細に本名が出ないようにする [要確認：Stripe Expressでの設定画面]

---

## 2. 媒体（Publication）の設定

| 項目 | 入力する内容 |
|---|---|
| Publication name | **The Japan Handover** |
| Subdomain（リンク） | **japanhandover** → `https://japanhandover.substack.com` |
| Short description | Japan's small-business succession market, read from Japanese sources — the numbers, rules and sector signals foreign buyers need. Weekly. |
| Logo（正方形） | `assets/branding/logo-1024.png` |
| Wordmark（ヘッダー用・任意） | `assets/branding/wordmark-navy.png` |
| Cover / Social preview image | `assets/branding/cover-1200x630.png` |
| Language | English |
| Category | Business（なければ Finance） |
| Theme color（任意） | Navy `#14213D` / Accent `#D6402F` |
| About ページ | `config/launch-kit.md` §3 の EN をそのまま貼る（`[媒体名]` は The Japan Handover に置換済みの扱い） |
| Welcome email | `config/launch-kit.md` §4 の EN（`[曜日]` は配信曜日を決めて置換） |

**サブドメインの空き状況**：2026-10-08 に `japanhandover.substack.com` / `thejapanhandover.substack.com` を確認し、いずれも未使用（HTTP 404）。取られていた場合の予備は `thejapanhandover`。

---

## 3. 書き手（Profile）の設定

| 項目 | 入力する内容 |
|---|---|
| Name | **Steve** |
| Handle | **@japanhandover**（取られていれば @steve.japanhandover など） |
| Profile photo | `assets/branding/author-steve-1024.png`（顔写真は使わない） |
| Bio（短） | Writing The Japan Handover: Japan's small-business succession market, read from Japanese sources. Pen name. Based in Japan. |

※ X・LinkedIn も同じ名前・画像・Bioでそろえる（本名のアカウントとはつながない）。

---

## 4. 課金・Pledges の設定

| 項目 | 設定 |
|---|---|
| Pledges | **初日からON**（README §Phase 1） |
| 有料化 | まだONにしない。無料100人 または Pledges 5件 の早い方で有料化（README §4） |
| 価格（Pledges に表示される予定価格） | 月 **$25** ／ 年 **$250** ／ Founding Member **$500**（**承認待ちの案**） |

---

## 5. 開設後に教えてほしいこと

- 実際のURL（サブドメインが取れたか）
- 配信曜日（Welcome メールの `[曜日]` に入れる）
- 開設日（`metrics/metrics.csv` の起点にする）
