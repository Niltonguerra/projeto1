# builder
FROM rust:1.86 AS builder
WORKDIR /app
COPY Cargo.toml Cargo.lock ./
RUN mkdir src && echo "fn main() {}" > src/main.rs
RUN cargo build --release
RUN rm -rf src
COPY src ./src
RUN touch src/main.rs && cargo build --release

# produção
FROM debian:bookworm-slim AS production
WORKDIR /app
RUN apt-get update && apt-get install -y \
    ca-certificates \
    libssl3 \
    && rm -rf /var/lib/apt/lists/*
COPY --from=builder /app/target/release/scheduler-service .
EXPOSE 3501
CMD ["./scheduler-service"]

# desenvolvimento
FROM rust:1.86 AS development
WORKDIR /app
COPY . .
CMD ["cargo", "run"]