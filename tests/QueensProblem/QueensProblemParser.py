import os


class QueensProblemParser:
    @staticmethod
    def parse_input_file_to_dzn(input_file_path):
        """
        Convierte un archivo de entrada en un archivo .dzn para Minizinc.

        Parámetros:
        input_file_path (str): La ruta al archivo de entrada.

        Retorna:
        str: La ruta al archivo .dzn generado.

        Lanza:
        ValueError: Si el contenido del archivo no es un número válido.
        """

        with open(input_file_path, 'r') as file:
            line = file.readline().strip()
        try:
            n = int(line)
        except ValueError:
            raise ValueError(
                "El contenido del archivo no es un número válido: {}".format(str(line)))

        dzn_content = "n_i = {};\n".format(str(n))

        dzn_file_path = input_file_path.rsplit('.', 1)[0] + ".dzn"

        with open(dzn_file_path, 'w') as dzn_file:
            dzn_file.write(dzn_content)

        file_info = {
            "filename": os.path.basename(input_file_path),
            "path": dzn_file_path,
            "content": dzn_content,
        }

        return file_info
