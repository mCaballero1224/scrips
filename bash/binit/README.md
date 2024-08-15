# Binit

Binit takes your program, and throws it in the bin. Specifically, it copies a file to `/usr/local/bin`, but you're more than welcome to put it somewhere else by changing the script.

## Installation

Download the script

```
sudo curl -L https://raw.githubusercontent.com/mCaballero1224/scripts/main/bash/binit/binit -o /usr/local/bin/binit
```

Make the script executable

```
chmod +x /usr/local/bin/binit
```

## Usage

Run the script like you would any program, giving it the file you'd like to place in the binary directory.

```
binit /home/mCaballero1224/Development/some_project/some_executable
```
