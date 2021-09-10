package Lenguajes.Java.Clase2;

import Lenguajes.Java.Clase2.visibilidad.Tipo1;

public class Clase2 {

	public static void main(String[] args) {
		Tipo1 variable1 = new Tipo1();

		int sumar = variable1.sumar(1, 2);
		int restar = variable1.restar(2, 1);
		int dividir = variable1.dividir(10, 3);
		float dividirfloat = variable1.dividirfloat(10, 3);
		int multiplicar = variable1.multiplicar(2, 3);
		int residuo = variable1.residuo(10, 3);

		System.out.println(sumar);
		System.out.println(restar);
		System.out.println(variable1.restar(2, 1));
		System.out.println(dividir);
		System.out.println(dividirfloat);
		System.out.println(multiplicar);
		System.out.println(residuo);

		variable1.metodopublic();
		Tipo1.metodopublicstatic();
		variable1.metodoBoolean();

	}
}
