import os


class PUICAProblemParser:
    @staticmethod
    def parse_input_file_to_dzn(input_file_path):
        """
        Convierte un archivo de entrada del problema PUICA en un archivo .dzn para Minizinc.

        Parámetros:
        input_file_path (str): La ruta al archivo de entrada.

        Retorna:
        str: La ruta al archivo .dzn generado.
        """

        with open(input_file_path, 'r') as file:
            # Número de clientes
            n = int(file.readline().strip())
            # Número de sitios
            m = int(file.readline().strip())
            # Costos fijos
            f = list(map(float, file.readline().strip().split(',')))
            # Capacidades
            c = list(map(int, file.readline().strip().split(',')))
            # Demandas
            d = list(map(float, file.readline().strip().split(',')))
            # Beneficios
            b = [list(map(float, file.readline().strip().split(',')))
                 for _ in range(n)]

        dzn_content = f"n = {n};\nm = {m};\n"
        dzn_content += "f = [" + ", ".join(map(str, f)) + "];\n"
        dzn_content += "c = [" + ", ".join(map(str, c)) + "];\n"
        dzn_content += "d = [" + ", ".join(map(str, d)) + "];\n"
        dzn_content += "b = [| " + \
            " | ".join([", ".join(map(str, row)) for row in b]) + " |];\n"

        dzn_file_path = input_file_path.rsplit('.', 1)[0] + ".dzn"

        with open(dzn_file_path, 'w') as dzn_file:
            dzn_file.write(dzn_content)

        file_info = {
            "filename": os.path.basename(input_file_path),
            "path": dzn_file_path,
            "content": dzn_content,
        }

        return file_info

    @staticmethod
    def test_parse_input_file_to_dzn():
        from tools.File_selector import File_selector
        return Parser.parse_input_file_to_dzn(File_selector.select())
