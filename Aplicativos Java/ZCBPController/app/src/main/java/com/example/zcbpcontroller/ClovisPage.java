package com.example.zcbpcontroller;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.content.DialogInterface;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.TextView;
import android.widget.Toast;

public class ClovisPage extends AppCompatActivity {

    public TextView meuTextView;
    public int numeroAtual;

    @SuppressLint("MissingInflatedId")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_clovis_page);

        meuTextView = findViewById(R.id.textViewLevel);
        numeroAtual = 0; // Defina o valor inicial do número

        // Atualize o TextView com o valor inicial
        meuTextView.setText(String.valueOf(numeroAtual));

        CheckBox cba = findViewById(R.id.checkBoxAmarelo);
        CheckBox cbl1 = findViewById(R.id.checkBoxLaranja1);
        CheckBox cbl2 = findViewById(R.id.checkBoxLaranja2);
        CheckBox cbv1 = findViewById(R.id.checkBoxVermelho1);
        CheckBox cbv2 = findViewById(R.id.checkBoxVermelho2);
        CheckBox cbv3 = findViewById(R.id.checkBoxVermelho3);
        cba.setEnabled(false);
        cba.setClickable(false);
        cbl1.setEnabled(false);
        cbl2.setEnabled(false);
        cbv1.setEnabled(false);
        cbv2.setEnabled(false);
        cbv3.setEnabled(false);

        CheckBox cbLife0 = findViewById(R.id.checkBoxLife0);
        CheckBox cbLife2 = findViewById(R.id.checkBoxLife2);
        CheckBox cbLife3 = findViewById(R.id.checkBoxLife3);
        cbLife0.setChecked(true);
        cbLife0.setClickable(false);
        cbLife2.setClickable(false);
        cbLife3.setClickable(false);
    }

    public void somarUm(View view) {
        // Somar 1 ao número atual
        if(numeroAtual != 43){
            numeroAtual++;
        }
        // Atualizar o TextView com o novo valor
        meuTextView.setText(String.valueOf(numeroAtual));

        //======================================================================================================================
        //Ao subir para o amarelo
        if(numeroAtual >= 7){
            CheckBox cbAmarelo = findViewById(R.id.checkBoxAmarelo);
            cbAmarelo.setChecked(true);
        }
        //======================================================================================================================
        //Ao subir para o laranja
        if(numeroAtual == 19){
            AlertDialog.Builder msgOrangeList = new AlertDialog.Builder(this);
            msgOrangeList.setTitle("Escolha uma habilidade");
            final String[] opcoes = getResources().getStringArray(R.array.LaranjaClovis);
            msgOrangeList.setItems(R.array.LaranjaClovis, new DialogInterface.OnClickListener() {
                public void onClick(DialogInterface dialog, int which) {
                    // The 'which' argument contains the index position
                    // of the selected item
                    String escolha = opcoes[which];
                    if(escolha.contains("+1 Ação Corpo a Corpo Grátis")){
                        CheckBox cbl1 = findViewById(R.id.checkBoxLaranja1);
                        cbl1.setChecked(true);
                    }else{
                        CheckBox cbl2 = findViewById(R.id.checkBoxLaranja2);
                        cbl2.setChecked(true);
                    }
                    Toast.makeText(ClovisPage.this, "Opção escolhida: " + escolha, Toast.LENGTH_SHORT).show();
                }
            });
            msgOrangeList.show();
        }
        //======================================================================================================================
        //ao subir para o vermelho
        if(numeroAtual == 43){
            AlertDialog.Builder msgRedList = new AlertDialog.Builder(this);
            msgRedList.setTitle("Escolha uma habilidade");
            final String[] opcoes = getResources().getStringArray(R.array.VermelhoClovis);
            msgRedList.setItems(R.array.VermelhoClovis, new DialogInterface.OnClickListener() {
                public void onClick(DialogInterface dialog, int which) {
                    // The 'which' argument contains the index position
                    // of the selected item
                    String escolha = opcoes[which];
                    if(escolha.contains("+1 Ação de Combate Grátis")){
                        CheckBox cbv1 = findViewById(R.id.checkBoxVermelho1);
                        cbv1.setChecked(true);
                    }else{
                        if(escolha.contains("+1 no Dado: Combate")){
                            CheckBox cbv2 = findViewById(R.id.checkBoxVermelho2);
                            cbv2.setChecked(true);
                        }else{
                            CheckBox cbv3 = findViewById(R.id.checkBoxVermelho3);
                            cbv3.setChecked(true);
                        }
                    }
                    Toast.makeText(ClovisPage.this, "Opção escolhida: " + escolha, Toast.LENGTH_SHORT).show();
                }
            });
            msgRedList.show();
        }
    }

    public void subtUm(View view) {
        // Somar 1 ao número atual
        if(numeroAtual != 0){
            numeroAtual--;
        }

        // Atualizar o TextView com o novo valor
        meuTextView.setText(String.valueOf(numeroAtual));

        //======================================================================================================================
        //ao sair do amarelo
        if(numeroAtual < 7){
            CheckBox cbAmarelo = findViewById(R.id.checkBoxAmarelo);
            cbAmarelo.setChecked(false);
        }

        //======================================================================================================================
        //ao sair do laranja
        if(numeroAtual < 19){
            CheckBox cbl1 = findViewById(R.id.checkBoxLaranja1);
            CheckBox cbl2 = findViewById(R.id.checkBoxLaranja2);
            cbl1.setChecked(false);
            cbl2.setChecked(false);
        }

        //======================================================================================================================
        //ao sair do vermelho
        if(numeroAtual < 43){
            CheckBox cbv1 = findViewById(R.id.checkBoxVermelho1);
            CheckBox cbv2 = findViewById(R.id.checkBoxVermelho2);
            CheckBox cbv3 = findViewById(R.id.checkBoxVermelho3);
            cbv1.setChecked(false);
            cbv2.setChecked(false);
            cbv3.setChecked(false);
        }
    }

    public void voltar(View v){
        finish();
    }

    public void exibirConfirmacao1(View v){
        //caixa de diálogo com botões de pergunta
        AlertDialog.Builder msgbox = new AlertDialog.Builder(this);
        msgbox.setTitle("Confirmação");
        msgbox.setMessage("Confirmar o primeiro dano sofrido?");
        msgbox.setPositiveButton("Sim", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialogInterface, int i) {
                validar2();
                Toast.makeText(ClovisPage.this, "Dano Sofrido. Cuidado!", Toast.LENGTH_LONG).show();
            }
        });
        msgbox.setNegativeButton("Não", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialogInterface, int i) {
                CheckBox cbLife1 = findViewById(R.id.checkBoxLife1);
                cbLife1.setChecked(false);
                Toast.makeText(ClovisPage.this, "Operação Cancelada", Toast.LENGTH_LONG).show();
            }
        });
        msgbox.show();
    }

    public void exibirConfirmacao2(View v){
        AlertDialog.Builder msgbox = new AlertDialog.Builder(this);
        msgbox.setTitle("Confirmação");
        msgbox.setMessage("Confirmar o segundo dano sofrido?");
        msgbox.setPositiveButton("Sim", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialogInterface, int i) {
                validar3();
                Toast.makeText(ClovisPage.this, "Dano Sofrido. Cuidado!", Toast.LENGTH_LONG).show();
            }
        });
        msgbox.setNegativeButton("Não", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialogInterface, int i) {
                CheckBox cbLife2 = findViewById(R.id.checkBoxLife2);
                cbLife2.setChecked(false);
                Toast.makeText(ClovisPage.this, "Operação Cancelada", Toast.LENGTH_LONG).show();
            }
        });
        msgbox.show();
    }

    public void exibirConfirmacao3(View v){
        AlertDialog.Builder msgbox = new AlertDialog.Builder(this);
        msgbox.setTitle("Confirmação");
        msgbox.setMessage("Confirmar o terceiro dano sofrido?");
        msgbox.setPositiveButton("Sim", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialogInterface, int i) {
                validar4();
                dialogBoxdeath();
                Toast.makeText(ClovisPage.this, "Morte do Personagem", Toast.LENGTH_LONG).show();
                Button btSoma = findViewById(R.id.buttonSoma);
                Button btSub = findViewById(R.id.buttonSub);
                btSoma.setEnabled(false);
                btSub.setEnabled(false);
            }
        });
        msgbox.setNegativeButton("Não", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialogInterface, int i) {
                CheckBox cbLife3 = findViewById(R.id.checkBoxLife3);
                cbLife3.setChecked(false);
                Toast.makeText(ClovisPage.this, "Operação Cancelada", Toast.LENGTH_LONG).show();
            }
        });
        msgbox.show();
    }

    public void dialogBoxdeath(){
        AlertDialog.Builder msgboxDeath = new AlertDialog.Builder(this);
        msgboxDeath.setTitle("Morte");
        msgboxDeath.setMessage("Infelizmente sua jornada acaba por aqui");
        msgboxDeath.show();
    }
    public void validar2(){
        CheckBox cbLife2 = findViewById(R.id.checkBoxLife2);
        CheckBox cbLife1 = findViewById(R.id.checkBoxLife1);
        CheckBox cbLife0 = findViewById(R.id.checkBoxLife0);
        cbLife0.setChecked(false);
        cbLife0.setClickable(false);
        cbLife1.setClickable(false);
        cbLife2.setClickable(true);
    }

    public void validar3(){
        CheckBox cbLife1 = findViewById(R.id.checkBoxLife1);
        CheckBox cbLife2 = findViewById(R.id.checkBoxLife2);
        CheckBox cbLife3 = findViewById(R.id.checkBoxLife3);
        cbLife1.setChecked(false);
        cbLife1.setClickable(false);
        cbLife2.setClickable(false);
        cbLife3.setClickable(true);
    }

    public void validar4(){
        CheckBox cbLife2 = findViewById(R.id.checkBoxLife2);
        CheckBox cbLife3 = findViewById(R.id.checkBoxLife3);
        cbLife2.setChecked(false);
        cbLife2.setClickable(false);
        cbLife3.setClickable(false);
    }
}