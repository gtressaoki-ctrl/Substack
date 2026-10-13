---
name: deepdive
description: 月2回の有料深掘り号（1,500〜2,500 words、独自集計の表またはグラフ用データ必須、冒頭3〜4段落無料）を作る。「deepdive」「深掘り」で使う。
---
README.md の「深掘り号」に従う。
1. テーマ候補を3つ出し「読者がこの1本で1つ判断を下せるか」で評価、編集長の選択を待って **停止**（指定済みなら省略）。
2. `issues/YYYY-MM-DD-slug/` に outline / draft / factcheck / final / promo を作成。独自集計の表（またはCSV）を必ず1つ。冒頭3〜4段落で無料読者にも価値が伝わり、ペイウォール位置を `<!-- PAYWALL -->` で示す。
3. 表は画像（`images/`）にし、元データはCSVで残す。編集長コメントが入ったら `python3 tools/make_handoff.py issues/<dir> --table-images ...` で拡張機能への指示文を生成する。テーマ候補は `research/deepdive-candidates.md` に記録。
4. 絶対ルール全項目を守り、公開前チェックリストを表示して **停止**。
