package com.api_rastreamento.service;

import com.api_rastreamento.model.Usuario;
import com.api_rastreamento.model.HistoryLocation;
import com.api_rastreamento.repository.HistoryLocationRepository;
import com.api_rastreamento.repository.UserRepository;
import org.springframework.stereotype.Service;
import java.util.List;
import java.util.Map;

@Service
public class UsuarioService {

    private final UserRepository userRepository;
    private final HistoryLocationRepository historyRepository;

    public UsuarioService(UserRepository userRepository,
                          HistoryLocationRepository historyRepository) {
        this.userRepository = userRepository;
        this.historyRepository = historyRepository;
    }

    public Map<String, Object> getHistory(String email, String senha) {
        Usuario user = userRepository.findByEmailAndSenha(email, senha)
                .orElseThrow(() -> new RuntimeException("Usuário não encontrado"));

        return Map.of(
                "longitude", user.getLongitude(),
                "latitude", user.getLatitude()
        );
    }

    public Map<String, Object> getUser(String email, String senha) {
        Usuario user = userRepository.findByEmailAndSenha(email, senha)
                .orElseThrow(() -> new RuntimeException("Usuário não encontrado"));

        List<HistoryLocation> historico =
                historyRepository.findByUsuario_Id(user.getId());

        return Map.of(
                "id", user.getId(),
                "nome", user.getNome(),
                "email", user.getEmail(),
                "longitude_atual", user.getLongitude(),
                "latitude_atual", user.getLatitude(),
                "historico", historico
        );
    }

    public void createUser(String nome, String email, String senha,
                           Double longitude, Double latitude) {

        Usuario user = new Usuario();
        user.setNome(nome);
        user.setEmail(email);
        user.setSenha(senha);
        user.setLongitude(longitude);
        user.setLatitude(latitude);

        userRepository.save(user);
    }
}
