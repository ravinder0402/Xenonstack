# internsctl -

## Table of Contents
- [Introduction](#introduction)
- [Synopsis](#synopsis)
- [Options](#options)
- [Commands](#commands)
- [Usage Examples](#usage-examples)


## Introduction

`internsctl` is a command-line tool designed to control and manage intern-related activities within an organization.

## Synopsis

```bash
internsctl [OPTIONS] [COMMAND]
```

## Options

- `--help`: Show help message and exit.
- `--version`: Show the current version of internsctl.

## Commands

- `internsctl --help`
- `internsctl --version`
- `internsctl cpu getinfo`
- `internsctl memory getinfo`
- `internsctl user create <username>`
- `internsctl user list`
- `internsctl user list --sudo-only`
- `internsctl file getinfo <file-name>`
- `internsctl file getinfo [options] <file-name>`

### File Getinfo Options

- `--size, -s`: Show the size of the file.
- `--permissions, -p`: Show file permissions.
- `--owner, -o`: Show file owner.
- `--last-modified, -m`: Show the last modified time of the file.

## Usage Examples

```bash
# Display help
internsctl --help

# Show the version
internsctl --version

# Get CPU information
internsctl cpu getinfo

# Get memory information
internsctl memory getinfo

# Create a new user
internsctl user create john_doe

# List all users
internsctl user list

# List only sudo users
internsctl user list --sudo-only

# Get file information (size, permissions, owner, last modified)
internsctl file getinfo example.txt
internsctl file getinfo --size --permissions example.txt
```