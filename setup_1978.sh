#!/bin/bash

# Create the project root
mkdir -p 1978/{templates,data}

# Create Python module files with boilerplate headers
cat > 1978/main.py <<EOF
# main.py – Entry point for the 1978 vinyl app
def main():
    print("🎶 Welcome to 1978 – The Vinyl Oracle")

if __name__ == "__main__":
    main()
EOF

touch 1978/{library_parser.py,top10_real.py,vinyl_ai.py,starter_kit.py}

# Fill README
cat > 1978/README.md <<EOF
# 1978

The Vinyl Oracle – A Top 10 album generator built with nostalgia and love.
- 🎧 Real Top 10 (based on your Apple Music data)
- 🧠 AI-inferred emotional picks
- 🎁 Printable "Dad-to-Son Vinyl Starter Kit"

Created by AJ Ricardo.
EOF

# Confirm structure
echo "🎉 Project 1978 initialized!"
tree 1978
