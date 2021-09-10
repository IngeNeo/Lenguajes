package Lenguajes.Java.semana3.Adopcion;

public class Pez extends Animal {
	public Pez(String nombre) {
		this.setNombre(nombre);
		System.out.println("Soy un pez y me llamo " + this.getNombre());
	}

	@Override
	public void comer() {
		System.out.println(this.getNombre() + " Soy un pez y como diferente");
	}

	@Override
	public void caminar() {
		System.out.println(this.getNombre() + " Comenzo a Nadar");
	}

	@Override
	public void sonido() {
		System.out.println(this.getNombre() + " glup glup glup");
	}
}
