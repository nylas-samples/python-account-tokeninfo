# python-return-token_info

This sample will show you to easily return all token information

This will return a dictionary which will contain the follow:
- Created_at
- Scopes
- State 
- Updated_at 

You can follow along step-by-step in our blog post ["How to Send Emails with the Nylas Python SDK"](https://www.nylas.com/blog/how-to-send-emails-with-the-nylas-python-sdk/).

## Setup

### System dependencies

- Python v3.x

### Gather environment variables

You'll need the following values:

```text
ACCESS_TOKEN = ""
CLIENT_ID = ""
CLIENT_SECRET = ""
RECIPIENT_ADDRESS = ""
```

Add the above values to a new `.env` file:

```bash
$ touch .env # Then add your env variables
```

### Install dependencies

```bash
$ pip3 install nylas
```

## Usage

Run the script using the `python3` command:

```bash
$ python3 ReturnAccount.py
```

When this works succesfully you will be able to see all the token information

## Learn more

Visit our [Nylas Python SDK documentation](https://developer.nylas.com/docs/developer-tools/sdk/python-sdk/) to learn more.
...

<br />

## Authors
- @
