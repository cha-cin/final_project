package tw.edu.pu.cs.s1032869.mqtt_v2;

import android.os.Bundle;
import android.os.Handler;
import android.os.Message;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.ImageView;

import org.eclipse.paho.client.mqttv3.IMqttDeliveryToken;
import org.eclipse.paho.client.mqttv3.MqttCallback;
import org.eclipse.paho.client.mqttv3.MqttClient;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.MqttMessage;
import org.eclipse.paho.client.mqttv3.persist.MemoryPersistence;

public class MainActivity extends AppCompatActivity {
    MemoryPersistence persistence;
    Thread uiThread;
    String set[]=new String[24];
    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        //設定隱藏標題
        getSupportActionBar().hide();
        //設定隱藏狀態
        getWindow().getDecorView().setSystemUiVisibility(View.SYSTEM_UI_FLAG_FULLSCREEN);
        PahoDemo p =new PahoDemo();
        p.doDemo();
        uiThread = new uiThread();



    }

    private Handler mHandler = new Handler() {
        public void handleMessage(Message msg) {
            super.handleMessage(msg);
            for(int i=0;i<24;i++){
//                System.out.println(set[i]);
                if(set[i].charAt(0)=='9'){
                    to_replace_image(i+1);
                    System.out.println(set[i]+"  ("+(i/6)+","+(i%6+1)+")  You are so great!");}
                else
                    System.out.println(set[i]+"  ("+(i/6)+","+(i%6+1)+")  Bad");
            }
        }
    };

    class uiThread extends Thread {

        @Override
        public void run() {
            // TODO Auto-generated method stub
            super.run();
            try {
                Message msg = new Message();
                mHandler.sendMessage(msg);
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }

    public void to_replace_image(int i){
     switch(i){
         case 1:
             ImageView fire1 = (ImageView) findViewById(R.id.fire1);
             fire1.setImageDrawable(getResources().getDrawable(R.drawable.fire));
             break;
         case 2:
             ImageView fire2 = (ImageView) findViewById(R.id.fire2);
             fire2.setImageDrawable(getResources().getDrawable(R.drawable.fire));
             break;
         case 3:
             ImageView fire3 = (ImageView) findViewById(R.id.fire3);
             fire3.setImageDrawable(getResources().getDrawable(R.drawable.fire));
             break;
         case 4:
             ImageView fire4 = (ImageView) findViewById(R.id.fire4);
             fire4.setImageDrawable(getResources().getDrawable(R.drawable.fire));
             break;
         case 5:
             ImageView fire5 = (ImageView) findViewById(R.id.fire5);
             fire5.setImageDrawable(getResources().getDrawable(R.drawable.fire));
             break;
         case 6:
             ImageView fire6 = (ImageView) findViewById(R.id.fire6);
             fire6.setImageDrawable(getResources().getDrawable(R.drawable.fire));
             break;
         case 7:
             ImageView fire7 = (ImageView) findViewById(R.id.fire7);
             fire7.setImageDrawable(getResources().getDrawable(R.drawable.fire));
             break;
         case 8:
             ImageView fire8 = (ImageView) findViewById(R.id.fire8);
             fire8.setImageDrawable(getResources().getDrawable(R.drawable.fire));
             break;
         case 9:
             ImageView fire9 = (ImageView) findViewById(R.id.fire9);
             fire9.setImageDrawable(getResources().getDrawable(R.drawable.fire));
             break;
         case 10:
             ImageView fire10 = (ImageView) findViewById(R.id.fire10);
             fire10.setImageDrawable(getResources().getDrawable(R.drawable.fire));
             break;
         case 11:
             ImageView fire11 = (ImageView) findViewById(R.id.fire11);
             fire11.setImageDrawable(getResources().getDrawable(R.drawable.fire));
             break;
         case 12:
             ImageView fire12 = (ImageView) findViewById(R.id.fire12);
             fire12.setImageDrawable(getResources().getDrawable(R.drawable.fire));
             break;
         case 13:
             ImageView fire13 = (ImageView) findViewById(R.id.fire13);
             fire13.setImageDrawable(getResources().getDrawable(R.drawable.fire));
             break;
         case 14:
             ImageView fire14 = (ImageView) findViewById(R.id.fire14);
             fire14.setImageDrawable(getResources().getDrawable(R.drawable.fire));
             break;
         case 15:
             ImageView fire15 = (ImageView) findViewById(R.id.fire15);
             fire15.setImageDrawable(getResources().getDrawable(R.drawable.fire));
             break;
         case 16:
             ImageView fire16 = (ImageView) findViewById(R.id.fire16);
             fire16.setImageDrawable(getResources().getDrawable(R.drawable.fire));
             break;
         case 17:
             ImageView fire17 = (ImageView) findViewById(R.id.fire17);
             fire17.setImageDrawable(getResources().getDrawable(R.drawable.fire));
             break;
         case 18:
             ImageView fire18 = (ImageView) findViewById(R.id.fire18);
             fire18.setImageDrawable(getResources().getDrawable(R.drawable.fire));
             break;
         case 19:
             ImageView fire19 = (ImageView) findViewById(R.id.fire19);
             fire19.setImageDrawable(getResources().getDrawable(R.drawable.fire));
             break;
         case 20:
             ImageView fire20 = (ImageView) findViewById(R.id.fire20);
             fire20.setImageDrawable(getResources().getDrawable(R.drawable.fire));
             break;
         case 21:
             ImageView fire21 = (ImageView) findViewById(R.id.fire21);
             fire21.setImageDrawable(getResources().getDrawable(R.drawable.fire));
             break;
         case 22:
             ImageView fire22 = (ImageView) findViewById(R.id.fire22);
             fire22.setImageDrawable(getResources().getDrawable(R.drawable.fire));
             break;
         case 23:
             ImageView fire23 = (ImageView) findViewById(R.id.fire23);
             fire23.setImageDrawable(getResources().getDrawable(R.drawable.fire));
             break;
         case 24:
             ImageView fire24 = (ImageView) findViewById(R.id.fire24);
             fire24.setImageDrawable(getResources().getDrawable(R.drawable.fire));
             break;
     }

    }


    public void set_the_array(String get_forty_eight){
        for(int i=0;i<24;i++){
            set[i]= String.valueOf(get_forty_eight.subSequence(i,i+1));
        }
        uiThread.start();
    }


    public class PahoDemo implements MqttCallback {
        MqttClient client;

            public void doDemo() {
                MqttMessage message = new MqttMessage();
                persistence = new MemoryPersistence();
                try {
                    client = new MqttClient("tcp://192.168.2.200:1883", "Sending",persistence);
                    client.connect();
                    client.setCallback(this);
                    client.subscribe("test");
                    messageArrived("test",message);
//                    message.setPayload("123456789012345678901234567890123456789012345678".getBytes());
//                    client.publish("test",message );
                } catch (MqttException e) {
                    e.printStackTrace();
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }

            @Override
            public void connectionLost(Throwable cause) {
                // TODO Auto-generated method stub

            }

            @Override
            public void messageArrived(String topic, MqttMessage message) throws Exception {
                // TODO Auto-generated method stub
                String get_forty_eight=String.valueOf(message);
                set_the_array(get_forty_eight);
            }

            @Override
            public void deliveryComplete(IMqttDeliveryToken token) {
                // TODO Auto-generated method stub

            }

        }
}

//                set[0]= String.valueOf(get_forty_eight.subSequence(0,2));
//                set[1]= String.valueOf(get_forty_eight.subSequence(2,4));
//                set[2]= String.valueOf(get_forty_eight.subSequence(4,6));
//                set[3]= String.valueOf(get_forty_eight.subSequence(6,8));
//                set[4]= String.valueOf(get_forty_eight.subSequence(8,10));
//                set[5]= String.valueOf(get_forty_eight.subSequence(10,12));
//                set[6]= String.valueOf(get_forty_eight.subSequence(12,14));
//                set[7]= String.valueOf(get_forty_eight.subSequence(14,16));
//                set[8]= String.valueOf(get_forty_eight.subSequence(16,18));
//                set[9]= String.valueOf(get_forty_eight.subSequence(18,20));
//                set[10]= String.valueOf(get_forty_eight.subSequence(20,22));
//                set[11]= String.valueOf(get_forty_eight.subSequence(22,24));
//                set[12]= String.valueOf(get_forty_eight.subSequence(24,26));
//                set[13]= String.valueOf(get_forty_eight.subSequence(26,28));
//                set[14]= String.valueOf(get_forty_eight.subSequence(28,30));
//                set[15]= String.valueOf(get_forty_eight.subSequence(30,32));
//                set[16]= String.valueOf(get_forty_eight.subSequence(32,34));
//                set[17]= String.valueOf(get_forty_eight.subSequence(34,36));
//                set[18]= String.valueOf(get_forty_eight.subSequence(36,38));
//                set[19]= String.valueOf(get_forty_eight.subSequence(38,40));
//                set[20]= String.valueOf(get_forty_eight.subSequence(40,42));
//                set[21]= String.valueOf(get_forty_eight.subSequence(42,44));
//                set[22]= String.valueOf(get_forty_eight.subSequence(44,46));
//                set[23]= String.valueOf(get_forty_eight.subSequence(46,48));