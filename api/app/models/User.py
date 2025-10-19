from app.core.database import connection

class User:

    # Create Table Method
    @staticmethod
    def create():
        try:
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    nome VARCHAR(100),
                    email VARCHAR(100) UNIQUE,
                    senha VARCHAR(100),
                    longitude DOUBLE PRECISION,
                    latitude DOUBLE PRECISION
                )
            """)
            connection.commit()
            print("Tabela users criada ou já existente.")
        except Exception as e:
            connection.rollback()
            print(f"Erro ao criar a tabela: {e}")
        finally:
            cursor.close()

    # Delete Table Method
    @staticmethod
    def delete():
        try:
            cursor = connection.cursor()
            cursor.execute("DROP TABLE IF EXISTS users")
            connection.commit()
            print("Tabela 'users' deletada.")
        except Exception as e:
            connection.rollback()
            print(f"Erro ao deletar a tabela: {e}")
        finally:
            cursor.close()

    # Create User Method
    @staticmethod
    def createuser(nome, email, senha, longi, lati):
        try:
            cursor = connection.cursor()
            query = """
                INSERT INTO 
                users (nome, email, senha, longitude, latitude) 
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (nome, email, senha, longi, lati))
            connection.commit()
            print("Usuário inserido com sucesso.")
        except Exception as e:
            connection.rollback()
            print(f"Erro ao inserir usuário: {e}")
        finally:
            cursor.close()

    # Delete User Method
    @staticmethod
    def deleteuser(email, senha):
        try:
            cursor = connection.cursor()
            query = "DELETE FROM users WHERE email=%s AND senha=%s"
            cursor.execute(query, (email, senha))
            connection.commit()
            print("Usuário deletado com sucesso.")
        except Exception as e:
            connection.rollback()
            print(f"Erro ao deletar usuário: {e}")
        finally:
            cursor.close()

    # Get User Method
    @staticmethod
    def getuser(email, senha):
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM users WHERE email = %s AND senha = %s", (email, senha))
            return cursor.fetchone()
        except Exception as e:
            connection.rollback()
            print(f"Erro ao buscar usuário: {e}")
            return None
        finally:
            cursor.close()

    @staticmethod
    def update(email, longi, lati):
        try:
            cursor = connection.cursor()
            query = """
                UPDATE users
                SET longitude = %s,
                    latitude = %s
                WHERE email = %s
            """
            cursor.execute(query, (longi, lati, email))
            if cursor.rowcount == 0:
                print("Usuário não encontrado. Nenhuma atualização realizada.")
            else:
                print("Usuário atualizado com sucesso.")
            connection.commit()
        except Exception as e:
            connection.rollback()
            print(f"Erro ao atualizar usuário: {e}")
        finally:
            cursor.close()
