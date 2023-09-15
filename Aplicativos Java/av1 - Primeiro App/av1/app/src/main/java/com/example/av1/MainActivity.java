package com.example.av1;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    @Override

    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_main);
        String newLogin = getIntent().getStringExtra("newLogin");
        TextView helloTV2 = findViewById(R.id.editTextName);
        helloTV2.setText(newLogin);

    }

    public void validar (View v){

        EditText senhaET = findViewById(R.id.editTextPassword);
        EditText loginET = findViewById(R.id.editTextName);

        String valor = senhaET.getText().toString();
        String login2 = loginET.getText().toString();

            if (valor.equals("aluno")){
                Intent i1 = new Intent(this,Principal.class);
                i1.putExtra("login",login2);
                startActivity(i1);


            }
            else{
                Intent i2 = new Intent(this,LoginIncorreto.class);
                startActivity(i2);

            }
    }

}