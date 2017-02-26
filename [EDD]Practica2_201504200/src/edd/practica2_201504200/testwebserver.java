/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package edd.practica2_201504200;
import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;
import com.squareup.okhttp.Response;

import java.net.MalformedURLException;
import java.net.URL;
import java.util.logging.Level;

/**
 *
 * @author Dénilson Argueta
 */
public class testwebserver {
    public static OkHttpClient webClient = new OkHttpClient();
    
    public testwebserver()
    {
    }
    
    public static void nombre()
    {
         String nombre = "Marco";
        RequestBody formBody = new FormEncodingBuilder()
                .add("dato", nombre)
                .add("dato2", "4")
                .build();
        String r = getString("metodoWeb", formBody); 
        System.out.println(r + "---");
    }
    
    public static void insertarlista(String dato)
    {
        RequestBody formBody = new FormEncodingBuilder()
                .add("dato",dato)
                .build();
        getString("insertarLista", formBody);
    }
    public static void buscarlista(String palabra)
    {
        RequestBody formBody = new FormEncodingBuilder()
                .add("dato",palabra)
                .build();
        String r = getString("buscarLista", formBody); 
        System.out.println(r +"");
    }
    public static void eliminarlista(String indice)
    {
        RequestBody formBody = new FormEncodingBuilder()
                .add("dato",indice)
                .build();
        getString("eliminarLista", formBody); 
    }
    //ESTOS METODOS SON DE LA COLA
    public static void agregarCola(String palabra)
    {
        RequestBody formBody = new FormEncodingBuilder()
                .add("dato",palabra)
                .build();
        getString("agregarCola", formBody); 
    }
    public static void sacarCola()
    {
        RequestBody formBody = new FormEncodingBuilder()
                .add("dato", "aqui")
                .build();
        String r = getString("sacarCola", formBody);      
        System.out.println(r +"");
    }
    //ESTOS METODOS SON DE LA PILA
    public static void agregarPila(String palabra)
    {
        RequestBody formBody = new FormEncodingBuilder()
                .add("dato",palabra)
                .build();
        getString("agregarPila", formBody); 
    }
    public static void sacarPila()
    {
        RequestBody formBody = new FormEncodingBuilder()
                .add("dato", "aqui")
                .build();
        String r = getString("sacarPila", formBody);      
        System.out.println(r +"");
    }
 
     public static String getString(String metodo, RequestBody formBody) {

        try {
            URL url = new URL("http://0.0.0.0:5000/" + metodo);
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response response = webClient.newCall(request).execute();//Aqui obtiene la respuesta en dado caso si hayas pues un return en python
            String response_string = response.body().string();//y este seria el string de las respuesta
            return response_string;
        } catch (MalformedURLException ex) {
            java.util.logging.Logger.getLogger(testwebserver.class.getName()).log(Level.SEVERE, null, ex);
        } catch (Exception ex) {
            java.util.logging.Logger.getLogger(testwebserver.class.getName()).log(Level.SEVERE, null, ex);
        }
        return null;
    }
    
}
