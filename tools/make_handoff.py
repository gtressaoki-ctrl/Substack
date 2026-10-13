#!/usr/bin/env python3
"""final.md から、Claude in Chrome に貼る「下書き作成」指示文を生成する。

使い方:
  python3 tools/make_handoff.py issues/<dir> [--social images/social.png] [--table-images a.png,b.png]

- final.md 先頭の <!-- ... --> は編集メモとして除外する。
- 1行目の "# " をタイトル、次の "*...*" 行をサブタイトルとして使う。
- Markdown の表は、--table-images で渡した画像に出現順で置き換える（足りなければ止める）。
- <!-- PAYWALL --> は「ここに有料の区切り（Paywall）を入れる」指示に置き換える。
- 【編集長コメント待ち】が残っていたら生成しない（未完成の原稿を出さない）。
出力: <dir>/chrome-handoff.md
"""
import argparse
import pathlib
import re
import sys

RULES = """【守ってほしいこと】
- 記事の「公開（Publish）」「予約（Schedule）」「メール送信」は絶対にしない。下書き保存まで。公開は私が自分でボタンを押す。
- 本文は下に書いた英文をそのまま使い、言い回しを変えない・足さない。
- 画像のアップロード欄に来たら、どの位置にどの画像を入れるかを私に伝えて止まる（ファイルは私が選ぶ）。
- メールアドレス・パスワード・Stripe・本人確認には触らない。何も削除しない。
- 画面が想定と違う場合は、探し回らずに見えているものを報告して止まる。"""

FORMAT = """  - 「## 」で始まる行は見出し（Heading 2）にする。
  - **〜** は太字、*〜* は斜体にする。
  - [テキスト](URL) はリンクにする。
  - 「- 」「1. 」で始まる行は箇条書き・番号付きリストにする。
  - 「[画像を挿入：ファイル名]」の行は、その位置に画像を入れる（私がファイルを選ぶ）。
  - 「[ここに Paywall を入れる]」の行は、Substack の有料区切り（Paywall）を入れる。ただし有料購読がまだONでなければ入れずに報告する。
  - 「---」の行は区切り線にする。"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("issue_dir")
    ap.add_argument("--social", default="")
    ap.add_argument("--table-images", default="")
    a = ap.parse_args()

    d = pathlib.Path(a.issue_dir)
    src = (d / "final.md").read_text(encoding="utf-8")
    if "【編集長コメント待ち" in src:
        sys.exit("final.md に【編集長コメント待ち】が残っています。埋めてから実行してください。")
    if "[要確認" in src:
        sys.exit("final.md に [要確認] が残っています。factcheck を終えてから実行してください。")

    body = re.sub(r"^\s*<!--.*?-->\s*", "", src, count=1, flags=re.S).strip()
    lines = body.split("\n")
    title = lines[0].lstrip("# ").strip()
    sub_i = next(i for i, l in enumerate(lines[1:], 1) if l.strip())
    subtitle = lines[sub_i].strip().strip("*").strip()
    rest = "\n".join(lines[sub_i + 1:]).strip()
    rest = re.sub(r"^---\s*\n", "", rest)  # 冒頭の区切り線は不要

    images = [x for x in a.table_images.split(",") if x]
    tables = re.findall(r"(?:^\|.*\|[ \t]*\n)+", rest + "\n", flags=re.M)
    if len(tables) > len(images):
        sys.exit(f"表が{len(tables)}個ありますが、画像は{len(images)}個です。--table-images を指定してください。")
    for t, img in zip(tables, images):
        rest = rest.replace(t.rstrip("\n"), f"[画像を挿入：{pathlib.Path(img).name}]", 1)
    rest = rest.replace("<!-- PAYWALL -->", "[ここに Paywall を入れる]")
    rest = re.sub(r"\n{3,}", "\n\n", rest)

    uploads = sorted(set(re.findall(r"\[画像を挿入：([^\]]+)\]", rest)))
    if a.social:
        uploads.append(pathlib.Path(a.social).name)
    social_line = (f"- 記事の設定（Settings / SEO / Social preview など）で、SNS共有用の画像を {pathlib.Path(a.social).name} にする（欄が見つからなければ報告）。\n"
                   if a.social else "")

    out = f"""以下は、Chrome拡張機能（Claude in Chrome）に貼り付ける指示文です。
※ 先にSubstackにログインし、画像（{" / ".join(uploads) or "なし"}）をパソコンに保存しておく。

---ここから下をコピーして貼る---

https://japanhandover.substack.com の管理画面で、新しい記事（Post）の下書きを作ってください。私はログイン済みです。

{RULES}

【作業】新しい記事を作り、次の内容で下書き保存する。
- Title: {title}
- Subtitle: {subtitle}
- 本文：下の「本文ここから」〜「本文ここまで」の間。
{FORMAT}
{social_line}- 公開範囲（Audience）は Everyone（無料）。

本文ここから
{rest}
本文ここまで

最後に「できた／できなかった／私が手で操作する必要がある」を一覧で報告し、下書きのプレビューURLがあれば教えてください。

---ここまで---
"""
    (d / "chrome-handoff.md").write_text(out, encoding="utf-8")
    print(f"wrote {d / 'chrome-handoff.md'} ({len(out)} chars, tables replaced: {len(tables)})")


if __name__ == "__main__":
    main()
