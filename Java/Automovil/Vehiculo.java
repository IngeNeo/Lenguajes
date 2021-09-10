package Lenguajes.Java.Automovil;

public abstract class Vehiculo {

	// Inserte acá los atributos
	private String nombreConductor;
	private int nPasajeros = 0;
	private int nMaximoPasajeros;
	private double cantidadDinero = 0;
	private double localizacionX = 0;
	private double localizacionY = 0;
	private boolean aireAcondicionadoActivado = false;
	private boolean motorEncendido = false;
	private boolean wifiEncendido = false;
	private boolean enMarcha = false;

	// Inserte acá el método constructor
	public Vehiculo(String nombreConductor) {
		this.nMaximoPasajeros = 1;
		this.nombreConductor = nombreConductor;
	}

	public Vehiculo(String nombreConductor, int nMaximoPasajeros) {
		this.nombreConductor = nombreConductor;
		this.nMaximoPasajeros = nMaximoPasajeros;
	}
	// Inserte acá los métodos (NO LOS GETTER Y SETTERS)

	public void dejarPasajero() {
		if (this.enMarcha == false) {
			this.nPasajeros -= 1;
		}
	}

	public double calcularDistanciaAcopio() {
		double distancia = 0;
		double valor = (Math.pow(this.localizacionX, 2)) + (Math.pow(this.localizacionY, 2));
		distancia = (Math.sqrt((valor)));
		return distancia;
	}

	public void gestionarAireAcondicionado() {
		if (this.aireAcondicionadoActivado == true) {
			this.aireAcondicionadoActivado = false;
		} else if (this.aireAcondicionadoActivado == false && this.motorEncendido == true) {
			this.aireAcondicionadoActivado = true;
		}
	}

	public void gestionarMotor() {
		if (this.motorEncendido == true) {
			this.motorEncendido = false;
			this.aireAcondicionadoActivado = false;
			this.wifiEncendido = false;
			this.enMarcha = false;
		} else {
			this.motorEncendido = true;
		}
	}

	public void gestionarWifi() {
		if (this.wifiEncendido) {
			this.wifiEncendido = false;
		} else if (this.wifiEncendido == false && this.motorEncendido == true) {
			this.wifiEncendido = true;
		}
	}

	public abstract void gestionarMarcha();

	public void moverDerecha(double d) {
		if (this.motorEncendido == true && this.enMarcha == true)
			this.localizacionX += d;
	}

	public void moverIzquierda(double d) {
		if (this.motorEncendido == true && this.enMarcha == true) {
			this.localizacionX -= d;
		}
	}

	public void moverArriba(double d) {
		if (this.motorEncendido == true && this.enMarcha == true) {
			this.localizacionY += d;
		}
	}

	public void moverAbajo(double d) {
		if (this.motorEncendido == true && this.enMarcha == true) {
			this.localizacionY -= d;
		}
	}

	// Inserte acá los SETTERS Y GETTERS
	public void setNombreConductor(String nombreConductor) {
		this.nombreConductor = nombreConductor;
	}

	public String getNombreConductor() {
		return this.nombreConductor;
	}

	public void setnPasajeros(int nPasajeros) {
		this.nPasajeros = nPasajeros;
	}

	public int getnPasajeros() {
		return this.nPasajeros;
	}

	public void setnMaximoPasajeros(int nMaximoPasajeros) {
		this.nMaximoPasajeros = nMaximoPasajeros;
	}

	public int getnMaximoPasajeros() {
		return this.nMaximoPasajeros;
	}

	public void setCantidadDinero(double cantidadDinero) {
		this.cantidadDinero = cantidadDinero;
	}

	public double getCantidadDinero() {
		return this.cantidadDinero;
	}

	public void setLocalizacionX(double localizacionX) {
		this.localizacionX = localizacionX;
	}

	public double getLocalizacionX() {
		return this.localizacionX;
	}

	public void setLocalizacionY(double localizacionY) {
		this.localizacionY = localizacionY;
	}

	public double getLocalizacionY() {
		return this.localizacionY;
	}

	public void setAireAcondicionadoActivado(boolean aireAcondicionadoActivado) {
		this.aireAcondicionadoActivado = aireAcondicionadoActivado;
	}

	public boolean isAireAcondicionadoActivado() {
		return this.aireAcondicionadoActivado;
	}

	public void setMotorEncendido(boolean motorEncendido) {
		this.motorEncendido = motorEncendido;
	}

	public boolean isMotorEncendido() {
		return this.motorEncendido;
	}

	public void setWifiEncendido(boolean wifiEncendido) {
		this.wifiEncendido = wifiEncendido;
	}

	public boolean isWifiEncendido() {
		return this.wifiEncendido;
	}

	public void setEnMarcha(boolean enMarcha) {
		this.enMarcha = enMarcha;
	}

	public boolean isEnMarcha() {
		return this.enMarcha;
	}
}