package Lenguajes.Java.Banco;

public class CuentaBanco {

	// Inserte acá los atributos
	private String numeroCuenta;
	private String nombrePropietario;
	private double saldo;

	// Inserte acá el método constructor
	public CuentaBanco(String numeroCuenta, String nombrePropietario, double saldo) {
		this.numeroCuenta = numeroCuenta;
		this.nombrePropietario = nombrePropietario;
		this.saldo = saldo;
	}

	// Inserte acá los SETTERS Y GETTERS
	public void setNumeroCuenta(String numeroCuenta) {
		this.numeroCuenta = numeroCuenta;
	}

	public String getNumeroCuenta() {
		return this.numeroCuenta;
	}

	public void setNomberPropietario(String nombrePropietario) {
		this.nombrePropietario = nombrePropietario;
	}

	public String getNombrePropietario() {
		return this.nombrePropietario;
	}

	public void setSaldo(double saldo) {
		this.saldo = saldo;
	}

	public double getSaldo() {
		return this.saldo;
	}

	// Inserte acá los métodos (NO LOS GETTER Y SETTERS)

	public void depositar(double c) {
		this.saldo += c;
	}

	public void retirar(double c) {

		double retiro = (c + (c * 0.05));
		if (this.saldo >= retiro) {
			this.saldo -= retiro;
		}
	}
}
