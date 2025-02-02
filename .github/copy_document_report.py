name: google gocument copy



# on:
#   schedule:
#     - cron: '0 0 1 * *'

on:
  push:
    branches:
      - master

jobs:
  copy_google_doc:
    runs-on: ubuntu-latest

    steps:
      - name: checkout repo
        uses: actions/checkout@v4

      - name: setup python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: install packages for work
        run: pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client

      - name: save credential
        run: echo '${{ secrets.GOOGLE_CREDENTIALS }}' > credentials.json

      - name: execute to copy Google Document
        run: python copy_document_report.py