# Introduction
This tool requires the environment and the installation will be listed below, the installation includes for MacOS and Windows. Specifically, it needs to be installed to run the tool:
- Findomain
- Subfinder
- Httpx
- Amass
- Acunetix
- Typer
# Installation

- Findomain


   1. Windows

        Download the binary from 
    
         https://github.com/findomain/findomain/releases/latest/download/findomain-windows.exe.zip
  
        Open a CMD shell and go to the dir where findomain.exe was downloaded. 
           Exec: findomain.exe --help in the CMD shell.

        


   2. MacOS
  
        You have two options to install Findomain in MacOS.

        Using Homebrew:
       ```sh
        $ brew install findomain
        $ findomain
        ```
      Manually from the repo:
       ```sh
        $ curl -LO https://github.com/findomain/findomain/releases/latest/download/findomain-osx.zip
        # Extract the ZIP file.
        $ chmod +x findomain.dms
        $ ./findomain.dms --help
      ```
      

- Subfinder

    This tool can install windows and macos, but need install go

    `subfinder` requires go1.19 to install successfully. Run the following command to install the latest version:
    ```sh
    go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
    ```
  
- Httpx

    This tool can install windows and macos, but need install go

  `httpx` requires **go1.19** to install successfully. Run the following command to get the repo:

    ```sh
    go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
    ```
- Amass

    This tool can install windows and macos, but need install go
       
     `amass` requires **go1.19** to install successfully. 
    ```sh
    go install -v github.com/owasp-amass/amass/v3/...@master
    ```
  
- Acunetix
      
     `acunetix` requires with docker. Install docker and run the following link.
      
    https://hub.docker.com/r/secfa/docker-awvs



- Typer

    Need to install python or python3 from MacOS or windows

    ```sh
    pip install typer
    ```
    or
    ```sh
    pip3 install typer
    ```
