const map = new ol.Map({
    target: 'map',
    layers: [
        new ol.layer.Tile({
            source: new ol.source.OSM()
        }),
        new ol.layer.Tile({
            source: new ol.source.TileWMS({
                url: 'http://localhost:8080/geoserver/ows',
                serverType: 'geoserver',
                params: {
                    'LAYERS': 'workspace:nome_da_sua_layer',
                    'VERSION': '1.1.1'
                }
            })
        })
    ],
    view: new ol.View({
        center: ol.proj.fromLonLat([0, 0]),
        zoom: 2
    })
});

document.getElementById('userForm').addEventListener('submit', async function (e) {
    e.preventDefault();

    const email = document.getElementById('email').value;
    const senha = document.getElementById('senha').value;

    const formData = new URLSearchParams();
    formData.append('email', email);
    formData.append('senha', senha);

    try {
        const response = await fetch('http://127.0.0.1:8081/api/getuser', {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            const text = await response.text();
            document.getElementById('response').textContent =
                `Erro: ${response.status} - ${text}`;
            return;
        }

        const result = await response.json();
        document.getElementById('response').textContent =
            JSON.stringify(result, null, 2);

        updateMap(result.historico);

    } catch (error) {
        console.error('Erro:', error);
        document.getElementById('response').textContent =
            'Erro ao enviar os dados';
    }
});

function updateMap(historico) {
    if (!historico || historico.length === 0) return;

    const features = historico.map(coord => {
        const point = new ol.Feature({
            geometry: new ol.geom.Point(
                ol.proj.fromLonLat([coord.longitude, coord.latitude])
            )
        });

        point.setStyle(new ol.style.Style({
            image: new ol.style.Circle({
                radius: 6,
                fill: new ol.style.Fill({ color: 'green' }),
                stroke: new ol.style.Stroke({ color: 'green', width: 10 })
            })
        }));

        return point;
    });

    const lineCoords = historico.map(coord =>
        ol.proj.fromLonLat([coord.longitude, coord.latitude])
    );

    const line = new ol.Feature({
        geometry: new ol.geom.LineString(lineCoords)
    });

    line.setStyle(new ol.style.Style({
        stroke: new ol.style.Stroke({
            color: 'green',
            width: 3
        })
    }));

    features.push(line);

    const vectorLayer = new ol.layer.Vector({
        source: new ol.source.Vector({ features })
    });

    map.getLayers().forEach(layer => {
        if (layer instanceof ol.layer.Vector) {
            map.removeLayer(layer);
        }
    });

    map.addLayer(vectorLayer);

    const last = historico[historico.length - 1];
    map.getView().setCenter(
        ol.proj.fromLonLat([last.longitude, last.latitude])
    );
    map.getView().setZoom(20);
}
