# cleardimage

This script grabs all docker images and deletes them. This also stops any containers using these images. The scripts creates an array of image IDs then iterates through that array to delete them using the docker cli comands.

## Motivation

I've been trying to use Dockerhub more often, so I'm trying not to be cluttered by having a bunch of images/containers locally that I don't use. This is just incase I do end up cluttered any way and need a quick method to clean things up. 
