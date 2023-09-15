package com.example.av1;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

public class Principal extends AppCompatActivity {
    String login3;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_principal);

        String login = getIntent().getStringExtra("login");
        TextView helloTV = findViewById(R.id.textView4);
        helloTV.setText("Olá Aluno " + login);
        login3=login;

    }

    public void confirmar (View v){

        EditText animalET = findViewById(R.id.editTextAnimal);
        EditText apelidoET = findViewById(R.id.editTextNickName);

        String animal = animalET.getText().toString();
        String apelido = apelidoET.getText().toString();

        Intent i3 = new Intent(this, Info.class);
        i3.putExtra("animal",animal);
        i3.putExtra("apelido",apelido);
        i3.putExtra("login", login3);

        startActivity(i3);
    }


}