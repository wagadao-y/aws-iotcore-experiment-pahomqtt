paho-mqttを使ってAWS IoT CoreにPub/Subするだけのスクリプトです。

### 実行方法
IoT Coreのモノの証明書をcertificatesフォルダに保管し、paho-client.pyを実行してください。
プライベートキー : private.pem.key  
デバイス証明書 : certificate.pem.crt  
ルートCA証明書 : Amazon-root-CA-1.pem  
```
# コマンドライン引数のAWS IoT Coreのデバイスエンドポイントは読み替えてください
pip install paho-mqtt
python .\paho-client.py "xxxxxxxxxx-ats.iot.ap-northeast-1.amazonaws.com"
```
