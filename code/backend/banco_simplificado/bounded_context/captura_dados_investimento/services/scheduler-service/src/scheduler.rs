use tokio_cron_scheduler::{JobScheduler, Job};
use crate::jobs;
use tokio::signal;

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

    tokio::select! {
        _ = signal::ctrl_c() => {
            eprintln!(">>> SIGINT recebido");
        }
        _ = async {
            signal::unix::signal(signal::unix::SignalKind::terminate())
                .unwrap()
                .recv()
                .await;
        } => {
            eprintln!(">>> SIGTERM recebido");
        }
    }

    eprintln!(">>> Sinal recebido");
}