from app.core.database import connection

class HistoryLocation:

    # Create Table Method
    @staticmethod
    def create():
        try:
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS history_location (
                    id SERIAL PRIMARY KEY,
                    user_id INT,
                    longitude DOUBLE PRECISION,
                    latitude DOUBLE PRECISION,
                    CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
                )
            """)
            connection.commit()
            print("Tabela history_location criada ou já existente.")
        except Exception as e:
            connection.rollback()
            print(f"Erro ao criar a tabela: {e}")
        finally:
            cursor.close()

    # Get History Method
    @staticmethod
    def gethistory(user_id):
        try:
            cursor = connection.cursor()
            query = "SELECT longitude, latitude FROM history_location WHERE user_id = %s ORDER BY id ASC"
            cursor.execute(query, (user_id,))
            result = cursor.fetchall()
            history = [{"longitude": row[0], "latitude": row[1]} for row in result]
            return history
        except Exception as e:
            print(f"Erro ao obter historico de usuarios: {e}")
            return []
        finally:
            cursor.close()
