package Lenguajes.Java.semana3.Herencia;

public class Herencia {
	public static void main(String[] args) {
		Figura circulo = new Circulo(12.0f);
		circulo.calcularArea();

		Figura cuadrado = new Cuadrado(12.0f);
		cuadrado.calcularArea();

	}
}
