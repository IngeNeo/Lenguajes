package Lenguajes.Java.semana3.Herencia;

public abstract class Figura {
	private float area;

	public abstract float calcularArea();

	public void setArea(float area) {
		this.area = area;
	}

	public float getArea() {
		return this.area;
	}

}
