package Lenguajes.Java.Clase2.visibilidad;

public class Tipo2 {

	public Tipo2() {
		Tipo1 tipo1 = new Tipo1();
		tipo1.metodoprotected();
		tipo1.metodosintipo();
		// tipo1.metodoprivate();

		Tipo1.metodoprotectedstatic();
	}
}
