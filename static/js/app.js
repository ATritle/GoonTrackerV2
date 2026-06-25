async function refreshDashboard() {

    const response = await fetch("/api/latest");

    const data = await response.json();

    document.querySelector("#map-name").textContent = data.map;

    document.querySelector("#game-mode").textContent = data.game_mode;

    document.querySelector("#boss").textContent = data.boss;

    document.querySelector("#reporter").textContent = data.reporter;

    document.querySelector("#source").textContent = data.source;

    document.querySelector("#confidence").textContent =
        Math.round(data.confidence * 100) + "%";

    document.querySelector("#report-time").textContent =
        data.report_time;

    document.querySelector("#last-updated").textContent =
        data.last_updated;
}

setInterval(refreshDashboard, 30000);