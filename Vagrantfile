$setup = <<SCRIPT
    DEBIAN_FRONTEND=noninteractive apt-get update
SCRIPT

$dependencies = <<SCRIPT
    DEBIAN_FRONTEND=noninteractive apt-get install -y postgresql libpq-dev
    DEBIAN_FRONTEND=noninteractive su - postgres -c 'createuser vagrant -SRD'
    DEBIAN_FRONTEND=noninteractive su - postgres -c 'createdb photo_album'
    DEBIAN_FRONTEND=noninteractive su - postgres -c 'psql -c "GRANT ALL PRIVILEGES ON DATABASE photo_album TO vagrant;"'
    DEBIAN_FRONTEND=noninteractive apt-get install -y python-dev libjpeg-dev zlib1g-dev
    DEBIAN_FRONTEND=noninteractive apt-get install -y python-pip rubygems
    DEBIAN_FRONTEND=noninteractive apt-get install -y cifs-utils
    DEBIAN_FRONTEND=noninteractive apt-get install -y nginx
    DEBIAN_FRONTEND=noninteractive cp /vagrant/nginx.test /etc/nginx/sites-available/photo_album
    DEBIAN_FRONTEND=noninteractive ln -s /etc/nginx/sites-available/photo_album /etc/nginx/sites-enabled/
    DEBIAN_FRONTEND=noninteractive rm /etc/nginx/sites-enabled/default
    DEBIAN_FRONTEND=noninteractive mkdir /media/album
    DEBIAN_FRONTEND=noninteractive echo "//waskiewicz-server/home-media /media/album cifs guest 0 0" >> /etc/fstab
    DEBIAN_FRONTEND=noninteractive mount -a
    DEBIAN_FRONTEND=noninteractive apt-get install -y python-software-properties python g++ make
    DEBIAN_FRONTEND=noninteractive add-apt-repository -y ppa:chris-lea/node.js
    DEBIAN_FRONTEND=noninteractive apt-get update
    DEBIAN_FRONTEND=noninteractive apt-get install -y nodejs
    DEBIAN_FRONTEND=noninteractive sh -c 'cd /vagrant && npm install'
    DEBIAN_FRONTEND=noninteractive pip install -r /vagrant/requirements/local.txt
    DEBIAN_FRONTEND=noninteractive gem install --no-user-install compass -v 0.12.7
    DEBIAN_FRONTEND=noninteractive ln -s /vagrant/node_modules/grunt-cli/bin /home/vagrant/bin
    DEBIAN_FRONTEND=noninteractive service nginx start
    DEBIAN_FRONTEND=noninteractive su - vagrant -c 'python /vagrant/photo_album/manage.py syncdb'
    DEBIAN_FRONTEND=noninteractive su - vagrant -c 'python /vagrant/photo_album/manage.py migrate'
    DEBIAN_FRONTEND=noninteractive su - vagrant -c 'python /vagrant/photo_album/manage.py collectstatic --noinput -l -i sass'
SCRIPT

Vagrant.configure('2') do |config|

    config.vm.box = 'precise64'
    config.vm.box_url = "http://files.vagrantup.com/" + config.vm.box + ".box"

    config.ssh.forward_agent = true
    # Forward the dev server port
    config.vm.network :forwarded_port, host: 8000, guest: 80

    config.vm.provision "shell", inline: $setup
    config.vm.provision "shell", inline: $dependencies
end
