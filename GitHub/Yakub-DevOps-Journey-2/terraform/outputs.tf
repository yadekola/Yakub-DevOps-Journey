output "app_public_ip" {
  description = "Public IP of the app instance"
  value       = aws_instance.app.public_ip
}

output "app_instance_id" {
  value = aws_instance.app.id
}

output "ssh_command" {
  description = "Copy-paste to connect"
  value       = "ssh -i ~/.ssh/${var.key_name}.pem ubuntu@${aws_instance.app.public_ip}"
}
