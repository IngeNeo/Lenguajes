package Lenguajes.Java.Banco;

public class CuentaAhorro extends CuentaBanco {

	// Inserte acá el método constructor
	public CuentaAhorro(String numeroCuenta, String nombrePropietario, double saldo) {
		super(numeroCuenta, nombrePropietario, saldo);
	}

	// Inserte acá los métodos (NO LOS GETTER Y SETTERS)

	public double getIEA() {
		double interes = 0.0;
		if (this.getSaldo() < 1000000) {
			interes = this.getSaldo() * 0.01;
		} else if (this.getSaldo() >= 1000000 && this.getSaldo() < 2000000) {
			interes = this.getSaldo() * 0.0175;
		} else if (this.getSaldo() >= 2000000) {
			interes = this.getSaldo() * 0.023;
		}
		return interes;
	}

	public void pagarInteres(int dias) {
		if (dias >= 1) {
			double pagar = 0;
			pagar = this.getSaldo() * (1 + (this.getIEA() / 365));
			pagar = this.getSaldo() + (dias * pagar);
			this.setSaldo(pagar);
		}
	}
}
