package com.example.fatosesquecidosapp;

import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.NotificationCompat;
import androidx.core.app.NotificationManagerCompat;

import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.content.Intent;
import android.os.Build;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;

public class MainActivity extends AppCompatActivity {

    private String CHANNEL_ID = "Fatos";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        createNotificationChannel();
    }

    public void fatos(View v) {
        Intent i = new Intent(this, Fato.class);
        startActivity(i);
    }

    public void boatos(View v) {
        Intent i2 = new Intent(this, Boato.class);
        startActivity(i2);
    }

    public void procurarFato(View v) {
        Intent i3 = new Intent(this, ListaFatos.class);
        startActivity(i3);
    }

    private void createNotificationChannel() {

        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            CharSequence name = "Fatos Esquecidos App";
            String description = "Contagem de Boatos encontrados";
            int importance = NotificationManager.IMPORTANCE_DEFAULT;
            NotificationChannel channel = new NotificationChannel(CHANNEL_ID, name, importance);
            channel.setDescription(description);
            NotificationManager notificationManager =
                    getSystemService(NotificationManager.class);
            notificationManager.createNotificationChannel(channel);
        }
    }

    public static int notificationId = 1;
    FatosAdapter f = new FatosAdapter();


    public void notificationAction(View v) {

        NotificationCompat.Builder builder = new NotificationCompat.Builder(this, CHANNEL_ID)
                .setSmallIcon(R.drawable.ic_launcher_foreground)
                .setContentTitle("Contagem OK")
                .setContentText("Foram encontrados " + f.getItemCount() + " boatos.")
                .setPriority(NotificationCompat.PRIORITY_DEFAULT);
        NotificationManagerCompat notificationManager = NotificationManagerCompat.from(this);
        notificationManager.notify(notificationId, builder.build());

    }
}