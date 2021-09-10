package Lenguajes.Java.Clase7.UMLCLASE;

public class Avion extends Vehiculo {
	private double altitud;
	private Aeropuerto aeropuerto;

	/**
	 * Constructor for objects of class Avion
	 */
	public Avion(Aeropuerto aeropuerto) {
		this.aeropuerto = aeropuerto;
		this.altitud = 0;
	}

	public Aeropuerto getAeropuerto() {
		return this.aeropuerto;
	}

	public double asceder() {
		System.out.println("velocidad cambio a " + this.acelerar(100.0f));
		this.altitud += 100.0;
		return this.altitud;
	}

	public double desceder() {
		System.out.println("velocidad cambio a " + this.frenar(10.0f));
		this.altitud -= 10.0;
		return this.altitud;
	}

}
