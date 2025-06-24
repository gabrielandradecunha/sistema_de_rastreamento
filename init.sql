CREATE OR REPLACE FUNCTION inserir_historico_localizacao()
RETURNS TRIGGER AS $$
BEGIN
    -- Insere a nova localização no histórico
    INSERT INTO history_location (user_id, longitude, latitude)
    VALUES (NEW.id, NEW.longitude, NEW.latitude);

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
