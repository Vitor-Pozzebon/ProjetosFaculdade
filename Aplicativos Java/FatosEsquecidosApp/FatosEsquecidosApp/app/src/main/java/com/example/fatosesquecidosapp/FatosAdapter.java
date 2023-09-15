package com.example.fatosesquecidosapp;

import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

public class FatosAdapter extends RecyclerView.Adapter<FatosAdapter.fatosViewHolder>{

    public static class fatosViewHolder extends RecyclerView.ViewHolder{
        public TextView nomeTV;
        public TextView dataTV;
        public TextView gravidadeTV;
        public TextView acoesTV;
        public TextView planejamentosTV;
        public fatosViewHolder(@NonNull View itemView) {
            super(itemView);
            nomeTV = itemView.findViewById(R.id.textViewName);
            gravidadeTV = itemView.findViewById(R.id.textViewGravity);
            dataTV = itemView.findViewById(R.id.textViewDate);
            acoesTV = itemView.findViewById(R.id.textViewActions);
            planejamentosTV = itemView.findViewById(R.id.textViewPlanning);
        }
    }

    private FatosDAO dao = new FatosDAO();
    private int criadosCount = 0;
    private int associadosCount = 0;

    public int getAssociadosCount() {
        return associadosCount;
    }

    public void setAssociadosCount(int associadosCount) {
        this.associadosCount = associadosCount;
    }

    public int contador = getAssociadosCount();


    @NonNull
    @Override
    public fatosViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        int a = Log.i("FatosAdapter", "Criados: " + criadosCount++);
        contador = a;

        View v = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.layout_fato_item, parent, false);
        fatosViewHolder vh = new fatosViewHolder(v);
        return vh;
    }

    @Override
    public void onBindViewHolder(@NonNull fatosViewHolder holder, int position) {
        ItensFatos fatos = dao.listar().get(position);
        holder.nomeTV.setText(fatos.getNome());
        holder.dataTV.setText(fatos.getData());
        holder.gravidadeTV.setText(fatos.getGravidade());
        holder.acoesTV.setText(fatos.getAcoes());
        holder.planejamentosTV.setText(fatos.getPlanejamento());

        Log.i("FatosAdapter", "Associados: " + associadosCount++);
    }

    @Override
    public int getItemCount()
    {
        return dao.listar().size();
    }
}




