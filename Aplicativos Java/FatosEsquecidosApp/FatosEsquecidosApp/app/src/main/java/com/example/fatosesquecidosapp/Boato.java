package com.example.fatosesquecidosapp;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;

public class Boato extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_boato);
    }

    public void voltar2(View v){
        Intent i2 = new Intent(this, MainActivity.class);
        startActivity(i2);
    }
}