# Create the file
cat > hello.py << 'EOF'
print("Hello from GitHub Actions!")
name = "World"
print(f"Hello, {name}!")
print("The script ran successfully!")
EOF

# Stage, commit and push
git add .
git commit -m "Add hello.py script"
git push origin main