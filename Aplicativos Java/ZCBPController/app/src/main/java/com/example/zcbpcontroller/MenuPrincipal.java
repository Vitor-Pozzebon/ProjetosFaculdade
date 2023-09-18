package com.example.zcbpcontroller;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;

public class MenuPrincipal extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_menu_principal);
    }

    public void silasPage(View v){
        Intent silas = new Intent(this, SilasPage.class);
        startActivity(silas);
    }

    public void annPage(View v){
        Intent ann = new Intent(this, AnnPage.class);
        startActivity(ann);
    }

    public void baldricPage(View v){
        Intent baldric = new Intent(this, BaldricPage.class);
        startActivity(baldric);
    }

    public void clovisPage(View v){
        Intent clovis = new Intent(this, ClovisPage.class);
        startActivity(clovis);
    }

    public void nellyPage(View v){
        Intent nelly = new Intent(this, NellyPage.class);
        startActivity(nelly);
    }

    public void sansomPage(View v){
        Intent sansom = new Intent(this, SamsonPage.class);
        startActivity(sansom);
    }
}