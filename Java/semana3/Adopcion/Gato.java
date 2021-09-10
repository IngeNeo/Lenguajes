package Lenguajes.Java.semana3.Adopcion;

public class Gato extends Animal {
	public Gato(String nombre) {
		this.setNombre(nombre);
		System.out.println("Soy un gato y me llamo " + this.getNombre());
	}

	@Override
	public void sonido() {
		System.out.println(this.getNombre() + " Miau Miau Miau");
	}
}
