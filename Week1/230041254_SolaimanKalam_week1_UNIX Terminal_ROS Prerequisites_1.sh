#!/bin/bash

mkdir -p ~/altair_software_recruitment/executables
cat > ~/altair_software_recruitment/executables/hello_altair.py << 'EOF'
#!/usr/bin/env python3
print("Hello Altair!")
EOF

# Only root permission
sudo chmod 700 ~/altair_software_recruitment/executables/hello_altair.py
sudo chown root:root ~/altair_software_recruitment/executables/hello_altair.py
