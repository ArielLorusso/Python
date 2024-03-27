# NGINX TUTORIAL
https://www.youtube.com/watch?v=7tGhir27ZJo&list=PLOLrQ9Pn6cawvMA5JjhzoQrnKbYGYQqx1&index=1

# 1 Getting Started with Nginx | Docker | Docker Compose
- [x] Getting started with Docker and Nginx
  - [x] Pull image from Docker
  - [x] Run Nginx container
  - [X] Docker stop container
  - [ ] Verifying your installation
    - [ ] Nginx -v
    - [ ] Docker top web
    - [ ] curl localhost
    - [x] Browser localhost:8080
- [ ] Basic Service management
  - [ ] service nginx start
  - [ ] service nginx stop
  - [ ] Nginx commands
    - [ ] -h
    - [ ] -v -V
    - [ ] -t -T
    - [ ] -s signal
- [ ] Nginx default folder /usr/share/nginx/html
- [ ] Docker-compose file - using volumes
- [ ] Serving custom pages index.html 1
- [ ] Building a new Nginx image
- [ ] DockerFile 

## Install Docker Desktop

### irtualization is Enabled in BIOS/UEFI

Enter BIOS or UEFI settings pressing a key like 
F2, Del, Esc, F10    during the system boot 

Look for an option related to virtualization 
often called Intel VT-x or AMD-V

### Download your systems version pakage

https://docs.docker.com/desktop/install/ubuntu/

```sh
    sudo apt-get update
    sudo apt-get install ./docker-desktop-4.25.1-amd64.deb
```
if it fails to install try the following...

### uninstall

Docker :
```sh
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh --uninstall
```
Docker Desktop :
```sh
    sudo apt-get purge docker-ce docker-ce-cli containerd.io
    sudo rm -rf /var/lib/docker
```
Doker compose :
```sh
    sudo rm /usr/local/bin/docker-compose
```
### Update Docker Repository Configuration:

Install Docker Desktop Dependencies Manually:
If the above steps don't resolve the issue, you can try installing the dependencies manually before installing Docker Desktop. For example:
```sh
    sudo apt-get install docker-ce-cli
```

Open the Docker repository configuration file for editing:

```sh
    sudo nano /etc/apt/sources.list.d/docker.list
```

Check if there is a line like:

```sh
    deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] 
    https://download.docker.com/linux/ubuntu victoria stable
```

If so, change victoria to your actual Ubuntu codename 
For Linux Mint 21.2, which is based on Ubuntu 20.04 (Focal Fossa)

```sh
    deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] 
    https://download.docker.com/linux/ubuntu focal stable
```



### Check Kernel Modules:
Make sure that the necessary kernel modules are loaded. 
Run the following command to check if the kvm module is loaded:
```sh
    lsmod | grep kvm
```

The absence of output when running indicates that 
the kvm kernel  module is not currently loaded.
Desktop relies on hardware virtualization 
To load the kvm module, you can use the following command:
```sh
    sudo modprobe kvm
```

outputs looks like this
kvm                  1032192  0



### Reinstalation should be succesfull

## Create Acount  ( optional )
    email   : ariellorusso
    acount  : ariellorusso@gmail.com


## Pull Nginx image 

https://hub.docker.com/search?q=nginx
https://hub.docker.com/_/nginx

### Nginx Docs

http://nginx.org/en/docs

    COMERCIAL VARIANTS  https://docs.nginx.com/
    https://unit.nginx.org/                         https://www.youtube.com/watch?v=TdzGzXIxJNM&list=PLGz_X9w9raXf3fVkUnWB-g9siSZIIVjYW&index=4
    https://docs.nginx.com/nginx-management-suite   https://www.youtube.com/watch?v=BFFxDPcSl-g&list=PLGz_X9w9raXf48sICkVUs1-j7TVIXkZWv
    https://docs.nginx.com/nginx-amplify/           https://www.youtube.com/watch?v=UT88tFE8naU     
## Run container
```sh
    docker pull nginx
    docker run -it --rm -d -p 8000:80 --name website nginx
    # -it : interactive shel
    # -rm : clean conntainers
    # -d  : demon background process
    # -p  : ports
    # -- name : name/ image
```

TERMINAL OUTPUT :
Digest: sha256:86e53c4c16a6a276b204b0fd3a8143d86547c967dc8258b3d47c3a21bb68d3c6
Status: Downloaded newer image for nginx:latest
7668923432af963a001111cae74a1fbd254be2f226d9865fb12c8f88d4469b4f

DOCKER DESKTOP :
c20060033e06f882b0fbe2db7d974d72e0887a3be5e554efdb0dcf8d53512647

