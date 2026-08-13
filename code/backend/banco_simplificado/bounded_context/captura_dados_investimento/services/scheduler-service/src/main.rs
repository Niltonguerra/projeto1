mod scheduler;
mod jobs;

#[tokio::main]
async fn main() {
    tracing_subscriber::fmt::init();
    scheduler::start().await;
}