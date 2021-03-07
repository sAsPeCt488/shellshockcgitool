# CGI Script ShellShock Exploitation Tool.

# What is Shellshock?
*Shellshock is a critical bug in Bash versions 1.0.3 - 4.3 that can enable an attacker to execute arbitrary commands.
Vulnerable versions of Bash incorrectly execute commands that follow function definitions stored inside environment variables - this can be exploited by an attacker in systems that store user input in environment variables.*

# What is CGI ?
Some web servers (including Apache) support the Common Gateway Interface (CGI) specification which allows CLI programs to be used to generate dynamic pages.
Request information e.g. query parameters, user agent, etc. is stored in environment variables. Standard output from the program is returned to the user as the HTTP response.

## Usage:
python3 shellshock.py

Developed for Symfonos3 Vulhub machine!
