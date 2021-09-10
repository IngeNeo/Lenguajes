package Lenguajes.Java.semana3.Adopcion;

public class Pollo extends Animal {
	public Pollo(String nombre) {
		this.setNombre(nombre);
		System.out.println("Soy un pollo y me llamo " + this.getNombre());
	}

	@Override
	public void caminar() {
		System.out.println(this.getNombre() + " Comenzó a volar");
	}

	@Override
	public void sonido() {
		System.out.println(this.getNombre() + " kikriki");
	}
}
