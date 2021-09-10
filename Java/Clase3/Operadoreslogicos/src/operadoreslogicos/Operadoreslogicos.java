package Lenguajes.Java.Clase3.Operadoreslogicos.src.operadoreslogicos;

public class Operadoreslogicos {

	public static void main(String[] args) {

		/*
		 * int valor = 5; System.out.println(valor); System.out.println(valor++);
		 * System.out.println(valor); System.out.println(valor--);
		 * System.out.println(valor); System.out.println(valor);
		 * System.out.println(++valor); System.out.println("hola mundo");
		 *
		 *
		 * int a = 1; int b = 1; int c = 2; int d = 2;
		 *
		 *
		 * System.out.println(a < b); System.out.println(a > b);
		 *
		 * System.out.println(a >= b); System.out.println(a <= b);
		 *
		 * System.out.println(a == b); System.out.println(a != b);
		 *
		 * System.out.println(a != b && c != d); System.out.println(a == b && c == d);
		 *
		 * System.out.println(a == b || c != d); System.out.println(a == b || c == d);
		 * System.out.println(a != b || c != d);
		 *
		 *
		 * float A = 1; System.out.println(A); A+=3; System.out.println(A); A-=3;
		 * System.out.println(A); A/=3; System.out.println(A);
		 *
		 * a = +3 * 2 / 2;
		 *
		 * System.out.println(a);
		 */

		/*
		 * String a = "hola"; String b = "mundokk"; String c = "mundokk"; String d =
		 * "mundo"; String f = "Objeto"; System.out.println(a+b+c+d+f);
		 *
		 * System.out.println(b == c); //System.out.println(b.compareTo(a));
		 * //System.out.println(b.compareToIgnoreCase(c));
		 *
		 * //System.out.println(b.equals(c)); //System.out.println(b.equals(a));
		 * //System.out.println(b.equalsIgnoreCase(c));
		 *
		 *
		 * //System.out.println(b.compareTo(a));
		 */
		int a = 3;
		int b = 3;

		if (a == b && a > b) {
			System.out.println("Si es verdad");
		} else if (a > b) {
			System.out.println("a es mayor");
		} else if (a != b) {
			System.out.println("a es menor");
		} else {
			System.out.println("es diferente");
		}

		System.out.println("Siguiente linea");

		String dia = "Hola";

		switch (dia) {
			case "Hola":
				System.out.println("Lunes");
				break;
			case "Hola2":
				System.out.println("Dia Miercoles");
				break;
			case "Hola Mundo ":
				System.out.println("Dia Martes");
				break;
			default:
				System.out.println("Dia Invalido");
				break;
		}

	}

}
