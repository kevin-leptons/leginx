# LEGINX

HTTP APIs Skeleton for something. Waiting for idea.

# USAGE

Checkout APIs at https://leginx.herokuapp.com/

# DEVELOPMENT

```bash
# some tools for development
apt-get install git python3 curl

# source code
git clone https://github.com/kevin-leptons/leginx
cd leginx

# development environment
./env init
. venv/bin/activate

# run server on background
leginx start &> /dev/null &
[1] 4688

# check api
curl localhost:8080; echo
{"organization": "Leginx org", "name": "Leginx", "headquater": "Ha Noi,
Viet Nam", "license": "MIT License", "version": "0.1.0"}

# stop server
kill %1
```
