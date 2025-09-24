pip install build pytest
python -m build            # creates dist/*.whl and *.tar.gz
pip install -e .           # editable install for dev
pytest
