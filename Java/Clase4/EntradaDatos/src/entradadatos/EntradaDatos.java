package Lenguajes.Java.Clase4.EntradaDatos.src.entradadatos;

import java.util.Scanner;

public class EntradaDatos {

	public static void main(String[] args) {

		Scanner lectura = new Scanner(System.in);
		System.out.println("Ingrese datos Cadena: ");
		String cadena = lectura.nextLine();
		System.out.println("Ingreso cadena: " + cadena);

		System.out.println("Ingrese Hola Mundo: ");
		cadena = lectura.nextLine();
		String holamundojava = "Hola Mundo";
		String holamundojava2 = "Hola Mundo";
		// Con los dos string sin ser objeto.
		System.out.println(holamundojava + " == " + holamundojava2 + " : " + (holamundojava == holamundojava2));
		// Con los dos string con el equals
		System.out.println(holamundojava + " equals " + holamundojava2 + " : " + holamundojava.equals(holamundojava2));
		// Con un dato ingresado
		System.out.println(cadena + " == " + holamundojava2 + " : " + (cadena == holamundojava2));
		// Con un dato ingresado equals
		System.out.println(cadena + " == " + holamundojava2 + " : " + cadena.equals(holamundojava2));

		System.out.println("Ingrese dato entero: ");
		int entero = lectura.nextInt();
		System.out.println("Ingreso Entero: " + entero);
		System.out.println("Ingrese un decimal (,): ");
		float decimal = lectura.nextFloat();
		System.out.println("Ingreso un decimal: " + decimal);
		lectura.close();
	}
}
