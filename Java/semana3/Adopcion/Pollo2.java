package Lenguajes.Java.semana3.Adopcion;

public class Pollo2 extends Animal {
	public Pollo2(String nombre) {
		this.setNombre(nombre);
		System.out.println("Soy un pollo y me llamo " + this.getNombre());

	}

	@Override
	public void sonido() {
		System.out.println(this.getNombre() + "Pio Pio Pio");
	}

	@Override
	public void caminar() {
		System.out.println(this.getNombre() + "Comenzo a caminar");
	}
}
