# Base our app image off of the WALKOFF App SDK image
FROM frikky/shuffle:app_sdk_ubuntu as base

# We're going to stage away all of the bloat from the build tools so lets create a builder stage
FROM base as builder



# Update the list of packages
RUN sudo apt-get update
# Install pre-requisite packages.
RUN sudo apt-get install -y wget apt-transport-https software-properties-common
# Download the Microsoft repository GPG keys
RUN wget -q "https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/packages-microsoft-prod.deb"
# Register the Microsoft repository GPG keys
RUN sudo dpkg -i packages-microsoft-prod.deb
# Update the list of packages after we added packages.microsoft.com
RUN sudo apt-get update
# Install PowerShell
RUN sudo apt-get install -y powershell
# Start PowerShell
#RUN pwsh

# Install all of our pip packages in a single directory that we can copy to our base image later
RUN mkdir /install
WORKDIR /install
COPY requirements.txt /requirements.txt
RUN pip install --prefix="/install" -r /requirements.txt

# Switch back to our base image and copy in all of our built packages and source code
FROM base
COPY --from=builder /install /usr/local
COPY src /app

# Install any binary dependencies needed in our final image
# RUN apk --no-cache add --update my_binary_dependency

# Finally, lets run our app!
WORKDIR /app
CMD python app.py --log-level DEBUG
