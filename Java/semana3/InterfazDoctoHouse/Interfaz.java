package Lenguajes.Java.semana3.InterfazDoctoHouse;

//import java.util.Arrays;

public class Interfaz {

	public static void main(String[] args) {
		int[] v1 = { 0, 2, 1, 65, 66, 78, 12, 11, 90, 13 };
		int[] v2 = { 0, -2, 1, 9, 4, 78, 12, 11, 90, 13 };

		/*
		 * Cuando pones sumaVectorial = (acá esta diciendole a java que vas asignar una
		 * variable, y por ende debes de especificar el tipo de vairable a manejar Creo
		 * que lo que quieres es guardar el resultado haciendole el llamado al medoto,
		 * entonces el caso sería diferente
		 *
		 * Entonces, definimos la variable (En este caso sería sumaVectoriaResultado
		 * como para diferenciar) y llamamos la funcion, como la llamamos ¿? en este
		 * caso, nombrendo la función y enviando los parametros. sumaVectorial(v1,v2);
		 *
		 * Haríamos que el valor que retorna la función de una vez queda guardado en la
		 * variuable
		 *
		 * Quedaria así entonces
		 *
		 * int[] sumaVectorialResultado = sumaVectorial(v1,v2);
		 *
		 */

		// Por eso acá da error, ahora porque utilizar Array.toString ? no lo hemos
		// visto, y para el ejercicio no es importante.
		// sumaVectorial = Arrays.toString(v1 , v2);

		/*
		 * Acá como ya anteriomente declaramos ya la variable que va a tener el
		 * resultado, entonces solamente mostramos por pantalla el valor de ese
		 * resultado
		 *
		 * System.out.print(sumaVectorialResultado);
		 *
		 * Pero claro, le vas a mostrar algo raro, porque le muestra la ubicación en
		 * memoria, si quiere ver el resultado, tendría que hacer un for que recorra esa
		 * lista.
		 *
		 * Pero para temas del ejercicio no lo piden, solamente piden la funcionalidad
		 * de sumaVectorial;
		 */

		/*
		 * Acá sale error porque estas llamando la funcion con una variable V1 en
		 * mayuscula la V, y esa variable no existe.
		 *
		 */
		System.out.print(sumaVectorial(v1, v2));

		/*
		 * Si queremos tambien mostrar el resultado sin guardar en una variable lo puede
		 * hacer como lo tienes pero enviando en nombre de la variable bien.
		 *
		 * System.out.print(sumaVectorial(v1, v2));
		 *
		 */

	}

	public static int[] sumaVectorial(int[] v1, int[] v2) {

		/*
		 * Acá noto que la funcion esta correcta y que de verdad tiene que retornar el
		 * arreglo sumado.... en la plataforma, ya sale esta función, entonces es solo
		 * colocarlo allá este codigo y listo no hay problema
		 */

		int lon = v1.length;
		int[] s = new int[lon];

		for (int i = 0; i < lon; i++) {
			s[i] = v1[i] + v2[i];
		}

		return s;
	}
}
