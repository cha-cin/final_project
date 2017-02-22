package com.technoatp.speech_to_text;

import java.util.ArrayList;
import java.util.Locale;
import android.app.Activity;
import android.content.ActivityNotFoundException;
import android.content.Intent;
import android.os.Bundle;
import android.speech.RecognizerIntent;
import android.view.View;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.TextView;
import android.widget.Toast;

import org.eclipse.paho.client.mqttv3.MqttClient;
import org.eclipse.paho.client.mqttv3.MqttConnectOptions;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.MqttMessage;
import org.eclipse.paho.client.mqttv3.persist.MemoryPersistence;

public class MainActivity extends Activity {

    protected static final int RESULT_SPEECH = 1;

    private ImageButton btnSpeak;
    private TextView Text;

    private MqttClient client;
    private MqttConnectOptions connOpts;
    private String topic = "123";
    private String content ;
    private int qos = 2;
    private String broker = "tcp://192.168.2.150:1883";
    private String clientId = "username";
    MemoryPersistence persistence;

    private TextView txv;
    private Button conBtn;
    private Button publishBtn;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Text = (TextView) findViewById(R.id.Text);
        btnSpeak = (ImageButton) findViewById(R.id.mic);

        conBtn = (Button) findViewById(R.id.button);
        publishBtn = (Button) findViewById(R.id.button2);


        btnSpeak.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View v) {

                Intent intent = new Intent(
                        RecognizerIntent.ACTION_RECOGNIZE_SPEECH);

                intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, Locale.getDefault());

                try {
                    startActivityForResult(intent, RESULT_SPEECH);
                    Text.setText("");
                } catch (ActivityNotFoundException a) {
                    Toast.makeText(getApplicationContext(),
                            "Your device doesn't support Speech to Text",
                            Toast.LENGTH_SHORT).show();
                }
            }
        });

        conBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
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
                //txv.setText(String.valueOf(flag));
            }
        });

        publishBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                MqttMessage message = new MqttMessage(content.getBytes());
                message.setQos(qos);
                try
                {
                    client.publish(topic, message);
                }
                catch (MqttException e)
                {
                    System.out.println("reason "+e.getReasonCode());
                    System.out.println("msg "+e.getMessage());
                    System.out.println("loc "+e.getLocalizedMessage());
                    System.out.println("cause "+e.getCause());
                    System.out.println("excep "+e);
                    e.printStackTrace();
                }
            }
        });

    }



    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);

        switch (requestCode) {
            case RESULT_SPEECH: {
                if (resultCode == RESULT_OK && null != data) {

                    ArrayList<String> text = data
                            .getStringArrayListExtra(RecognizerIntent.EXTRA_RESULTS);

                    Text.setText(text.get(0));
                    System.out.println(text.get(0)+"11111111111111111111111111111111");
                    content=text.get(0);
                }
                break;
            }

        }
    }

    public void connect()
    {

    }

    public void publish()
    {

    }

    public void subscribe()
    {
        try
        {
            client.subscribe(topic, qos);
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
    }

    public void disconnect()
    {
        try
        {
            client.disconnect();
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
    }
}