## DOCKER VS_CODE EXTENSION

* The extension :
https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker

* Extension Documentation
https://code.visualstudio.com/docs/containers/overview

## Enter in the browser
```
    http://localhost:8000
```

Should see the folowing :

Welcome to nginx!
If you see this page:
```
    Welcome to nginx!
    If you see this page, the nginx web server is successfully installed 
    and working.  Further configuration is required.
```

## oprionaly use curl 
```sh
    curl localhost:8000
```

and terminal displays the HTML content

<!DOCTYPE html>
<html>
<head>
    <title>Welcome to nginx!</title>
    <style> html { color-scheme: light dark; }  </style>
</head>
<body>
    <h1>Welcome to nginx!</h1>
    <p>If you see this page, the nginx web server is successfully installed and
    working. Further configuration is required.</p>
    <p>For online documentation and support please refer to
    <a href="http://nginx.org/">nginx.org</a>.<br/>
    Commercial support is available at
    <a href="http://nginx.com/">nginx.com</a>.</p>
    <p><em>Thank you for using nginx.</em></p>
</body>
</html>

## Install VS_Code Docker extension

Has 3 windows :     Containers    Images    Regisrties

in the first one we should see the nginx container and its files
right click to Stop / Restart / AtackShell to the container

we will AtackShell
```sh
root@c27a2586dff3:/# nginx -v
nginx_version: nginx/1.25.3
```

We can see all the servicesin the container
```sh
   $ docker top website
ID       PID    PPID     C    STIME  TTY    TIME        CMD
root   17028    17002    0    20:56   ?    00:00:00     nginx: master process nginx -g daemon off;
_rpc   17073    17028    0    20:56   ?    00:00:00     nginx: worker process
_rpc   17074    17028    0    20:56   ?    00:00:00     nginx: worker process
_rpc   17075    17028    0    20:56   ?    00:00:00     nginx: worker process
_rpc   17076    17028    0    20:56   ?    00:00:00     nginx: worker process
```

we can see 4 workers 1 master process
```sh
    root@7668923432af:/# nginx stop 
    nginx: invalid option: "stop"
    root@7668923432af:/# service nginx start
    root@7668923432af:/# service nginx stop 
    * The terminal process "/usr/bin/bash '-c', 'docker exec 
    -it 7668923432af963a001111cae74a1fbd254be2f226d9865fb12c8f88d4469b4f 
    bash'" terminated with exit code: 137. 
```
## RE-RUN
```sh
    docker run -it --rm -d -p 8000:80 --name website nginx
```

    Atach Shell

## NGINX HELP command
```sh
    root@2667229db2a5:/# nginx -h
    nginx version: nginx/1.25.3
    Usage: nginx [-?hvVtTq] [-s signal] [-p prefix]
                [-e filename] [-c filename] [-g directives]
    Options:
    -?,-h         : this help
    -v            : show version and exit
    -V            : show version and configure options then exit
    -t            : test configuration and exit
    -T            : test configuration, dump it and exit
    -q            : suppress non-error messages during configuration testing
    -s signal     : send signal to a master process: stop, quit, reopen, reload
    -p prefix     : set prefix path (default: /etc/nginx/)
    -e filename   : set error log file (default: /var/log/nginx/error.log)
    -c filename   : set configuration file (default: /etc/nginx/nginx.conf)
    -g directives : set global directives out of configuration file
```
## VERSION + CONFIGURATION

```sh
root@2667229db2a5:/# nginx -V   #  VERSION & OPTIONS
nginx version: nginx/1.25.3
built by gcc 12.2.0 (Debian 12.2.0-14) 
built with OpenSSL 3.0.9 30 May 2023 (running with OpenSSL 3.0.11 19 Sep 2023)
TLS SNI support enabled
configure arguments: 
    --prefix=/etc/nginx                                         --sbin-path=/usr/sbin/nginx 
    --modules-path=/usr/lib/nginx/modules                       --conf-path=/etc/nginx/nginx.conf 
    --error-log-path=/var/log/nginx/error.log                   --http-log-path=/var/log/nginx/access.log 
    --pid-path=/var/run/nginx.pid                               --lock-path=/var/run/nginx.lock 
    --http-client-body-temp-path=/var/cache/nginx/client_temp 
    --http-proxy-temp-path=/var/cache/nginx/proxy_temp 
    --http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp 
    --http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp 
    --http-scgi-temp-path=/var/cache/nginx/scgi_temp 
    --user=nginx                    --group=nginx                   --with-compat
    --with-file-aio                 --with-threads                  --with-http_addition_module     
    --with-http_auth_request_module --with-http_dav_module          --with-http_flv_module      
    --with-http_gunzip_module       --with-http_gzip_static_module  --with-http_mp4_module      
    --with-http_random_index_module --with-http_realip_module       --with-http_secure_link_module  
    --with-http_slice_module        --with-http_ssl_module          --with-http_stub_status_module  
    --with-http_sub_module          --with-http_v2_module           --with-http_v3_module           
    --with-mail                     --with-mail_ssl_module          --with-stream                   
    --with-stream_realip_module     --with-stream_ssl_module        --with-stream_ssl_preread_module 
    --with-cc-opt='-g -O2 -ffile-prefix-map=/data/builder/debuild/nginx-1.25.3/debian/debuild-base/nginx-1.25.3=. -fstack-protector-strong -Wformat -Werror=format-security -Wp,-D_FORTIFY_SOURCE=2 -fPIC' --with-ld-opt='-Wl,-z,relro -Wl,-z,now -Wl,--as-needed -pie'
root@2667229db2a5:/# ^C
```
## VALIDATED CONFIG PRINT
```sh
root@2667229db2a5:/# nginx -t  # CONFIG ROUT & STATE
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```

