package Lenguajes.Java.semana3.InterfazRetos.src.interfaz;

public class ComidaUno extends EmpresaAbstracta implements Empresa {
	String nombreEmpresa;

	public ComidaUno(String nombreEmpresa) {
		this.nombreEmpresa = nombreEmpresa;
	}

	public void ponerOnline() {
		this.online = !this.online;
	}

	@Override
	public String mostraNombreEmpresa() {
		return this.nombreEmpresa;
	}

	@Override
	public String mostraDescripcionEmpresa() {
		return "venta de alimentos de granjas propias.";
	}

	@Override
	public double calcularDescuento(int estrato) {
		// 0 - 2 : 40% -> 3 - 4: 20 % -> 5> : 5%
		double descuento = 0;
		if (this.online) {
			if (estrato >= 0 && estrato <= 2) {
				descuento = 0.4;
			} else if (estrato >= 3 && estrato <= 4) {
				descuento = 0.2;
			} else if (estrato >= 5) {
				descuento = 0.05;
			}
		}
		return descuento;
	}

	@Override
	public boolean calcularDomicilio(double baseX, double baseY) {
		// raiz cuadrada de la suma de X elevado a la 2 y Y elevado a las 2.
		if (this.online) {
			double baseXalCuadrado = Math.pow(baseX, 2);
			double baseYalCuadrado = Math.pow(baseY, 2);
			double sumaXyY = baseXalCuadrado + baseYalCuadrado;
			double distancia = Math.sqrt(sumaXyY);
			// return distancia <= 10.0? true : false;
			return distancia <= 10.0;
		}
		return false;
	}

}
