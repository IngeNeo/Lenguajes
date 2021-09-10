package Lenguajes.Java.Automovil;

public class Taxi extends Vehiculo {

	// Inserte acá los atributos
	private double distanciaRecorrida = 0;
	private boolean segurosActivados = false;

	// Inserte acá el método constructor
	public Taxi(String nombreConductor) {
		super(nombreConductor);
	}

	// Inserte acá los métodos (NO LOS GETTER Y SETTERS)
	public void gestionarMarcha() {
		if (this.isEnMarcha() == true) {
			this.setEnMarcha(false);
		} else if (this.getnPasajeros() > 0) {
			if (this.isEnMarcha() == false && this.segurosActivados == true) {
				this.setEnMarcha(true);
			}
		}
	}

	public void reiniciarTaximetro() {
		this.distanciaRecorrida = 0;
	}

	public void presionarBotonPanico() {
		this.setEnMarcha(false);
		this.segurosActivados = false;
		reiniciarTaximetro();
	}

	@Override
	public void moverDerecha(double d) {
		if (this.isEnMarcha() == true) {
			if (this.getnPasajeros() > 0) {
				this.setDistanciaRecorrida(this.getDistanciaRecorrida() + d);
			}
			this.setLocalizacionX(this.getLocalizacionX() + d);
		}
	}

	@Override
	public void moverIzquierda(double d) {
		if (this.isEnMarcha() == true) {
			if (this.getnPasajeros() > 0) {
				this.setDistanciaRecorrida(this.getDistanciaRecorrida() + d);
			}
			this.setLocalizacionX(this.getLocalizacionX() - d);
		}
	}

	@Override
	public void moverArriba(double d) {
		if (this.isEnMarcha() == true) {
			if (this.getnPasajeros() > 0) {
				this.setDistanciaRecorrida(this.getDistanciaRecorrida() + d);
			}
			this.setLocalizacionY(this.getLocalizacionY() + d);
		}
	}

	@Override
	public void moverAbajo(double d) {
		if (this.isEnMarcha() == true) {
			if (this.getnPasajeros() > 0) {
				this.setDistanciaRecorrida(this.getDistanciaRecorrida() + d);
			}
			this.setLocalizacionY(this.getLocalizacionY() - d);
		}
	}

	public double calcularPasaje() {
		double pasaje = 0;
		if (this.distanciaRecorrida != 0) {
			pasaje = 3000 + (2300 * this.distanciaRecorrida);
		}
		return pasaje;
	}

	public void gestionarSeguros() {
		if (this.isEnMarcha() == false && this.segurosActivados == true) {
			this.segurosActivados = false;
		} else if (this.isEnMarcha() == false && this.segurosActivados == false) {
			this.segurosActivados = true;
		}
	}

	@Override
	public void dejarPasajero() {
		if (this.getnPasajeros() == 1 && this.segurosActivados == false) {
			this.setnPasajeros(this.getnPasajeros() - 1);
			this.setCantidadDinero(this.getCantidadDinero() + this.calcularPasaje());
			reiniciarTaximetro();
		}
	}

	public void recogerPasajero() {
		if (this.getnPasajeros() == 0) {
			this.setnPasajeros(this.getnPasajeros() + 1);
		}
	}

	// Inserte acá los SETTERS Y GETTERS
	public void setDistanciaRecorrida(double distanciaRecorrida) {
		this.distanciaRecorrida = distanciaRecorrida;
	}

	public double getDistanciaRecorrida() {
		return this.distanciaRecorrida;
	}

	public void setSegurosActivados(boolean segurosActivados) {
		this.segurosActivados = segurosActivados;
	}

	public boolean isSegurosActivados() {
		return this.segurosActivados;
	}

}