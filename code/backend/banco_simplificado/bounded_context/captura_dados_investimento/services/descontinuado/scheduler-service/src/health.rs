use axum::{Router, routing::get};

pub async fn start() {
    eprintln!(">>> health server iniciando na 3501");
    let app = Router::new().route("/health", get(|| async { "ok" }));
    let listener = tokio::net::TcpListener::bind("0.0.0.0:3501").await.unwrap();
    eprintln!(">>> health server ouvindo");
    axum::serve(listener, app).await.unwrap();
}