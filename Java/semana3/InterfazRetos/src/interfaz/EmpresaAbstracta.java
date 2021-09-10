package Lenguajes.Java.semana3.InterfazRetos.src.interfaz;

public class EmpresaAbstracta {
	private int valorTotal = 0;
	public boolean online = false;

	public void comprarProducto(int valor) {
		if (this.online) {
			this.valorTotal += valor;
		}
	}

	public double calcularTotal(double descuento) {
		if (this.online) {
			double descuentoCalculado = this.valorTotal * descuento;
			return this.valorTotal - descuentoCalculado;
		} else {
			return 0;
		}
	}
}
