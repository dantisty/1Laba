cat > environment.yml << 'EOF'
name: env_anaconda
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.11
  - numpy
  - scikit-learn
  - matplotlib
  - seaborn  
  - pandas
  - bottleneck
  - pip
  - pip:
    - dash
EOF
