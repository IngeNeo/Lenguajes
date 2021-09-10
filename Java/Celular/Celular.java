package Lenguajes.Java.Celular;

public class Celular {

	public static void main(String[] args) {

	}

	public class SIMCard {

		// Inserte acá los atributos
		private String empresaTelefonia = "HI";
		private double saldo = 0;
		private String numeroTelefono;
		private boolean celularApagado = true;
		private boolean modoAvionActivado = false;
		private boolean datosActivados = false;
		private int saldoDatos = 0;

		// Inserte acá el método constructor
		public SIMCard(String numeroTelefono) {
			this.numeroTelefono = numeroTelefono;
		}

		// Inserte acá los métodos (NO LOS GETTER Y SETTERS)
		public void comprarDatos(int c) {
			int pagar = 0;
			int cantidad = 0;
			if (c < 10) {
				pagar = (c * 3000);
			} else if (c > 10 && c < 30) {
				cantidad = c - 10;
				pagar = (10 * 3000);
				pagar = pagar + (cantidad * 2500);
			} else if (c > 30) {
				cantidad = c - 20;
				pagar = (20 * 3000);
				pagar = pagar + (cantidad * 1500);
			}
			if (this.saldo >= pagar) {
				this.saldoDatos = c;
				this.saldo -= pagar;
			}
		}

		public void consumirDatos(int c) {
			if (this.datosActivados == true) {
				if (c <= this.saldoDatos) {
					this.saldoDatos -= c;
				}
			}
		}

		public void llamar(int s) {
			float pagar = 0;
			int cantidad = 0;
			if (this.modoAvionActivado != true || this.celularApagado != true) {
				if (s < 60) {
					pagar = (s * 1);
				} else if (s > 60) {
					cantidad = s - 60;
					pagar = (60 * 1);
					pagar = pagar + (cantidad * 0.5f);
				}
				if (this.saldo >= pagar) {
					this.saldo -= pagar;
				}
			}
		}

		public void recargarSaldo(double s) {
			this.saldo += s;
		}

		public void gestionarEncendidoCelular() {
			if (this.celularApagado == false) {
				this.celularApagado = true;
				this.datosActivados = false;
				this.modoAvionActivado = false;
			} else {
				this.celularApagado = false;
				this.datosActivados = false;
				this.modoAvionActivado = false;
			}
		}

		public void gestionarModoAvion() {
			if (this.celularApagado == false) {
				if (this.modoAvionActivado == false) {
					if (this.datosActivados == true) {
						this.datosActivados = false;
					}
					this.modoAvionActivado = true;
				} else {
					this.modoAvionActivado = false;
				}
			}
		}

		public void gestionarDatos() {
			if (this.celularApagado == false) {
				if (this.modoAvionActivado == false) {
					if (this.datosActivados == true) {
						this.datosActivados = false;
					} else {
						this.datosActivados = true;
					}
				}
			}
		}

		// Inserte acá los SETTERS Y GETTERS
		public String getEmpresaTelefonia() {
			return empresaTelefonia;
		}

		public void setEmpresaTelefonia(String empresaTelefonia) {
			this.empresaTelefonia = empresaTelefonia;
		}

		public double getSaldo() {
			return saldo;
		}

		public void setSaldo(double saldo) {
			this.saldo = saldo;
		}

		public String getNumeroTelefono() {
			return numeroTelefono;
		}

		public void setNumeroTelefono(String numeroTelefono) {
			this.numeroTelefono = numeroTelefono;
		}

		public boolean isCelularApagado() {
			return celularApagado;
		}

		public void setCelularApagado(boolean celularApagado) {
			this.celularApagado = celularApagado;
		}

		public boolean isModoAvionActivado() {
			return modoAvionActivado;
		}

		public void setModoAvionActivado(boolean modoAvionActivado) {
			this.modoAvionActivado = modoAvionActivado;
		}

		public boolean isDatosActivados() {
			return datosActivados;
		}

		public void setDatosActivados(boolean datosActivados) {
			this.datosActivados = datosActivados;
		}

		public int getSaldoDatos() {
			return saldoDatos;
		}

		public void setSaldoDatos(int saldoDatos) {
			this.saldoDatos = saldoDatos;
		}
	}
}