package Lenguajes.Java.Persona;

public class Estudiante extends Persona {
	// Inserte acá el método constructor
	public Estudiante(String id, String nombre, String email, String idioma) {
		super(id, nombre, email, idioma);
	}

	// Inserte acá la implementación del método abstracto de la clase padre
	public void dirigir() {
		String ruta = "/";
		String URL_New = this.getUrl() + ruta + this.getIdioma() + ruta + "estudiante";
		this.setUrl(URL_New);
	}
}