pub async fn ping_api() {
    let url = "https://sua-api.com/health";

    match reqwest::get(url).await {
        Ok(res) => {
            tracing::info!(status = %res.status(), url, "Job executado");
        }
        Err(err) => {
            tracing::error!(error = %err, url, "Falha ao chamar endpoint");
        }
    }
}