Usefull commands for system info while troubleshooting

screenfetch
neofetch
ifconfig
lshw -cpu
lshw -html > lshw.html

# ohmyposh themes
    https://ohmyposh.dev/docs/themes
    
    powerlevel10    k_rainbow        emodipt-extend    
    ys              blue-owl         wholespace
    velvet          cloud-context    cloud-native-azure
    froczh          montys           avit
    kushal          tokyo           



# Install oh my Posh           https://www.youtube.com/watch?v=2VlleD1Dj-4
        sudo wget  https://github.com/JanDeDobbeleer/oh-my-posh/releases/latest/download/posh-linux-amd64 -O /usr/local/bin/oh-my-posh
        sudo chmod +x /usr/local/bin/oh-my-posh

## Download the themes
        mkdir / poshthemes
        wget https://github.com/JanDeDobbeleer/oh-my-posh/releases/latest/download/themes.zip -O /.poshthemes/themes.zip
        unzip ~/.poshthemes/themes.zip -d ~/.poshthemes
        chmod u+rw ~/.poshthemes/*.json
        Im /.poshthemes/themes.zip

    eval "$(oh-my-posh-init --shell bash --config ~/.poshthemes/.omp.json)"
I
## Setup the fonts
        cd-
        mkdir.fonts
        unzip ~/Descargas/Meslo.zip -d-/fonts/Meslo
        fc-cache-fv

# make it work
Append to bashrc  configuration  a  command to evaluate when inicialized

    ariel/.bashrc:    or  home/.bashrc:                   

    eval "$(oh-my-posh --init --shell bash --config ~/.poshthemes/ARIEL.omp.json)"
