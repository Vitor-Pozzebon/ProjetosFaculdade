package com.example.fatosesquecidosapp;

public class ItensFatos {
    private String nome;
    private String data;
    private String gravidade;
    private String acoes;
    private String planejamento;

    public ItensFatos(String nome, String data, String gravidade, String acoes, String planejamento) {
        this.nome = nome;
        this.data = data;
        this.gravidade = gravidade;
        this.acoes = acoes;
        this.planejamento = planejamento;
    }

    public String getNome() {
        return nome;
    }

    public String getData() {
        return data;
    }

    public String getGravidade() {
        return gravidade;
    }

    public String getAcoes() {
        return acoes;
    }

    public String getPlanejamento() {
        return planejamento;
    }
}


