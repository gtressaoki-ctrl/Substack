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

---

## 6. 設定結果（2026-10-10、Claude in Chrome による作業の報告）

| 項目 | 結果 |
|---|---|
| 媒体名・サブドメイン・紹介文・言語・カテゴリ | 設定済み（Business） |
| ロゴ・ワードマーク・アクセント色 #D6402F | 設定済み。ワードマークは縦横比の制限（21:4）に合わせて上下に透明余白を追加 |
| カバー画像 | Website editor の Welcome page の Image 欄に設定（ソーシャルプレビュー専用欄は見つからず） |
| 背景色 | 白のまま（紺にはしない方針） |
| プロフィール（Steve、@japanhandover、Bio、写真） | 設定済み |
| About・Welcome email | 設定済み。配信曜日は火曜。"paid subscribers get" → "will get" への修正が必要（編集長が手で修正） |
| Pledges | ON。月$25／年$250／Founding $500 |
| Paid subscriptions・Stripe | 未接続（有料化の条件に達するまで触らない） |

**残っている対応（編集長）**
- Substack上の、拡張機能が独自に作った下書き「Issue #1 — The pool is shrinking…」を削除する（ファクトチェック未了のため。第1号は `issues/2026-10-08-successor-crunch/final.md` を使う）
- 返信先（Reply-to）とメールの送信者名が本名・個人Gmailの表示名になっていないか確認する（アカウントは個人Gmailのまま運用、編集長判断）
- 2段階認証を有効にする
- X・LinkedIn の名前・画像・Bio をそろえる
