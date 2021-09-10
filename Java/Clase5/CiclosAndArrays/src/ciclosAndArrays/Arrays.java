package Lenguajes.Java.Clase5.CiclosAndArrays.src.ciclosAndArrays;

import java.util.Scanner;

public class Arrays {

	public static void main(String[] args) {
		// 0,1,2,3,4
		/*
		 * int[] enteroInicializado = {15,24,38,41,52}; int indice = 0;
		 * System.out.println(enteroInicializado[indice]);
		 * System.out.println(enteroInicializado[1]);
		 * System.out.println(enteroInicializado[2]);
		 * System.out.println(enteroInicializado[3]);
		 * System.out.println(enteroInicializado[4]);
		 */

		/*
		 * int[] entero = new int[5]; entero[0]=56; entero[1]=6; entero[2]=41;
		 * entero[3]=5; entero[4]=8; //entero[5]=9;
		 *
		 * System.out.println(entero[0]); System.out.println(entero[1]);
		 * System.out.println(entero[2]); System.out.println(entero[3]);
		 * System.out.println(entero[4]); System.out.println(entero.length);
		 */

		/*
		 * String[] cadena = new String[5]; cadena[0]="hola mundo";
		 */

		/*
		 * String[] cadenas = new String[25]; for(int indice = 0;
		 * indice<cadenas.length;indice+=2){ cadenas[indice] = "Hola mundo #"+indice;
		 * System.out.println("posicion #"+ indice+ " -> "+cadenas[indice]); }
		 * System.out.println(cadenas[1]);
		 *
		 * int[] entero = new int[25]; for(int indice = 0;
		 * indice<cadenas.length;indice+=2){ entero[indice] = indice;
		 * System.out.println("posicion #"+ indice+ " -> "+entero[indice]); }
		 * System.out.println(entero[1]);
		 */

		// Mostrar la tirilla de productos de clientes que ingresa
		// producto -> precio
		// Total -> valor
		Scanner lectura = new Scanner(System.in);
		System.out.println("Bienvenido, cuantos productos compro hoy? ");
		int productos = lectura.nextInt();
		lectura.nextLine();

		String[] nombreProductos = new String[productos];
		int[] valorProductos = new int[productos];

		for (int indice = 0; indice < productos; indice++) {
			System.out.println("Ingrese el nombre del producto # " + (indice + 1));
			nombreProductos[indice] = lectura.nextLine();
			System.out.println("Ingrese el valor del producto #" + (indice + 1));
			valorProductos[indice] = lectura.nextInt();
			lectura.nextLine();
		}

		// Tirilla
		System.out.println("Su compra fue la siguiente: ");
		int totalFactura = 0;
		/*
		 * for(int indice2= 0; indice2 < nombreProductos.length; indice2++){
		 * System.out.println("Producto "+ nombreProductos[indice2]+
		 * " Valor: "+valorProductos[indice2]); totalFactura+=valorProductos[indice2]; }
		 */

		for (int indice2 = nombreProductos.length - 1; indice2 >= 0; indice2--) {
			System.out.println("Producto " + nombreProductos[indice2] + " Valor: " + valorProductos[indice2]);
			totalFactura += valorProductos[indice2];
		}

		System.out.println("Total Fue: " + totalFactura);
		lectura.close();

	}
}
