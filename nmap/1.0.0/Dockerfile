# Base our app image off of the WALKOFF App SDK image
FROM peterclemenko/shuffle:app_sdk_kali as base

# We're going to stage away all of the bloat from the build tools so lets create a builder stage
FROM base as builder

# Update the list of packages
RUN apt-get update
# Install pre-requisite packages.
RUN apt-get install -y wget apt-transport-https software-properties-common sudo nmap
# Start PowerShell
#RUN pwsh

# Install all of our pip packages in a single directory that we can copy to our base image later
#RUN mkdir /install
WORKDIR /install
COPY requirements.txt /requirements.txt
RUN pip install --prefix="/install" -r /requirements.txt

# Switch back to our base image and copy in all of our built packages and source code
FROM base
COPY --from=builder /install /usr/local
COPY src /app

# Update the list of packages
RUN apt-get update
# Install pre-requisite packages.
RUN apt-get install -y wget apt-transport-https software-properties-common sudo nmap
# Start PowerShell
#RUN pwsh
# Install any binary dependencies needed in our final image
# RUN apk --no-cache add --update my_binary_dependency
#RUN mkdir /install
WORKDIR /install
COPY requirements.txt /requirements.txt
RUN pip install --prefix="/install" -r /requirements.txt

# Finally, lets run our app!
WORKDIR /app
CMD python3 app.py --log-level DEBUG
