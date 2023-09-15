package com.example.av1;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

public class Info extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_info);

        String login3 = getIntent().getStringExtra("login");
        String animal = getIntent().getStringExtra("animal");
        String apelido = getIntent().getStringExtra("apelido");

        TextView helloTV = findViewById(R.id.textViewInfo1);
        helloTV.setText("Login: " + login3);

        TextView helloTV2 = findViewById(R.id.textViewInfo2);
        helloTV2.setText("Animal de estimação: " + animal);

        TextView helloTV3 = findViewById(R.id.textViewInfo3);
        helloTV3.setText("Primeiro apelido: " + apelido);
    }

    public void confirmar2 (View v){

        Intent i = new Intent(this,Principal.class);
        startActivity(i);

    }
}