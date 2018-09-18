# MicroServices-API
## Usage
`python3 -m api.v1.app`

### API Example
`http://0.0.0.0:5000/api/v1/convert?from=USD&to=JPY&amt=25`

### Example Output

    "result": 2804.3525

    "info": {

        "rate": 112.1741,
        "timestamp": "2018-09-18 19:35:51.074000"
    },

    "query": {

        "amount": "25",
        "from": "USD",
        "to": "JPY"
    }
