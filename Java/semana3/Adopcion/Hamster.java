package Lenguajes.Java.semana3.Adopcion;

public class Hamster extends Animal

{
	public Hamster(String nombre) {
		this.setNombre(nombre);
		System.out.println("Soy un hamster me llamo " + this.getNombre());
	}

	@Override
	public void comer() {
		System.out.println(this.getNombre() + " empezo a comer semillas de girasol");
	}

	@Override
	public void caminar() {
		System.out.println(this.getNombre() + " empezo a correr en su bola estatica");
	}

	@Override
	public void sonido() {
		System.out.println(this.getNombre() + " glapuff glapuff glapuff");
	}

}
