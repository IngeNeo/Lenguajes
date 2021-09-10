package Lenguajes.Java.semana3.UMLCLASESobreCarga;

public class Bicicleta {
	// instance variables - replace the example below with your own
	private String marca;
	private String color;
	private int velocidadMax;
	private int rin;

	public Bicicleta() {
		this.marca = "GW";
		this.color = "Gris";
		this.velocidadMax = 100;
		this.rin = 16;
	}

	public Bicicleta(int velocidadMax, int rin) {
		this.marca = "GW";
		this.color = "Gris";
		this.velocidadMax = velocidadMax;
		this.rin = rin;
	}

	public Bicicleta(int velocidadMax, int rin, String color) {
		this.marca = "GW";
		this.color = color;
		this.velocidadMax = velocidadMax;
		this.rin = rin;
	}

	public String getMarca() {
		return this.marca;
	}

	public String getColor() {
		return this.color;
	}

	public int getVelocidadMax() {
		return this.velocidadMax;
	}

	public int getRin() {
		return this.rin;
	}

	public void setMarca(String marca) {
		this.marca = marca;
	}

	public void setColor(String color) {
		this.color = color;
	}

	public void setVelocidadMax(int velocidadMax) {
		this.velocidadMax = velocidadMax;
	}

	public void setRin(int rin) {
		this.rin = rin;
	}

}
