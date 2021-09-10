package Lenguajes.Java.semana3.Adopcion;

public class Perro extends Animal {

	public Perro(String nombre) {
		this.setNombre(nombre);
		System.out.println("Soy un perro y me llamo " + this.getNombre());
	}

	@Override
	public void sonido() {
		System.out.println(this.getNombre() + " Gua Gua Gua Gua");
	}
}
