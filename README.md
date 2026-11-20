# GN Frontier Shaders

GN Frontierの廃都市向けに調整したシェーダー設定です。Complementary Unbound r5.9.3を使い、彩度と露出を抑えて、遠景の霧や雨上がりの水たまりを調整しています。[GN Frontier](https://github.com/syarukasu/GN-Frontier) · [Complementary Development 公式サイト](https://www.complementary.dev/)

## 導入

1. `GN-Frontier-Shaders-Setup.zip` を展開し、そのフォルダをターミナルで開きます。[セットアップZIP](https://github.com/syarukasu/GN-Frontier-Shaders/releases/latest)
2. Python 3.8以降でインストーラーを実行します。引数にはMinecraftインスタンスの `shaderpacks` フォルダを指定してください。

   ```powershell
   py -3 install.py "C:\path\to\minecraft\shaderpacks"
   ```

3. ゲームのシェーダー一覧で **GN Frontier Shaders.zip** を選びます。

インストーラーはフォルダ内の公式版r5.9.3を探し、見つからなければ公式配布元から取得します。SHA-256を照合し、別名のZIPとGN用の設定を保存します。公式ZIPをすでに別の場所に置いている場合は `--base "C:\path\to\ComplementaryUnbound_r5.9.3.zip"` で指定できます。[公式配布ファイル](https://www.curseforge.com/minecraft/shaders/complementary-unbound/files/8884656)

## GN Frontierとの組み合わせ

設定値はMinecraft 1.20.1・Forge・Oculus 1.8.0で実機検証したGN Frontierの構成と同じです。TaCZスコープの遮光、歩行時の揺れとぼけはGN Frontier 0.2.15の専用MODが描画します。[専用MOD](https://github.com/syarukasu/GN-Frontier/tree/main/addon)

## ライセンスとクレジット

シェーダー本体はEminGTとComplementary Developmentによる**Complementary Unbound r5.9.3**です。本体には公式ZIP内のComplementary License Agreementが適用されます。このリポジトリのインストーラーとGN用の設定はMITライセンスです。[Complementary Development 公式サイト](https://www.complementary.dev/) · [MITライセンス](LICENSE)
