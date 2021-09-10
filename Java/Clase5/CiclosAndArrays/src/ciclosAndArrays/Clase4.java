package Lenguajes.Java.Clase5.CiclosAndArrays.src.ciclosAndArrays;

import java.util.Scanner;

public class Clase4 {

	public static void main(String[] args) {
		/*
		 * do { System.out.println("Ejecuto una vez"); } while (2 != 1);
		 */

		// Dar un descuento del 10% a los clientes que han comprado 500 mil pesos.
		Scanner lectura = new Scanner(System.in);
		String respuesta;
		int valorFactura = 0;
		do {
			System.out.println("Ingrese nombre producto: ");
			String producto = lectura.nextLine();
			System.out.println("Ingrese valor producto: ");
			int valorProducto = lectura.nextInt();
			lectura.nextLine();
			valorFactura += valorProducto;
			System.out.println("Tiene mas productos ? (s/n): ");
			respuesta = lectura.nextLine();
			System.out.println(producto);
		} while (respuesta.equalsIgnoreCase("s"));
		System.out.println("Su compra fue : " + valorFactura);
		if (valorFactura >= 500000) {
			float descuento = valorFactura * 0.1f;
			System.out.println("Se gano un descuento de :" + descuento);
			float valorTotal = valorFactura - descuento;
			System.out.println("En total compra fue de: " + valorTotal);
			lectura.close();
		}
	}
}
