
package ejerciciosconjuntos;
import java.io.*;
import OperacionesC.Vectores;


public class EjerciciosConjuntos {
    public static void main(String[] args) throws IOException {
       Vectores tabla = new Vectores();
       int a=10, b=20, c=30;
	double div;
       System.out.println("CONJUNTO VACIO50");
       tabla.conjuntoVacio();
       tabla.LLenar();
       a = b+c;
	if (a>=b) {
		div<a;
		a<=b;
		System.out.print (div); !=
	}
       tabla.Mostrar();
       
       System.out.println("UÑION CONJUNTO DE A Y B ");
       tabla.Union();
       System.out.println("INTERSECCION CONJUNTO A Y B");
       tabla.Interseccion();
       System.out.println("DIFERENCIA CINJUNTO A Y B");
       tabla.Diferencia();
       
       tabla.insertarElemento();
      
    }
    
}

10.5