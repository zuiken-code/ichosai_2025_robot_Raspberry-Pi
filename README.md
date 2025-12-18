# ichosai_2025_robot_Raspberry-Pi

任天堂 Switch の Joy-Con を使って、モーターで動くトロッコ型ロボットを操作するための Raspberry Pi 用 Python プロジェクトです。  
Joy-Con の入力を取得し、Web アプリケーション（Flask）経由でロボットの有効 / 無効（enable / disable）を切り替えながら制御します。

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

---

## 目次

- [概要](#概要)
- [はじめに](#はじめに)
- [インストール](#インストール)
- [使い方](#使い方)
- [アーキテクチャ設計](#アーキテクチャ設計)
- [Flask を使用した理由](#flaskを使用した理由)
- [スクリーンショット](#スクリーンショット)
- [コントリビュート](#コントリビュート)
- [ライセンス](#ライセンス)
- [連絡先](#連絡先)

---

## 概要

このプロジェクトは、  
**Joy-Con をコントローラーとして使用し、Raspberry Pi 上でロボット（トロッコ）を制御すること**  
を目的としています。

Joy-Con のドライバーには、以下の OSS を使用しています。

- dkms-hid-nintendo  
  https://github.com/nicman23/dkms-hid-nintendo

また、ロボットの動作を Web ブラウザから制御できるようにするため、  
Flask を用いた Web アプリケーションを実装しています。

Web からの enable / disable 操作とロボット制御を同時に行う必要があるため、  
`app.py` 内でロボット制御コードを **並列処理** として実行しています。

AprilTag を用いた自己位置推定・制御のコードも実装していますが、  
現時点では正常に動作していません（今後の改善対象です）。

---

## はじめに

このセクションでは、本プロジェクトを動かすために必要な環境について説明します。

### 動作環境・前提条件

- Raspberry Pi（Raspberry Pi OS 推奨）
- Python 3.7 以上
- 任天堂 Switch Joy-Con
- モーターおよびモータードライバ（今回は arduino を用いて自作したものをお借りしました）
- I2C が有効化されていること

### 使用ライブラリ（外部）

- flask
- pygame
- requests
- smbus
- opencv-python（AprilTag 用）

### 使用ライブラリ（標準ライブラリ）

- os
- sys
- time
- threading

※ 標準ライブラリは Python に標準で含まれているため、  
追加でインストールする必要はありません。

---

## インストール

1. リポジトリをクローンします。

   ```
   git clone https://github.com/zuiken-code/ichosai_2025_robot_Raspberry-Pi.git
   cd ichosai_2025_robot_Raspberry-Pi
   ```

2. 必要な Python ライブラリをインストールします。

   ```
   pip install flask pygame requests smbus opencv-python
   ```

3. Joy-Con 用ドライバーをインストールします。

   ```
   git clone https://github.com/nicman23/dkms-hid-nintendo
   cd dkms-hid-nintendo

   sudo dkms add .
   sudo dkms build nintendo -v 3.2
   sudo dkms install nintendo -v 3.2
   ```

4. Raspberry Pi を再起動します。
   ```
   sudo reboot
   ```

---

## 使い方

1. Joy-Con を Raspberry Pi に Bluetooth 接続します。

2. Flask アプリケーションを起動します。

   ```
   python app.py
   ```

3. Web ブラウザで以下の URL にアクセスします。

   ```
   http://<RaspberryPi の IP>:5000
   ```

4. Web UI からロボットの enable / disable を切り替え、  
   Joy-Con を使ってロボットを操作します。

---

## アーキテクチャ設計

本プロジェクトでは、  
コントローラー入力とモーター制御を直接結びつけない設計を採用しています。

またモーター制御は Arduino によって行っており、  
Raspberry Pi とは役割を分離した構成になっています。
（モーター制御用の基板は先輩からお借りしたものを使用しています）

Arduino 側の制御コードは、以下のリポジトリで公開されています。

- https://github.com/zuiken-code/ichosai_2025_robot_Arduino

### 設計の流れ

1. Joy-Con（Controller）の入力状態を取得
2. 入力内容からロボットの状態を表す Model を生成
3. Model の状態に応じてモーター（Arduino）へ制御信号を送信

このように、クリーンアーキテクチャの考え方を参考にし、

- Controller（入力）
- Model（状態）
- ハードウェア制御（出力）

入力・状態・出力の責務を分離した構成を意識しています。

### この設計を採用した理由

- 入力と出力を直接結びつけると、処理が複雑になりやすいため
- ロボットの状態を Model として明示的に扱うことで、
  デバッグや挙動の把握がしやすくなるため
- 将来的に、
  - 別のコントローラーの追加
  - 自動制御（AprilTag 等）の導入  
    がしやすくなるため

---

## Flask を使用した理由

- 知っている Web フレームワークが Flask だったため
- Raspberry Pi 上で Python を用いてロボットを制御しており、
  言語の互換性が高かったため
- Web からの enable / disable 操作で
  ロボットの動作をリアルタイムに切り替える必要があり、
  並列処理による実装が最も現実的だと考えたため

---

## スクリーンショット

※ スクリーンショットやデモ動画は後日追加予定

![Screenshot](image_url_here)

---

## コントリビュート

バグ報告や改善提案は GitHub Issues からお願いします。  
Pull Request も歓迎します。

---

## ライセンス

本プロジェクトは MIT License のもとで公開されています。

---

## 連絡先

- GitHub Issues:  
  https://github.com/zuiken-code/ichosai_2025_robot_Raspberry-Pi/issues
