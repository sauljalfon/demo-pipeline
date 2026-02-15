variable "credentials" {
  description = "Path to the GCP credentials JSON file"
  default     = "./keys/my_creds.json"
}

variable "project" {
  description = "My GCP project ID"
  default     = "terrademo-487020"
}

variable "region" {
  description = "Project Region"
  default     = "us-central1"
}

variable "location" {
  description = "Project Location"
  default     = "US"
}
