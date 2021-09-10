package Lenguajes.Java.Clase7.UMLCLASE;

public class Uml {

	public static void main(String[] args) {
		Aeropuerto aero = new Aeropuerto("Bogota");
		System.out.println(aero.getCiudad());
		aero.setCiudad("Medellin");
		System.out.println(aero.getCiudad());

		Avion avion = new Avion(aero);

		System.out.println("Avion ascendera con altitud " + avion.asceder());
		System.out.println("Avion ascendera con altitud " + avion.asceder());
		System.out.println("Avion ascendera con altitud " + avion.asceder());

		System.out.println("Avion descedera con altitud " + avion.desceder());
	}
}
