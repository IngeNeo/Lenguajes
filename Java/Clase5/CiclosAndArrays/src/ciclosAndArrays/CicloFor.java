package Lenguajes.Java.Clase5.CiclosAndArrays.src.ciclosAndArrays;

import java.util.Scanner;

public class CicloFor {

	public static void main(String[] args) {
		/*
		 * int i = 0; while (i<10){ System.out.println(i); i++; }
		 */
		Scanner lectura = new Scanner(System.in);
		System.out.println("Cuantas personas va a encuestar?: ");
		float personasEncuestada = lectura.nextInt();
		lectura.nextLine();
		float si = 0;
		float no = 0;
		for (float personas = 1; personas <= personasEncuestada; personas++) {
			System.out.println("Persona: " + personas + " Estas de acuerdo con la vacuna del covid? (s/n)");
			String respuesta = lectura.nextLine();
			if (respuesta.equalsIgnoreCase("s")) {
				si++;
			} else {
				no++;
			}
		}
		System.out.println("Total personas encuestadas: " + personasEncuestada);
		System.out.println("Personas que dijeron que si: " + si);
		System.out.println("Personas que dijeron que no: " + no);
		float siPorcentaje = si / personasEncuestada;
		float noPorcentaje = no / personasEncuestada;
		System.out.println("Personas que sijeron que si: %.2f " + (siPorcentaje * 100) + "%");
		System.out.println("Personas que sijeron que no: %.2f " + (noPorcentaje * 100) + "%");
		lectura.close();
	}
}
