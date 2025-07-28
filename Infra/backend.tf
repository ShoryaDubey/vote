terraform {
  backend "s3" {
    bucket = "terraformstate1853"
    key    = "dev/terraform.tfstate"
    region = "us-east-1"
  }
}
