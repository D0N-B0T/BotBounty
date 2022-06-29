sudo apt-get update
sudo apt-get upgrade
sudo apt install net-tools
sudo apt-get install python3-pip
sudo apt-get install curl
sudo apt-get install jq
go install -v github.com/projectdiscovery/dnsx/cmd/dnsx@latest
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
go install github.com/lc/gau/v2/cmd/gau@latest
git clone https://github.com/knqyf263/crtsh.git
cd crtsh
go build
mv crtsh ~/go/bin/crtsh
cd
sudo apt-get install golang-go
wget https://git.io/go-installer.sh && sudo bash go-installer.sh
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest
wget https://gitlab.com/api/v4/projects/33695681/packages/generic/nrich/latest/nrich_latest_amd64.deb
 sudo dpkg -i nrich_latest_amd64.deb
sudo apt install -y libpcap-dev
go install -v github.com/projectdiscovery/naabu/v2/cmd/naabu@latest
https://github.com/s0md3v/Arjun.git
python3 setup.py install




