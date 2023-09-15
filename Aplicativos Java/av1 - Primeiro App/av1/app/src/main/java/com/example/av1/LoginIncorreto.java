package com.example.av1;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;

public class LoginIncorreto extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login_incorreto);
    }
    public void refactor (View v){

        EditText newLoginET = findViewById(R.id.editTextLoginRefactor);

        String newLogin = newLoginET.getText().toString();
        String login3 = getIntent().getStringExtra("login");


        Intent i = new Intent(this, MainActivity.class);
        i.putExtra("newLogin", newLogin);
        startActivity(i);


    }




}