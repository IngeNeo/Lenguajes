package Lenguajes.Java.Pruebas;

//import java.util;

public class Pruebas {

	public static void main(String[] args) {

		/*
		 * Se solicita incluir la siguiente información acerca de un libro: titulo autor
		 * Debes imprimir la información en el siguiente formato:
		 *
		 * Proporciona el titulo: Proporciona el autor: <titulo> fue escrito por <autor>
		 */

		/*
		 * Scanner entrada = new Scanner(System.in);
		 * System.out.print("Digite el titulo del libro: "); String titulo =
		 * entrada.nextLine();
		 *
		 * System.out.print("Digite el nombre del autor del libro: "); String autor =
		 * entrada.nextLine();
		 *
		 * System.out.println("El libro " + titulo + " fue escrito por " + autor);
		 */

		/*
		 * Se solicita capturar la siguiente información de una tienda de libros: nombre
		 * (String) id (int) precio (double) envioGratuito (boolean) Tu tarea es
		 * imprimir un mensaje en el siguiente formato:
		 *
		 * Proporciona el nombre: Proporciona el id: Proporciona el precio: Proporciona
		 * el envio gratuito: <nombre> #<id> Precio: <simbolo><precio> Envio Gratuito:
		 * <envioGratuito> Por ejemplo:
		 *
		 * Proporciona el nombre: Programacion con Java Proporciona el id: 1520
		 * Proporciona el precio: 899 Proporciona el envio gratuito: true Programacion
		 * con Java #1520 Precio: $899.00 Envio Gratuito: true
		 */

		/*
		 * Scanner entrada = new Scanner(System.in);
		 * System.out.print("Digite el nombre del libro: ");
		 * String nombre = entrada.nextLine();
		 *
		 * System.out.print("Digite el ID del libro: ");
		 * int id = entrada.nextInt();
		 *
		 * System.out.print("Digite el precio del libro: ");
		 * double precio = entrada.nextDouble();
		 *
		 * System.out.print("El envio es gratuito (true, false): ");
		 * boolean envioGratuito = entrada.nextBoolean();
		 *
		 * System.out.println(nombre + " #" + id);
		 * System.out.println("Precio: " + "$" + precio);
		 * System.out.println("Envio Gratuito: " + envioGratuito);
		 */

		/*
		 * Scanner scanner = new Scanner(System.in);
		 * //Escribe tu solucion aqui
		 * System.out.print("Digite el alto: ");
		 * int alto = Integer.parseInt(scanner.nextLine());
		 * System.out.print("Digite el ancho: ");
		 * int ancho = Integer.parseInt(scanner.nextLine());
		 * int area = alto ancho;
		 * int perimetro = (alto + ancho) 2;
		 * System.out.println("Area: " + area);
		 * System.out.println("Perimetro: " + perimetro);
		 */

		/*
		 * Scanner scanner = new Scanner(System.in);
		 * System.out.print("Digite el numero 1: ");
		 * int numero1 = Integer.parseInt(scanner.nextLine());
		 * System.out.print("Digite el numero 2: ");
		 * int numero2 = Integer.parseInt(scanner.nextLine());
		 * System.out.print("El numero mayor es: ");
		 * System.out.println(numero1 > numero2 ? numero1 : numero2);
		 */

		/*
		 * Scanner scanner = new Scanner(System.in);
		 * System.out.print("Ingrese un valor entre 0 y 10: ");
		 * int calificacion = Integer.parseInt(scanner.nextLine());
		 * //Si esta entre 9 y 10 imprimir: A
		 * if (calificacion >= 9 && calificacion <= 10)
		 * System.out.println("A");
		 * //Si esta entre 8 y menor a 9 imprimir: B
		 * else if (calificacion >= 8 && calificacion < 9)
		 * System.out.println("B");
		 * //Si esta entre 7 y menor a 8 imprimir: C
		 * else if (calificacion >= 7 && calificacion < 8)
		 * System.out.println("C");
		 * //Si esta entre 6 y menor a 7 imprimir: D
		 * else if (calificacion >= 6 && calificacion < 7)
		 * System.out.println("D");
		 * //Si esta entre 0 y menor a 6 imprimir: F
		 * else if (calificacion >= 0 && calificacion < 6)
		 * System.out.println("F");
		 * //Si no esta en el rago, imprimir: Valor desconocido
		 * else
		 * System.out.println("Valor desconocido");
		 */

		double localizacionX = 10, localizacionY = 10;

		double valor = (Math.pow(localizacionX, 2)) + (Math.pow(localizacionY, 2));
		double distancia = (Math.sqrt((valor)));
		System.out.println(distancia);
	}
}