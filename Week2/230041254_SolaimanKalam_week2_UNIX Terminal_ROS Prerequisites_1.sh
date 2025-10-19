mkdir -p ~/logs
sudo find /root -type f -name "*log*" -exec mv {} ~/logs/ \;
sudo chown -R $USER:$USER ~/logs/