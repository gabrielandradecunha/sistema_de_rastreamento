CREATE OR REPLACE FUNCTION inserir_historico_localizacao()
RETURNS TRIGGER AS $$
DECLARE
    user_id INTEGER;
BEGIN
    -- Obtém o ID do usuário
    SELECT id INTO user_id FROM users WHERE email = NEW.email;

    -- Insere na tabela de histórico
    INSERT INTO history_location (user_id, longitude, latitude)
    VALUES (user_id, NEW.longitude, NEW.latitude);

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
