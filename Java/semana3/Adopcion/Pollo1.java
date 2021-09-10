package Lenguajes.Java.semana3.Adopcion;

public class Pollo1 extends Animal {
	public Pollo1(String nombre) {
		this.setNombre(nombre);
		System.out.println("Soy un pollo y me llamo " + this.getNombre());
	}

	public void caminar() {
		System.out.println(this.getNombre() + " Comenzo a Caminar pollo1");
	}

	@Override
	public void sonido() {
		System.out.println(this.getNombre() + "cloc cloc cloc cloc");
	}
}
