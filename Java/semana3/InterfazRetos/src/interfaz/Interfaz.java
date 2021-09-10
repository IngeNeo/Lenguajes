package Lenguajes.Java.semana3.InterfazRetos.src.interfaz;

public class Interfaz {

	/**
	 * @param args the command line arguments
	 */
	public static void main(String[] args) {
		/*
		 * Empresa empresa1 = new ComidaUno("Comida Uno"); mostrarEmpresa(empresa1);
		 */

		ComidaUno empresa1 = new ComidaUno("Comidas Andres");
		empresa1.comprarProducto(10000);
		empresa1.ponerOnline();
		empresa1.comprarProducto(10000);
		System.out.println(empresa1.calcularDescuento(5));

	}

	public static void mostrarEmpresa(Empresa empresaCreada) {
		System.out.println(empresaCreada.mostraDescripcionEmpresa());
		System.out.println(empresaCreada.mostraNombreEmpresa());
	}

}
