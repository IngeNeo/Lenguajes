package Lenguajes.Java.semana3.Herencia;

public class Circulo extends Figura {
	float pi = 3.14f;
	float radio;

	public Circulo(float radio) {
		this.radio = radio;
	}

	public void setRadio(int radio) {
		this.radio = radio;
	}

	public float getRadio() {
		return this.radio;
	}

	@Override
	public float calcularArea() {
		this.setArea(pi * (radio * radio));
		System.out.println("El area del circulo es" + this.getArea());
		return this.getArea();
	}
}
