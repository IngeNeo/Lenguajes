package Lenguajes.Java.Clase2.visibilidad;

public class Tipo1 {

	public Tipo1() {
		System.out.println("Aca nuevo");
	}

	public void metodopublic() {
		System.out.println("Metodo public");
		metodoprivate();
	}

	private void metodoprivate() {
		System.out.println("Metodo metodoprivate");
	}

	void metodosintipo() {
		System.out.println("Metodo metodosintipo");
	}

	protected void metodoprotected() {
		System.out.println("Metodo metodoprotected");
	}

	static public void metodopublicstatic() {
		System.out.println("Metodo public");
		// metodoprivate();
	}

	/*
	 * static private void metodoprivatestatic() {
	 * System.out.println("Metodo metodoprivate"); }
	 */

	static void metodosintipostatic() {
		System.out.println("Metodo metodosintipo");
	}

	static protected void metodoprotectedstatic() {
		System.out.println("Metodo metodoprotected");
	}

	public int sumar(int a, int b) {
		return a + b;
	}

	public int restar(int a, int b) {
		return a - b;
	}

	public int dividir(int a, int b) {
		return a / b;
	}

	public float dividirfloat(float a, float b) {
		return a / b;
	}

	public int multiplicar(int a, int b) {
		return a * b;
	}

	public int residuo(int a, int b) {
		return a % b;
	}

	public boolean metodoBoolean() {
		return true;
	}

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

	}
}