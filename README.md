# 

## pyenv + poetry環境構築
- `pyenv local 3.11.1`
- `poetry init`
- `poetry config virtualenvs.in-project true`
- `poetry env use 3.11.1`
- `poetry shell`

## Flet
- `poetry add flet`
- OS windowの場合
  - `flet run counter.py`
- webの場合
  - `flet run --web counter.py`

## Flet プロジェクトの作成
- `poetry run flet create <project-name>`
  - `poetry run flet create app`

## Flutter環境構築
https://docs.flutter.dev/get-started/install/macos/mobile-ios?tab=download

参考サイト
- https://flet.dev/docs/tutorials/python-realtime-chat
