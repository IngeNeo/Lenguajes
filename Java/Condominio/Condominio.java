package Lenguajes.Java.Condominio;
//EL CALIFICADOR GENERARÁ ERROR SI USTED NO IMPLEMENTA TODOS LOS MÉTODOS ESPECIFICADOS EN EL ENUNCIADO
import java.util.ArrayList;

public class Condominio {

	public static void main(String[] args) {

		ArrayList<Inmueble> Casas = new ArrayList<Inmueble>();

		Condominio n2 = new Condominio(Casas);
		Inmueble t1 = new Inmueble("001", "72023394", 70000.0, 96); // 6720000
		Inmueble t2 = new Inmueble("002", "1037681391", 67000.0, 80); // 5360000
		Inmueble t3 = new Inmueble("003", "33277591", 20000.0, 96); // 1920000
		Inmueble t4 = new Inmueble("004", "1032678245", 40000.0, 96); // 3840000

		System.out.println(Casas.size());
		n2.agregarInmueble(t1);
		System.out.println(Casas.size());
		n2.agregarInmueble(t2);
		System.out.println(Casas.size());
		n2.agregarInmueble(t3);
		System.out.println(Casas.size());

		// System.out.println(n2.trabajadores.get(0).getCC() + " " +
		// n2.trabajadores.get(0).getNombre());
		// System.out.println(n2.trabajadores.get(1).getCC() + " " +
		// n2.trabajadores.get(1).getNombre());
		// System.out.println(n2.trabajadores.get(2).getCC() + " " +
		// n2.trabajadores.get(2).getNombre());

		n2.eliminarInmueble("123456789");
		// System.out.println(n2.salarioQuincenalTrabajador("72023394"));
		n2.agregarInmueble(t4);
		// System.out.println(Nomina.size());
		// System.out.println(n2.trabajadores.get(3).getCC() + " " +
		// n2.trabajadores.get(3).getNombre());
		n2.eliminarInmueble("72023394");
		// System.out.println(Nomina.size());

		// System.out.println(n2.calcularSalarioQuincenalNomina());
		n2.desviacionEstandarCostoInmueble();
		// System.out.println(n2.desviacionEstandarEdadNomina());
	}
	// Inserte acá los atributos
	private ArrayList<Inmueble> inmuebles = new ArrayList<Inmueble>();

	// Inserte acá el método constructor
	public Condominio() {

	}

	public Condominio(ArrayList<Inmueble> inmuebles){
		this.inmuebles = inmuebles;
	}

	// Inserte acá los SETTERS Y GETTERS
	public ArrayList<Inmueble> getInmuebles() {
		return this.inmuebles;
	}

	// Inserte acá los métodos (NO LOS GETTER Y SETTERS)
	public void agregarInmueble(Inmueble i) {
		boolean encontrado = false;
		if (inmuebles.size() == 0) {
			this.inmuebles.add(i);
		} else {
			for (int j = 0; j < inmuebles.size(); j++) {
				if (this.inmuebles.get(j).getnCasa().equals(i.getnCasa())) {
					encontrado = true;
				}
			}
			if (encontrado == false) {
				this.inmuebles.add(i);
			}
		}
	}

	public void eliminarInmueble(String ID) {
		for (int j = 0; j < inmuebles.size(); j++) {
			if (this.inmuebles.get(j).getnCasa().equals(ID)) {
				this.inmuebles.remove(j);
			}
		}
	}

	public double calcularArriendoMensualCondominio() {
		double suma = 0;
		for (int j = 0; j < inmuebles.size(); j++) {
			suma = suma + this.inmuebles.get(j).getCostoMensual();
		}
		return suma;
	}

	public double promedioCostoInmueble() {
		return calcularArriendoMensualCondominio() / inmuebles.size();
	}

	public double desviacionEstandarCostoInmueble() {
		double desviacion = 0.0;
		for (int i = 0; i < inmuebles.size(); i++) {
			desviacion += Math.pow((inmuebles.get(i).getCostoMensual() - promedioCostoInmueble()), 2);
		}
		return Math.sqrt((1.0 / (inmuebles.size())) * desviacion);
	}
}