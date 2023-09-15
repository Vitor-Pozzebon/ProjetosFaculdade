package com.example.fatosesquecidosapp;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.RecyclerView;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;

public class Fato extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_fato);
    }

    public void voltar(View v){
        Intent i = new Intent(this, MainActivity.class);
        startActivity(i);
    }
}