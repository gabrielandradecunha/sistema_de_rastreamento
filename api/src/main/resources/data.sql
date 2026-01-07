CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    senha VARCHAR(100),
    longitude DOUBLE PRECISION,
    latitude DOUBLE PRECISION
);

CREATE TABLE IF NOT EXISTS history_location (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    longitude DOUBLE PRECISION,
    latitude DOUBLE PRECISION,
    CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- init_trigger.sql

-- Função para inserir no histórico
CREATE OR REPLACE FUNCTION inserir_historico_localizacao()
RETURNS TRIGGER AS $$
BEGIN
INSERT INTO history_location (user_id, longitude, latitude)
VALUES (NEW.id, NEW.longitude, NEW.latitude);
RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Trigger associada à tabela users
CREATE TRIGGER trigger_historico_localizacao
    AFTER UPDATE ON users
    FOR EACH ROW
    WHEN (OLD.latitude IS DISTINCT FROM NEW.latitude OR OLD.longitude IS DISTINCT FROM NEW.longitude)
EXECUTE FUNCTION inserir_historico_localizacao();