package com.api_rastreamento.controller;

import com.api_rastreamento.service.UsuarioService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import java.util.Map;

// para testes
@CrossOrigin(origins = "*")
@RestController
@RequestMapping("/api")
public class UsuarioController {

    private final UsuarioService service;

    public UsuarioController(UsuarioService service) {
        this.service = service;
    }

    @PostMapping("/historylocation")
    public ResponseEntity<?> getHistory(@RequestParam String email, @RequestParam String senha) {
        Map<String, Object> response = service.getHistory(email, senha);
        return ResponseEntity.ok(response);
    }

    @PostMapping("/getuser")
    public ResponseEntity<?> getUser(@RequestParam String email, @RequestParam String senha) {
        Map<String, Object> response = service.getUser(email, senha);
        return ResponseEntity.ok(response);
    }

    @PostMapping("/createuser")
    public ResponseEntity<?> createUser(@RequestParam String nome, @RequestParam String email, @RequestParam String senha,
                                        @RequestParam Double longitude, @RequestParam Double latitude) {
        service.createUser(nome, email, senha, longitude, latitude);
        return ResponseEntity.ok(Map.of("message", "Usuário criado"));
    }
}
