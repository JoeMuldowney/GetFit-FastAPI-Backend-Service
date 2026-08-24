resource "digitalocean_droplet" "getfit-droplet-01" {
  image  = "ubuntu-24-04-x64"
  name   = "getfit-droplet-01"
  region = "nyc1"
  size   = "s-1vcpu-1gb"


  tags = [
    "demo-projects"
  ]

  ssh_keys = [
    data.digitalocean_ssh_key.terraform.id
  ]
}