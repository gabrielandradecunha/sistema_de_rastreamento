package com.api_rastreamento.controller;

import com.api_rastreamento.model.Usuario;
import com.api_rastreamento.model.HistoryLocation;
import com.api_rastreamento.repository.UserRepository;
import com.api_rastreamento.repository.HistoryLocationRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;

@CrossOrigin(origins = "*")
@RestController
@RequestMapping("/api")
public class UsuarioController {

    @Autowired
    private UserRepository userRepository;

    @Autowired
    private HistoryLocationRepository historyRepository;


    @PostMapping("/historylocation")
    public ResponseEntity<?> getHistory(
            @RequestParam String email,
            @RequestParam String senha
    ) {
        Usuario user = userRepository.findByEmailAndSenha(email, senha).orElse(null);
        if (user == null) {
            return ResponseEntity.status(404).body(Map.of("error", "Usuário não encontrado"));
        }

        return ResponseEntity.ok(Map.of(
                "longitude", user.getLongitude(),
                "latitude", user.getLatitude()
        ));
    }

    @PostMapping("/getuser")
    public ResponseEntity<?> getUser(
            @RequestParam String email,
            @RequestParam String senha
    ) {
        Usuario user = userRepository.findByEmailAndSenha(email, senha).orElse(null);
        if (user == null) {
            return ResponseEntity.status(404).body(Map.of("error", "Usuário não encontrado"));
        }

        List<HistoryLocation> historico = historyRepository.findByUsuario_Id(user.getId());

        return ResponseEntity.ok(Map.of(
                "id", user.getId(),
                "nome", user.getNome(),
                "email", user.getEmail(),
                "longitude_atual", user.getLongitude(),
                "latitude_atual", user.getLatitude(),
                "historico", historico
        ));
    }


    @PostMapping("/createuser")
    public ResponseEntity<?> createUser(
            @RequestParam String nome,
            @RequestParam String email,
            @RequestParam String senha,
            @RequestParam Double longitude,
            @RequestParam Double latitude
    ) {
        Usuario user = new Usuario();
        user.setNome(nome);
        user.setEmail(email);
        user.setSenha(senha);
        user.setLongitude(longitude);
        user.setLatitude(latitude);

        userRepository.save(user);

        return ResponseEntity.ok(Map.of("message", "Usuário criado com sucesso"));
    }
}
