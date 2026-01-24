import requests
from pathlib import Path

def download_to_local(url: str, out_path: Path, parent_mkdir: bool = True):
    """
    Descarga un archivo desde una URL a una ruta local.

    Args:
        url (str): La URL del archivo a descargar.
        out_path (Path): La ruta local donde se guardará el archivo (objeto Path).
        parent_mkdir (bool): Si es True, crea los directorios padres si no existen.

    Returns:
        bool: True si la descarga fue exitosa, False en caso contrario.
    """
    # Verifica que out_path sea una instancia de Path (de pathlib).
    # Esto es importante para usar métodos como .parent o .write_bytes luego.
    if not isinstance(out_path, Path):
        raise ValueError(f'{out_path} must be a valid pathlib. Path object expected')

    # Si parent_mkdir es True, nos aseguramos de que la carpeta donde va el archivo exista.
    if parent_mkdir:
        # out_path.parent obtiene la carpeta contenedora.
        # mkdir(parents=True, exist_ok=True) crea la carpeta y sus padres si es necesario,
        # y no falla si ya existen.
        out_path.parent.mkdir(exist_ok=True, parents=True)

    try:
        # Realizamos la petición GET a la URL para obtener el recurso.
        response = requests.get(url)

        # raise_for_status() revisa el código de respuesta HTTP.
        # Si es un error (como 404 No Encontrado o 500 Error de Servidor), lanza una excepción.
        response.raise_for_status()

        # Escribimos el contenido binario (bytes) de la respuesta en el archivo de destino.
        out_path.write_bytes(response.content)

        # Si todo salió bien, retornamos True.
        return True

    except requests.RequestException as e:
        # Capturamos cualquier error relacionado con la petición (problemas de red, URL inválida, etc.).
        print(f'Failed to download {url}: {e}')
        return False
