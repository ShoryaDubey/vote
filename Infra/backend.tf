terraform {
  backend "s3" {
    bucket = "terraformstate1853"
    key    = "dev/"
    region = "us-east-1"
  }
}
