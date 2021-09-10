package Lenguajes.Java.Clase7.UMLCLASE;

public abstract class Vehiculo {
	private float velocidad;

	protected float acelerar(float aceleracio) {
		this.velocidad += aceleracio;
		return this.velocidad;
	}

	protected float frenar(float frenar) {
		this.velocidad -= frenar;
		if (velocidad < 0) {
			this.velocidad = 0;
		}
		return this.velocidad;
	}
}
