package Lenguajes.Java.Restaurante;

public class Pedido {

	private String nPedido;
	private String IDCliente;
	private double costoPedido;
	private int diasPedido;
	private int mesPedido;
	private int yearPedido;

	public Pedido(String nPedido, String IDCliente, double costoPedido, int diasPedido, int mesPedido, int yearPedido) {
		this.nPedido = nPedido;
		this.IDCliente = IDCliente;
		this.costoPedido = costoPedido;
		this.diasPedido = diasPedido;
		this.mesPedido = mesPedido;
		this.yearPedido = yearPedido;
	}

	public void setnPedido(String nPedido) {
		this.nPedido = nPedido;
	}

	public String getnPedido() {
		return this.nPedido;
	}

	public void setIDCliente(String IDCliente) {
		this.IDCliente = IDCliente;
	}

	public String getIDCliente() {
		return this.IDCliente;
	}

	public void setCostoPedido(double costoPedido) {
		this.costoPedido = costoPedido;
	}

	public double getCostoPedido() {
		return this.costoPedido;
	}

	public void setDiasPedido(int diasPedido) {
		this.diasPedido = diasPedido;
	}

	public int getDiasPedido() {
		return this.diasPedido;
	}

	public void setMesPedido(int mesPedido) {
		this.mesPedido = mesPedido;
	}

	public int getMesPedido() {
		return this.mesPedido;
	}

	public void setYearPedido(int yearPedido) {
		this.yearPedido = yearPedido;
	}

	public int getYearPedido() {
		return this.yearPedido;
	}

}
