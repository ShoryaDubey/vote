variable "ssh_port" {
    type = number
    default = 22
  
}

variable "server_port" {
  description = "The port the server will use for HTTP requests"
  type        = number
  default     = 80
}