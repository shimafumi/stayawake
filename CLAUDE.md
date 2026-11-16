# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 概要

Windows 専用の小さなユーティリティ。実行中は PC のスリープとディスプレイの消灯を防ぎ、コンソールに現在時刻を 1 秒ごとに上書き表示する。外部ライブラリは使わず、Python 標準ライブラリのみ。ビルド・lint・テストの仕組みはない。

## 実行方法

- `stayawake.bat` をダブルクリック（自分のフォルダに `cd` してから `py stayawake.py` を実行する）
- 直接実行する場合（Windows の Python ランチャー `py` が必要）:
  - PowerShell: `py .\stayawake.py`
  - Bash: `py ./stayawake.py`
- 終了は Ctrl+C

## 仕組み

- [stayawake.py](stayawake.py) が Win32 API `SetThreadExecutionState` を `ctypes.windll.kernel32` から呼ぶ。起動時に `ES_CONTINUOUS | ES_DISPLAY_REQUIRED | ES_SYSTEM_REQUIRED` を設定し、`KeyboardInterrupt`（Ctrl+C）を受けたら `ES_CONTINUOUS` だけを設定し直して元に戻す。
- この設定はスレッド単位で、プロセスが終われば OS が解除する。そのため、ウィンドウを閉じて終了した場合も設定が残ることはない。
- `ctypes.windll` を使うため、Windows 以外では動かない。
- Python ファイルの名前を変えるときは [stayawake.bat](stayawake.bat) も直す。
- `.bat` は CRLF でないと動かないことがあるため、[.gitattributes](.gitattributes) で改行コードを CRLF に固定している。
