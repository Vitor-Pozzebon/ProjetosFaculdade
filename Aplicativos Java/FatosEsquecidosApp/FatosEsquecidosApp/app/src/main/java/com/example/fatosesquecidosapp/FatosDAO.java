package com.example.fatosesquecidosapp;

import java.util.ArrayList;
import java.util.List;

public class FatosDAO {
    public List<ItensFatos> fatos = new ArrayList<>();

    public FatosDAO(){
        for (int i = 0; i < 100; i++){
            fatos.add(new ItensFatos("Nome " + i+1, "Data " + i+1, "Gravidade " + i+1,
                    "Ações " + i+1, "Planejamentos " + i+1));
        }
    }

    public List<ItensFatos> listar(){
        return fatos;
    }
}
