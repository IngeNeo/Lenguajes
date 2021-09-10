package Lenguajes.Java.semana3.Adopcion;

public abstract class Animal {
	private String nombre;

	public String getNombre() {
		return this.nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public void comer() {
		System.out.println(this.nombre + " Comenzo a comer");
	}

	public void caminar() {
		System.out.println(this.nombre + "Comenzo a caminar");
	}

	public abstract void sonido();

}
