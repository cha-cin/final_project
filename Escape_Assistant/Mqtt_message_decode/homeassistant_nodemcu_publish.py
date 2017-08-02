import paho.mqtt.client as mqtt

num_list = ["thirteen" , "fourteen" , "fifteen" , "sixteen" , "seventeen" ,
"eighteen" , "nineteen" , "twenty" , "tone" , "ttwo" , "tthree" , "tfour"]

eng_list = ["a" , "b" , "c" , "d" , "e" , "f" , "g" , "h" , "i" , "j"]

topic_select=0

while topic_select <12 :
        f = open('direction.txt', 'r')
        f.seek(topic_select,0)
        a_str = f.read(2)
        f.close()

        #f = open('LED_test'+a_str[0]+'.py', 'r')
        #b_str = f.read()
        #f.close()

        #f = open('LED_test'+a_str[1]+'.py', 'r')
        #c_str = f.read()
        #f.close()

        f = open('LED_sample.py', 'r')
        b_str = f.read()
        f.close()

        f = open('LED.py', 'w')
        f.truncate()
        f.write(b_str+"\n\t"+eng_list[int(a_str[0])]+"()\n\t"+eng_list[int(a_str[1])]+"()")
        f.close()

        f = open('LED.py', 'r')
        c_str = f.read()
        f.close()

        _g_cst_ToMQTTTopicServerIP = "192.168.2.200"
        _g_cst_ToMQTTTopicServerPort = 1883 #port
        _g_cst_MQTTTopicName = num_list[topic_select] #TOPIC name

        mqttc = mqtt.Client("python_pub")
        mqttc.connect(_g_cst_ToMQTTTopicServerIP, _g_cst_ToMQTTTopicServerPort)
        mqttc.publish(_g_cst_MQTTTopicName,c_str)
        print(_g_cst_MQTTTopicName)


        print (c_str)

        topic_select=topic_select+1