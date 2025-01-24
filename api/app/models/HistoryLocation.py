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