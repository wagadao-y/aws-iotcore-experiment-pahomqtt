import argparse
import time
import paho.mqtt.client as mqtt

# 参考 : Use AWS IoT Core MQTT broker with standard MQTT libraries
# https://aws.amazon.com/jp/blogs/iot/use-aws-iot-core-mqtt-broker-with-standard-mqtt-libraries/
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("endpoint")
    args = parser.parse_args()

    mqttc = mqtt.Client(client_id="MyPC", protocol=mqtt.MQTTv5)
    mqttc.tls_set(
        ca_certs="certificates/AmazonRootCA1.pem",
        certfile="certificates/certificate.pem.crt",
        keyfile ="certificates/private.pem.key",
        tls_version=2)
    mqttc.on_connect = on_connect
    mqttc.on_message = on_message
    mqttc.connect(args.endpoint, 8883, 60)
    mqttc.loop_start()
    while(True):
        time.sleep(1)
        mqttc.publish(topic="MyPC/test-topic", payload='{"message":"Hello from MyPC"}', qos=0, retain=False)

# MQTTv5で接続するとon_connect()の引数にpropertiesが追加される
# https://github.com/eclipse/paho.mqtt.python/issues/575
def on_connect(mqttc, userdata, flags, rc, properties=None):
    print("Connected with result code " + str(rc))
    mqttc.subscribe("MyPC/test-topic", qos=0, options=None, properties=None)

def on_message(mqttc, userdata, msg):
    print("Received " + msg.topic + " " + str(msg.payload))

if __name__ == "__main__":
    main()