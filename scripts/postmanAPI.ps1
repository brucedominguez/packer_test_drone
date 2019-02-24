# Install Chocolatey
iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
# Globally Auto confirm every action
choco feature enable -n allowGlobalConfirmation

# Install Python 2.x 2.7.15
choco install python2

# Install NodeJs
choco install nodejs.install

# Install Postman
choco install postman

# Install Microsoft Visual Studio 2013 Express
choco install visualstudio2013expressweb
