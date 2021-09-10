package Lenguajes.Java.semana3.InterfazDoctoHouse;

public class DoctorHouse implements Serie {
	private String nombre;
	private int numEpisodios;
	private String genero;
	private String episodioActua;

	String[] episodios;

	public DoctorHouse() {
		this.nombre = "Doctor House";
		this.numEpisodios = 6;
		this.genero = "Accion";
		this.episodioActua = "1. Piloto";
		this.episodios = new String[numEpisodios];
	}

	@Override
	public String siguienteEpisodio() {
		return "";
	}

	@Override
	public String episodioAnterior() {
		return "";
	}

	@Override
	public String getEpisodioActua() {
		return this.episodioActua;
	}

	@Override
	public String getNombre() {
		return this.nombre;
	}

	@Override
	public int getNumEpisodios() {
		return this.numEpisodios;
	}

	@Override
	public String getGenero() {
		return this.genero;
	}

	@Override
	public void volveraEmpezar() {
		this.episodioActua = "1. Piloto";
	}
}
