package Lenguajes.Java.semana3.Herencia;

public class Cuadrado extends Figura {
	float lado;

	public Cuadrado(float lado) {
		this.lado = lado;
	}

	@Override
	public float calcularArea() {
		this.setArea(lado * lado);
		System.out.println("El area del cuadrado es" + this.getArea());
		return this.getArea();
	}
}
