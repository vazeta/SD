import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class SerialMergeSort {

    List<String> palavras = new ArrayList<>();

    public static void merge(List<String> palavras) {
        if(palavras.size() < 2) return;
        int meio= palavras.size()/2;
        List<String> esq= new ArrayList<>(palavras.subList(0,meio));
        List<String> rig = new ArrayList<>(palavras.subList(meio + palavras.size()));
        merge(esq);
        merge(rig);
        sort(palavras,esq,rig);
        
    }
    public static void sort() {

        
        
    }


    public static void leTexto(String name){
        try {
            File f = new File(nome);
            FileReader leitor = new FileReader(f);
            BufferedReader linhas = new BufferedReader(leitor);
            String linha;
            
        } catch (FileNotFoundException ex) {
            System.out.println("Erro a abrir ficheiro.");
            System.exit(0);
        } catch (IOException ex) {
            System.out.println("Erro a ler ficheiro.");
            System.exit(0);
        }
            
    }
    public static void main(String[] args) {
        leTexto("words.txt");
        
        
    }

    
}
