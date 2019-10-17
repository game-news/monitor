# Dockerfile-nginx
FROM nginx:latest



# Remove the default config file that
# /etc/nginx/nginx.conf includes
RUN rm /etc/nginx/conf.d/default.conf



# We copy the requirements file in order to install
# Python dependencies
ADD app.conf /etc/nginx/conf.d
ADD ./cert/ /etc/nginx/cert/

# Nginx will listen on this port
EXPOSE 5555