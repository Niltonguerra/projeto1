use tokio_cron_scheduler::{JobScheduler, Job};
use crate::jobs;

pub async fn start() {
    eprintln!(">>> Iniciando scheduler");

    let mut scheduler = JobScheduler::new().await.unwrap();
    eprintln!(">>> Scheduler criado");

    let job = Job::new_async("0 * * * * *", |_uuid, _lock| {
        Box::pin(async {
            jobs::ping_api().await;
        })
    }).unwrap();
    eprintln!(">>> Job criado");

    scheduler.add(job).await.unwrap();
    eprintln!(">>> Job adicionado");

    scheduler.start().await.unwrap();
    eprintln!(">>> Scheduler started");

    tokio::signal::unix::signal(tokio::signal::unix::SignalKind::terminate())
        .unwrap()
        .recv()
        .await;

    eprintln!(">>> Sinal recebido");
}