```sh
root@2667229db2a5:/# nginx -T  # CONFIG DUMPT (SHOW FILES)
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```
```conf
# configuration file /etc/nginx/nginx.conf:

user  nginx;
worker_processes  auto;

error_log  /var/log/nginx/error.log notice;
pid        /var/run/nginx.pid;


events {
    worker_connections  1024;
}


http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    keepalive_timeout  65;

    #gzip  on;

    include /etc/nginx/conf.d/*.conf;
}

# configuration file /etc/nginx/mime.types:

types {
    text/html                                        html htm shtml;
    text/css                                         css;
    text/xml                                         xml;
    image/gif                                        gif;
    image/jpeg                                       jpeg jpg;
    application/javascript                           js;
    application/atom+xml                             atom;
    application/rss+xml                              rss;

    text/mathml                                      mml;
    text/plain                                       txt;
    text/vnd.sun.j2me.app-descriptor                 jad;
    text/vnd.wap.wml                                 wml;
    text/x-component                                 htc;

    image/avif                                       avif;
    image/png                                        png;
    image/svg+xml                                    svg svgz;
    image/tiff                                       tif tiff;
    image/vnd.wap.wbmp                               wbmp;
    image/webp                                       webp;
    image/x-icon                                     ico;
    image/x-jng                                      jng;
    image/x-ms-bmp                                   bmp;

    font/woff                                        woff;
    font/woff2                                       woff2;

    application/java-archive                         jar war ear;
    application/json                                 json;
    application/mac-binhex40                         hqx;
    application/msword                               doc;
    application/pdf                                  pdf;
    application/postscript                           ps eps ai;
    application/rtf                                  rtf;
    application/vnd.apple.mpegurl                    m3u8;
    application/vnd.google-earth.kml+xml             kml;
    application/vnd.google-earth.kmz                 kmz;
    application/vnd.ms-excel                         xls;
    application/vnd.ms-fontobject                    eot;
    application/vnd.ms-powerpoint                    ppt;
    application/vnd.oasis.opendocument.graphics      odg;
    application/vnd.oasis.opendocument.presentation  odp;
    application/vnd.oasis.opendocument.spreadsheet   ods;
    application/vnd.oasis.opendocument.text          odt;
    application/vnd.openxmlformats-officedocument.presentationml.presentation
                                                     pptx;
    application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
                                                     xlsx;
    application/vnd.openxmlformats-officedocument.wordprocessingml.document
                                                     docx;
    application/vnd.wap.wmlc                         wmlc;
    application/wasm                                 wasm;
    application/x-7z-compressed                      7z;
    application/x-cocoa                              cco;
    application/x-java-archive-diff                  jardiff;
    application/x-java-jnlp-file                     jnlp;
    application/x-makeself                           run;
    application/x-perl                               pl pm;
    application/x-pilot                              prc pdb;
    application/x-rar-compressed                     rar;
    application/x-redhat-package-manager             rpm;
    application/x-sea                                sea;
    application/x-shockwave-flash                    swf;
    application/x-stuffit                            sit;
    application/x-tcl                                tcl tk;
    application/x-x509-ca-cert                       der pem crt;
    application/x-xpinstall                          xpi;
    application/xhtml+xml                            xhtml;
    application/xspf+xml                             xspf;
    application/zip                                  zip;

    application/octet-stream                         bin exe dll;
    application/octet-stream                         deb;
    application/octet-stream                         dmg;
    application/octet-stream                         iso img;
    application/octet-stream                         msi msp msm;

    audio/midi                                       mid midi kar;
    audio/mpeg                                       mp3;
    audio/ogg                                        ogg;
    audio/x-m4a                                      m4a;
    audio/x-realaudio                                ra;

    video/3gpp                                       3gpp 3gp;
    video/mp2t                                       ts;
    video/mp4                                        mp4;
    video/mpeg                                       mpeg mpg;
    video/quicktime                                  mov;
    video/webm                                       webm;
    video/x-flv                                      flv;
    video/x-m4v                                      m4v;
    video/x-mng                                      mng;
    video/x-ms-asf                                   asx asf;
    video/x-ms-wmv                                   wmv;
    video/x-msvideo                                  avi;
}
```
```py
# configuration file /etc/nginx/conf.d/default.conf:
server {
    listen       80;
    listen  [::]:80;
    server_name  localhost;

    #access_log  /va /log/nginx/host.access.log  main;

    location / {                                            # DATA TO SERVE
        root   /usr/share/nginx/html;
        index  index.html index.htm;                        # (welcome to nginx) HTML
    }

    #error_page  404              /404.html;

    # redirect server error pages to the static page /50x.html
    #
    error_page   500 502 503 504  /50x.html;
    location = /50x.html {
        root   /usr/share/nginx/html;
    }

    # proxy the PHP scripts to Apache listening on 127.0.0.1:80
    #
    #location ~ \.php$ {                        
    #    proxy_pass   http://127.0.0.1;
    #}

    # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
    #
    #location ~ \.php$ {
    #    root           html;
    #    fastcgi_pass   127.0.0.1:9000;
    #    fastcgi_index  index.php;
    #    fastcgi_param  SCRIPT_FILENAME  /scripts$fastcgi_script_name;
    #    include        fastcgi_params;
    #}

    # deny access to .htaccess files, if Apache's document root
    # concurs with nginx's one
    #
    #location ~ /\.ht {
    #    deny  all;
    #}
}
```

