Managing Certbot certificates is often an underlooked operation since Certbot handles cert renewal automatically using a cronjob, so no worries there. But, what if we want to list which certificates are already installed, or we want to remove some of them properly. Today’s topic is all about listing, renewing and removing Certbot certificates.

Prerequisites
Web server
Certbot
sudo privileges
Renew certificates

Step 1. List certificates.

    sudo certbot certificates
    
Step 2. Renew a single certificate.

    sudo certbot renew --cert-name <insert_cert_name_listed_from_step_1_here>
    
Note(s): You could also add --dry-run at the end of the renew command just to make sure you know what you are doing.

Step 3. Finally, restart the web server Nginx/Apache, whatever you are using Certbot with.

    sudo systemctl restart nginx
    
or,

    sudo systemctl restart httpd
    
Delete certificates
Step 1. Basically, the same step as Step 1 in Renew certificates section.

    sudo certbot certificates
    
Step 2. Delete a single certificate.

    sudo certbot delete --cert-name <insert_cert_name_listed_from_step_1_here>

If you want to remove it in a more interactive way:

    sudo certbot delete
    
Step 3. Don’t forget to remove the Certbot generated web server’s configuration leftover lines for the related/unwanted domain. The configuration block looks something like the following:


    server {
        server_name test.com;
        ...

        listen 443 ssl; # managed by Certbot
        ssl_certificate /etc/letsencrypt/live/test.com/fullchain.pem; # managed by Certbot
        ssl_certificate_key /etc/letsencrypt/live/test.com/privkey.pem; # managed by Certbot
        include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
        ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot
    }


