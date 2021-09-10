package Lenguajes.Java.Clase4.EntradaDatos.src.entradadatos;

import java.util.Scanner;

public class Ciclo {

	public static void main(String[] args) {

		Scanner lectura = new Scanner(System.in);
		int multiplo = lectura.nextInt();
		int repeticiones = lectura.nextInt();

		int multiplicador = 0;
		System.out.println("Tabla de multiplicar de :" + multiplo);
		while (multiplicador <= repeticiones) {
			System.out.println(multiplo + " * " + multiplicador + " = " + multiplo * multiplicador);
			multiplicador++;
		}

		System.out.println("Ingrese un dato:");
		int dato = lectura.nextInt();
		while (dato != 0) {
			System.out.println("El dato es diferente a 0 : " + dato);
			dato = lectura.nextInt();
		}
		System.out.println("El dato ingresado fue 0 : " + dato);
		lectura.close();
	}

}
