resource "aws_key_pair" "maxkeypair" {
  key_name   = "maxtacu"
  public_key = file("./keys/maxtacu.pub")
  lifecycle {
    ignore_changes = [public_key]
  }
}

