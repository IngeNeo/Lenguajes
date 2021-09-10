package Lenguajes.Java.Nomina;

//EL CALIFICADOR GENERARÁ ERROR SI USTED NO IMPLEMENTA TODOS LOS MÉTODOS ESPECIFICADOS EN EL ENUNCIADO
import java.util.ArrayList;

public class Nomina {
	public static void main(String[] args) {
		/*
		 * OPERACIONES DE ENTRADA: [agregarTrabajador(t1), agregarTrabajador(t2),
		 * agregarTrabajador(t3), eliminarTrabajador("123456789"),
		 * salarioQuincenalTrabajador("72023394"), agregarTrabajador (t4),
		 * eliminarTrabajador("72023394")]
		 */

		ArrayList<Trabajador> Nomina = new ArrayList<Trabajador>();

		Nomina n2 = new Nomina(Nomina);
		Trabajador t1 = new Trabajador("Daniel", "72023394", 70000.0, 96, 31, 8, 1981); // 6720000
		Trabajador t2 = new Trabajador("Mat", "1037681391", 67000.0, 80, 23, 1, 2000); // 5360000
		Trabajador t3 = new Trabajador("Johan", "33277591", 20000.0, 96, 24, 5, 1970); // 1920000
		Trabajador t4 = new Trabajador("Paulo", "1032678245", 40000.0, 96, 7, 3, 2001); // 3840000

		System.out.println(Nomina.size());
		n2.agregarTrabajador(t1);
		System.out.println(Nomina.size());
		n2.agregarTrabajador(t2);
		System.out.println(Nomina.size());
		n2.agregarTrabajador(t3);
		System.out.println(Nomina.size());

		n2.eliminarTrabajador("123456789");
		System.out.println(n2.salarioQuincenalTrabajador("72023394"));
		n2.agregarTrabajador(t4);
		System.out.println(Nomina.size());
		System.out.println(n2.trabajadores.get(3).getCC() + " " + n2.trabajadores.get(3).getNombre());
		n2.eliminarTrabajador("72023394");
		System.out.println(Nomina.size());

		System.out.println(n2.calcularSalarioQuincenalNomina());
		n2.desviacionEstandarEdadNomina();
		System.out.println(n2.desviacionEstandarEdadNomina());
	}

	// Inserte acá los atributos
	private ArrayList<Trabajador> trabajadores = new ArrayList<Trabajador>();

	// Inserte acá el método constructor
	public Nomina() {

	}

	public Nomina(ArrayList<Trabajador> trabajadores) {
		this.trabajadores = trabajadores;
	}

	// Inserte acá los SETTERS Y GETTERS
	public ArrayList<Trabajador> getTrabajadores() {
		return this.trabajadores;
	}

	// Inserte acá los métodos (NO LOS GETTER Y SETTERS)
	public void agregarTrabajador(Trabajador t) {
		boolean ya = false;
		if (trabajadores.size() == 0) {
			this.trabajadores.add(t);
		} else {
			for (int i = 0; i < trabajadores.size(); i++) {
				if (trabajadores.get(i).getCC().equals(t.getCC())) {
					ya = true;
				}
			}
			if (ya == false) {
				this.trabajadores.add(t);
			}
		}
	}

	public void eliminarTrabajador(String ID) {
		for (int i = 0; i < trabajadores.size(); i++) {
			if (trabajadores.get(i).getCC().equals(ID)) {
				this.trabajadores.remove(i);
			}
		}
	}

	public int calcularSalarioQuincenalNomina() {
		int quincena = 0;
		for (int i = 0; i < trabajadores.size(); i++) {
			quincena += trabajadores.get(i).salarioQuincenal();
		}
		return quincena;
	}

	public double promedioEdadNomina() {
		double edad = 0;
		for (int i = 0; i < trabajadores.size(); i++) {
			edad += trabajadores.get(i).calcularEdad();
		}
		return edad / trabajadores.size();
	}

	public double desviacionEstandarEdadNomina() {
		double variacion = 0.0;
		for (int i = 0; i < trabajadores.size(); i++) {
			double e = trabajadores.get(i).calcularEdad();
			double p = promedioEdadNomina();
			variacion += Math.pow((e - p), 2);
		}
		variacion = Math.sqrt((1.0 / (trabajadores.size())) * variacion);
		return variacion;
	}

	public double salarioQuincenalTrabajador(String ID) {
		double quincena = -1;
		for (int i = 0; i < trabajadores.size(); i++) {
			if (trabajadores.get(i).getCC() == ID) {
				quincena = trabajadores.get(i).salarioQuincenal();
			}
		}
		return quincena;
	}
}