## NGINX SIGNAL

```sh
root@2667229db2a5:/# nginx -s stop # -s signal : STOP

2023/11/15 12:53:22 [notice] 86#86: signal process started
root@2667229db2a5:/# 
 *  The terminal process "/usr/bin/bash '-c', 'docker exec -it 2667229db2a5caa631ba25ed99623acd2615480f2be800527f046d07198861b0 bash'" terminated with exit code: 137. 
 *  Terminal will be reused by tasks, press any key to close it. 
 ```

## CHANGE THE HTML FILE

1. Go to the container and its files 
2. search path : `/usr/share/nginx/html`
3. Left click on open
4. Edit 
    ```html
    <h1>Welcome to nginx! </h1>
    <p> I CHANGED THE CONTENT :P </p>
    ```
5. See changes in Browser

## Dokerfile & Compose.yml

create 2 files :
* docker-compose.yml    : this will utilize the dokerfile
* Dokerfile 

when we built what specified in the Compose
if will follow the Dockerfile instructions

* create a html directory
  
## MAPPING DEFAULT NGINX FOLDER
```sh
$ docker-compose up

permission denied while trying to connect to the Docker daemon socket at 
unix:///var/run/docker.sock: Get "http://%2Fvar%2Frun%2Fdocker.sock/v1.24/containers/json?all=1&filters=%7B%22label%22%3A%7B%22com.docker.compose.config-hash%22%3Atrue%2C%22com.docker.compose.project%3Dnginx-django%22%3Atrue%7D%7D"
: dial unix /var/run/docker.sock: connect: permission denied
```

### Error PERMISOS

sudo usermod -aG docker $USER
sudo service docker start

sudo chmod 666 /var/run/docker.sock
sudo chmod 660 /var/run/docker.sock

----

docker-compose up -d --build    # FAIL
docker-compose restart nginx

docker-compose --version
docker version
docker info

sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-
$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose

###  TROUBLESHOOTING 

DOCKER APP SUGGESTION :
https://github.com/microsoft/vscode-docker/wiki/Troubleshooting

PREVIOUS INSTALATIONS :
https://hub.docker.com/_/nginx
https://docs.docker.com/desktop/install/ubuntu/

# CON PAOLO 30/11/23
```sh
whereis Dockerfile
docker
docker run nginx:latest 
docker ps       # PROCESS
docker ps -a
docker -h       # HELP
docker ps -a
docker images
docker run nginx:latest -t test # RUN
docker run ubuntu:latest
docker images -a
docker run -it ubuntu bash 
docker images
docker ps -a
docker rmi 018  # Remove Image
docker rm 018
docker rm 0234
docker rm 234
docker rm be1
docker ps -a
history 
```