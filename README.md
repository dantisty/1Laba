name: env_anaconda
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.11
  - numpy
  - pandas
  - scikit-learn=1.3
  - matplotlib
  - seaborn
  - bottleneck
  - pip
  - pip:
      - dash==3.2.0
      - plotly==6.3.0
      - flask
      - requests
      - blinker
      - click
      - jinja2
