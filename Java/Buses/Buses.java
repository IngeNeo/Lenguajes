package Lenguajes.Java.Buses;

public class Buses {

	public static void main(String args[]) {

	}

	public class Autobus {
		// Inserte acá los atributos
		private String nombreConductor;
		private int nPasajeros = 0;
		private double cantidadDinero = 0;
		private int nMaximoPasajeros;
		private double localizacionX = 0;
		private double localizacionY = 0;
		private boolean puertaAbierta;
		private boolean aireAcondicionadoActivado = false;
		private boolean motorEncendido = false;
		private boolean wifiEncendido = false;
		private boolean enMarcha = false;

		// Inserte acá el método constructor
		public Autobus(String nombreConductor, int nMaximoPasajeros, boolean puertaAbierta) {
			this.nombreConductor = nombreConductor;
			this.puertaAbierta = puertaAbierta;
			this.nMaximoPasajeros = nMaximoPasajeros;
		}

		// Inserte acá los métodos (NO LOS GETTER Y SETTERS)

		public void recogerPasajero(int estrato) {
			if (this.nMaximoPasajeros > this.nPasajeros) {
				if (this.enMarcha == false && this.puertaAbierta == true) {
					switch (estrato) {
						case 0:
						case 1:
						case 2:
							this.cantidadDinero += 1500;
							break;
						case 3:
						case 4:
							this.cantidadDinero += 2600;
							break;
						case 5:
						case 6:
							this.cantidadDinero += 3000;
							break;
					}
					this.nPasajeros += 1;
				}
			}
		}

		public void dejarPasajero() {
			if (this.enMarcha == false && this.puertaAbierta == true) {
				this.nPasajeros -= 1;
			}
		}

		public double calcularDistanciaAcopio() {
			double distancia = 0;
			double valor = (Math.pow(this.localizacionX, 2)) + (Math.pow(this.localizacionY, 2));
			distancia = (Math.sqrt((valor)));
			return distancia;
		}

		public void gestionarPuerta() {
			if (this.puertaAbierta == true && this.enMarcha == false) {
				this.puertaAbierta = false;
			} else if (this.puertaAbierta == false && this.enMarcha == false) {
				this.puertaAbierta = true;
			}
		}

		public void gestionarAireAcondicionado() {
			if (this.aireAcondicionadoActivado) {
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

		public void gestionarMarcha() {
			if (this.enMarcha == true && this.motorEncendido == true) {
				this.enMarcha = false;
			} else if (this.enMarcha == false && this.motorEncendido == true && this.puertaAbierta == false) {
				this.enMarcha = true;
			}
		}

		public void moverDerecha(double d) {
			if (this.puertaAbierta == false && this.motorEncendido == true) {
				this.localizacionX += d;
			}
		}

		public void moverIzquierda(double d) {
			if (this.puertaAbierta == false && this.motorEncendido == true) {
				this.localizacionX -= d;
			}
		}

		public void moverArriba(double d) {
			if (this.puertaAbierta == false && this.motorEncendido == true) {
				this.localizacionY += d;
			}
		}

		public void moverAbajo(double d) {
			if (this.puertaAbierta == false && this.motorEncendido == true) {
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

		public void setCantidadDinero(double cantidadDinero) {
			this.cantidadDinero = cantidadDinero;
		}

		public double getCantidadDinero() {
			return this.cantidadDinero;
		}

		public void setnMaximoPasajeros(int nMaximoPasajeros) {
			this.nMaximoPasajeros = nMaximoPasajeros;
		}

		public int getnMaximoPasajeros() {
			return this.nMaximoPasajeros;
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

		public void setPuertaAbierta(boolean puertaAbierta) {
			this.puertaAbierta = puertaAbierta;
		}

		public boolean isPuertaAbierta() {
			return this.puertaAbierta;
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
}