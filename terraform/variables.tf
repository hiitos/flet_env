variable "project_id" {
  description = "The ID of the project in which to create the resources."
  type        = string
}

variable "region" {
  description = "The region in which to create the resources."
  type        = string
  default     = "us-central1"
}

variable "image_name" {
  description = "The name of the Docker image."
  type        = string
}
