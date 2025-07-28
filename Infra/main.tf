data "aws_vpc" "default" {
  default = true
}

data "aws_subnets" "default" {
  filter {
    name   = "vpc-id"
    values = [data.aws_vpc.default.id]
  }
  
}
resource "aws_security_group" "instance_sg" {
  name_prefix = "instance-sg"
  vpc_id      = data.aws_vpc.default.id

  ingress {
    from_port   = var.server_port
    to_port     = var.server_port
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
  from_port   = var.ssh_port
  to_port     = var.ssh_port
  protocol    = "tcp"
  cidr_blocks = [data.vault_generic_secret.example.data["dev"]]
  }


    egress {
        from_port   = 0
        to_port     = 0
        protocol    = "-1"
        cidr_blocks = ["0.0.0.0/0"]
    }
}


resource "aws_instance" "web" {
  ami           = "ami-020cba7c55df1f615"
  instance_type = "t2.micro"
  key_name = "testing-key.pem"

  tags = {
    Name = "clucter"
  }
}