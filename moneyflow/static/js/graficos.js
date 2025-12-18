function criarGraficoPizza(elementId, labels, data) {
    const ctx = document.getElementById(elementId);
    if (!ctx) return;

    new Chart(ctx, {
        type: "pie",
        data: {
            labels: labels,
            datasets: [{
                data: data,
                borderWidth: 1
            }]
        }
    });
}

function criarGraficoLinha(elementId, labels, data, label) {
    const ctx = document.getElementById(elementId);
    if (!ctx) return;

    new Chart(ctx, {
        type: "line",
        data: {
            labels: labels,
            datasets: [{
                label: label,
                data: data,
                borderWidth: 2,
                tension: 0.3
            }]
        }
    });
}