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
