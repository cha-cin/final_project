package com.example.user.darkflamemaster;


import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.KeyEvent;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import org.eclipse.paho.client.mqttv3.IMqttDeliveryToken;
import org.eclipse.paho.client.mqttv3.MqttCallback;
import org.eclipse.paho.client.mqttv3.MqttClient;
import org.eclipse.paho.client.mqttv3.MqttClientPersistence;
import org.eclipse.paho.client.mqttv3.MqttConnectOptions;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.MqttMessage;
import org.eclipse.paho.client.mqttv3.persist.MemoryPersistence;



public class MainActivity extends AppCompatActivity {
    private MqttClient client;
    private MqttConnectOptions connOpts;
    private String topic = "fire6";
    private String content = "1";
    private int qos = 0;
    private String broker = "tcp://192.168.2.200:1883";
    private String clientId = "username";
    MemoryPersistence persistence;

    private TextView txv;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        //設定隱藏標題
        getSupportActionBar().hide();
        //設定隱藏狀態
        getWindow().getDecorView().setSystemUiVisibility(View.SYSTEM_UI_FLAG_FULLSCREEN);
        txv = (TextView) findViewById(R.id.txv);
        connect();
        subscribe();

    }



    public void connect()
    {
        boolean flag = false;
        persistence = new MemoryPersistence();
        try
        {
            client = new MqttClient(broker, clientId, persistence);
            connOpts = new MqttConnectOptions();
            connOpts.setCleanSession(true);
            client.connect(connOpts);
        }
        catch(MqttException e)
        {
            System.out.println("reason "+e.getReasonCode());
            System.out.println("msg "+e.getMessage());
            System.out.println("loc "+e.getLocalizedMessage());
            System.out.println("cause "+e.getCause());
            System.out.println("excep "+e);
            e.printStackTrace();
        }
        if(client != null)
        {
            flag = true;
        }
        else
        {
            flag = false;
        }
        txv.setText("你 CONNECT 的狀態是: "+String.valueOf(flag));
    }

    public void publish()
    {
        MqttMessage message = new MqttMessage(content.getBytes());
        message.setQos(qos);

        try
        {
            client.publish(topic, message);
            //txv.setText("你 PUBLISH 的字串是: "+String.valueOf(content));
        }
        catch (MqttException e)
        {
            System.out.println("reason "+e.getReasonCode());
            System.out.println("msg "+e.getMessage());
            System.out.println("loc "+e.getLocalizedMessage());
            System.out.println("cause "+e.getCause());
            System.out.println("excep "+e);
            e.printStackTrace();
            //txv.setText(String.valueOf(e.getReasonCode()));
        }
    }

    public void subscribe()
    {
        try
        {

            client.subscribe(topic, qos);
            txv.setText("你 SUBSCRIBE 獲得的字串是: "+String.valueOf("1111"));
        }
        catch(MqttException e)
        {
            System.out.println("reason "+e.getReasonCode());
            System.out.println("msg "+e.getMessage());
            System.out.println("loc "+e.getLocalizedMessage());
            System.out.println("cause "+e.getCause());
            System.out.println("excep "+e);
            e.printStackTrace();
            //txv.setText(String.valueOf(e.getReasonCode()));
        }
    }
}