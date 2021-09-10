package Lenguajes.Java.semana3.UMLCLASESobreCarga;

public class SobreCarga {
	public static void main(String[] args) {

		Bicicleta miPrimeraBicicleta = new Bicicleta();
		calidad(miPrimeraBicicleta);
		System.out.println("Nueva Coleccion");
		Bicicleta nuevaBicicleta = new Bicicleta(30, 12);
		calidad(nuevaBicicleta);
		Bicicleta nuevaBicicleta2 = new Bicicleta(40, 15);
		calidad(nuevaBicicleta2);

		System.out.println("Nueva Coleccion");

		Bicicleta nuevaBicicleta3 = new Bicicleta(10, 5, "Verde");
		calidad(nuevaBicicleta3);

		Bicicleta nuevaBicicleta4 = new Bicicleta(10, 5, "Amarillo");
		calidad(nuevaBicicleta4);

		Bicicleta nuevaBicicleta5 = new Bicicleta(10, 5, "Rojo");
		calidad(nuevaBicicleta5);

		System.out.println("Modificacion");
		miPrimeraBicicleta.setColor("Verde");
		miPrimeraBicicleta.setVelocidadMax(50);
		miPrimeraBicicleta.setRin(12);

		calidad(miPrimeraBicicleta);

	}

	public static void calidad(Bicicleta miPrimeraBicicleta) {
		System.out.println(miPrimeraBicicleta.getMarca());
		System.out.println(miPrimeraBicicleta.getRin());
		System.out.println(miPrimeraBicicleta.getColor());
		System.out.println(miPrimeraBicicleta.getVelocidadMax());
	}
}
