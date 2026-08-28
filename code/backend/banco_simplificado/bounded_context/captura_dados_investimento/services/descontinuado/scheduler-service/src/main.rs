mod scheduler;
mod jobs;
mod health;

#[tokio::main]
async fn main() {
    tracing_subscriber::fmt::init();

    tokio::spawn(health::start());
    scheduler::start().await;
}