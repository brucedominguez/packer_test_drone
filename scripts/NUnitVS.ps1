# Install Chocolatey
iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
# Globally Auto confirm every action
choco feature enable -n allowGlobalConfirmation

# Install .net 4.7.2
choco install netfx-4.7.2-devpack

# Install build tools 2015
choco install microsoft-build-tools

# Install Microsoft Visual Studio Professional 2017
choco install visualstudio2017professional

# Install JDK 8
choco install jdk8

# Install nunit
choco install nuget.commandline
choco install nunit-console-runner
choco install nunit-extension-nunit-v2-result-writer
choco install nunit-extension-vs-project-loader



