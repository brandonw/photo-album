$setup = <<SCRIPT
    DEBIAN_FRONTEND=noninteractive apt-get update
SCRIPT

$dependencies = <<SCRIPT
    DEBIAN_FRONTEND=noninteractive apt-get install -y postgresql libpq-dev
    DEBIAN_FRONTEND=noninteractive apt-get install -y python-dev libjpeg-dev zlib1g-dev
    DEBIAN_FRONTEND=noninteractive apt-get install -y python-pip
    DEBIAN_FRONTEND=noninteractive apt-get install -y python-software-properties python g++ make
    DEBIAN_FRONTEND=noninteractive add-apt-repository -y ppa:chris-lea/node.js
    DEBIAN_FRONTEND=noninteractive apt-get update
    DEBIAN_FRONTEND=noninteractive apt-get install -y nodejs
    DEBIAN_FRONTEND=noninteractive sh -c 'cd /vagrant && npm install'
    DEBIAN_FRONTEND=noninteractive pip install -r /vagrant/requirements/local.txt
    DEBIAN_FRONTEND=noninteractive ln -s /vagrant/node_modules/grunt-cli/bin /home/vagrant/bin
SCRIPT

Vagrant.configure('2') do |config|

    config.vm.box = 'precise64'
    config.vm.box_url = "http://files.vagrantup.com/" + config.vm.box + ".box"

    config.ssh.forward_agent = true
    # Forward the dev server port
    config.vm.network :forwarded_port, host: 8000, guest: 8000

    config.vm.provision "shell", inline: $setup
    config.vm.provision "shell", inline: $dependencies
end
