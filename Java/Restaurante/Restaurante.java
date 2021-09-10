package Lenguajes.Java.Restaurante;

import java.util.ArrayList;

public class Restaurante {

	private ArrayList<Pedido> pedidos = new ArrayList<Pedido>();

	public Restaurante() {

	}

	public void agregarPedidoLista(Pedido p) {
		boolean bandera = false;
		for (int i = 0; i < pedidos.size(); i++) {
			if (pedidos.get(i).getnPedido().equals(p.getnPedido())) {
				bandera = true;
			}
		}
		if (bandera == false) {
			this.pedidos.add(p);
		}
	}

	public void eliminarPedido(String nPedido) {
		for (int i = 0; i < pedidos.size(); i++) {
			if (pedidos.get(i).getnPedido().equals(nPedido)) {
				pedidos.remove(i);
			}
		}
	}

	public double calcularGanancias() {
		double ganancia = 0.0;
		for (int i = 0; i < pedidos.size(); i++) {
			ganancia += pedidos.get(i).getCostoPedido();
		}
		return ganancia;
	}

	public double promedioGananciasTotales() {
		return calcularGanancias() / pedidos.size();
	}

	public double desviacionEstandarGananciasTotales() {
		double desviacionEstandar = 0.0;
		for (int i = 0; i < pedidos.size(); i++) {
			double xi = pedidos.get(i).getCostoPedido();
			double u = promedioGananciasTotales();
			desviacionEstandar += Math.pow((xi - u), 2);
		}
		return Math.sqrt((1.0 / (pedidos.size())) * desviacionEstandar);
	}

	public double retornarCostoPedido(String ID) {
		double costo = 0.0;
		for (int i = 0; i < pedidos.size(); i++) {
			if (pedidos.get(i).getnPedido().equals(ID)) {
				costo = pedidos.get(i).getCostoPedido();
			}
		}
		return costo;
	}

}
