package Lenguajes.Java.Clase7.UMLCLASE;

public class Aeropuerto {
	private String ciudad;

	/**
	 * Constructor for objects of class Aeropuerto
	 */
	public Aeropuerto(String ciudad) {
		this.ciudad = ciudad;
	}

	public void setCiudad(String ciudad) {
		this.ciudad = ciudad;
	}

	public String getCiudad() {
		return this.ciudad;
	}

}
