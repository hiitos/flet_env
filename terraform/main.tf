// Configure the terraform google provider
terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      # https://registry.terraform.io/providers/hashicorp/google/latest
      # バージョン指定
      version = "~> 5.0"
    }
  }
}

# プロバイダ設定
provider "google" {
  project = var.project_id # 利用するプロジェクトのIDを設定
  region  = var.region
}

// Push Docker image to Google Container Registry
resource "null_resource" "docker_image_push" {
  provisioner "local-exec" {
    command = <<-EOT
      # Dockerfile が存在するディレクトリに移動
      cd ../app

      # Docker Buildx ビルダーインスタンスを作成（すでに存在しない場合）
      docker buildx create --name builder --use
      
      # マルチアーキテクチャのビルドを開始
      docker buildx build --platform linux/amd64,linux/arm64 \
        -t gcr.io/${var.project_id}/${var.image_name}:latest \
        -f ../app/Dockerfile . --push
      
      # Buildx ビルダーインスタンスを削除（オプション）
      docker buildx rm builder
    EOT
  }

  triggers = {
    always_run = "${timestamp()}"
  }
}

// Create a Google Cloud Run service
resource "google_cloud_run_service" "flet-cloud-run-app" {
  name     = var.project_id
  location = var.region

  template {
    spec {
      containers {
        image = "gcr.io/${var.project_id}/${var.image_name}:latest"
      }
    }
  }

  traffic {
    percent         = 100
    latest_revision = true
  }
}
