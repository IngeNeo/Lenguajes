package Lenguajes.Java.Automovil;

public class Autobus extends Vehiculo {

	// Inserte acá los atributos
	private boolean puertaAbierta = false;

	// Inserte acá el método constructor
	public Autobus(String nombreConductor, int nMaximoPasajeros) {
		super(nombreConductor, nMaximoPasajeros);
	}

	// Inserte acá los métodos (NO LOS GETTER Y SETTERS)
	public void recogerPasajero(int estrato) {
		if (this.getnMaximoPasajeros() > this.getnPasajeros()) {
			if (this.isEnMarcha() == false && this.puertaAbierta == true) {
				this.setCantidadDinero(this.getCantidadDinero() + calcularPasaje(estrato));
				this.setnPasajeros(this.getnPasajeros() + 1);
			}
		}
	}

	public void gestionarPuerta() {
		if (this.puertaAbierta == true) {
			this.puertaAbierta = false;
		} else if (this.puertaAbierta == false && this.isEnMarcha() == false) {
			this.puertaAbierta = true;
		}
	}

	public void gestionarMarcha() {
		if (this.isEnMarcha() == true && this.isMotorEncendido() == true) {
			this.setEnMarcha(false);
		} else if (this.isEnMarcha() == false && this.isMotorEncendido() == true && this.puertaAbierta == false) {
			this.setEnMarcha(true);
		}
	}

	public static double calcularPasaje(int estrato) {
		double pasaje = 0;
		switch (estrato) {
			case 0:
			case 1:
			case 2:
				pasaje = 1500;
				break;
			case 3:
			case 4:
				pasaje = 2600;
				break;
			case 5:
			case 6:
				pasaje = 3000;
				break;
		}
		return pasaje;
	}

	// Inserte acá los SETTERS Y GETTERS
	public void setPuertaAbierta(boolean puertaAbierta) {
		this.puertaAbierta = puertaAbierta;
	}

	public boolean isPuertaAbierta() {
		return this.puertaAbierta;
	}

}