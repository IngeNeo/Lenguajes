package Lenguajes.Java.semana3.Adopcion;

public class Adopcion {
	public static void main(String[] args) {
		/*
		 * Perro perro1 = new Perro("Kondor");
		 *
		 * perro1.comer(); perro1.caminar(); perro1.sonido();
		 *
		 * Gato gato1 = new Gato("Miringo");
		 *
		 * gato1.comer(); gato1.caminar(); gato1.sonido();
		 *
		 * Pez pez1 = new Pez("Nemo"); pez1.comer(); pez1.caminar(); pez1.sonido();
		 */

		Animal pollo = new Pollo("Claudio");
		pollo.comer();
		pollo.caminar();
		pollo.sonido();

		Animal pollo1 = new Pollo1("Kirilei");
		pollo1.comer();
		pollo1.caminar();
		pollo1.sonido();

		Animal pollo2 = new Pollo2("Patricio");
		pollo2.comer();
		pollo2.caminar();
		pollo2.sonido();

		Hamster hamster1 = new Hamster("Jimmy");
		hamster1.comer();
		hamster1.caminar();
		hamster1.sonido();

	}
}
