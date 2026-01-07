package com.api_rastreamento.config;

import io.swagger.v3.oas.annotations.OpenAPIDefinition;
import io.swagger.v3.oas.annotations.info.Contact;
import io.swagger.v3.oas.annotations.info.Info;
import org.springframework.context.annotation.Configuration;

@Configuration
@OpenAPIDefinition(
        info = @Info(
                title = "RASTREAMENTO API",
                version = "v1",
                contact = @Contact(
                        name = "Gabriel Andrade",
                        email = "gandradecortez50@gmail.com"
                )
        )
)
public class OpenApiConfiguration {

}