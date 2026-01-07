package com.api_rastreamento.repository;

import com.api_rastreamento.model.HistoryLocation;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface HistoryLocationRepository extends JpaRepository<HistoryLocation, Long> {
    List<HistoryLocation> findByUsuario_Id(Long id);
}
