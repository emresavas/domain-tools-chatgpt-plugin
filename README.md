# Domain Tools Plugin
A plugin that allows the user to query whois and DNS records using ChatGPT.

## Requirements
- Python 3.6 or higher
- An APILayer API key. [Create Free APILayer Account](https://apilayer.com/)

## Dependencies
- requests
- flask

## API Endpoints
### [GET] /whois/{domain}
Get Whois records for a domain

#### URL Params:
- `domain` - Domain name to be used in query (required)

#### Success Response:
```
{
   "result":{
      "domain_name":"EMRESAVAS.COM",
      "registrar":"Google LLC",
      "whois_server":"whois.google.com",
      "referral_url":null,
      "updated_date":"2022-07-28 19:43:50",
      "creation_date":"2007-08-07 14:44:42",
      "expiration_date":"2031-08-07 14:44:42",
      "name_servers":[
         "IGOR.NS.CLOUDFLARE.COM",
         "ROXY.NS.CLOUDFLARE.COM"
      ],
      "status":"clientTransferProhibited https://icann.org/epp#clientTransferProhibited",
      "emails":"registrar-abuse@google.com",
      "dnssec":"unsigned",
      "name":null,
      "org":null,
      "address":null,
      "city":null,
      "state":null,
      "zipcode":null,
      "country":null
   }
}
```

### [GET] /dns/{record}/{domain}
Get Whois records for a domain

#### URL Params:
- `record` - Record type like A, MX, NS, or SOA, etc. (required)
- `domain` - Domain name to be used in query (required)

#### Success Response:
```
{
  "results": [
    {
      "ipAddress": "188.114.96.2"
    },
    {
      "ipAddress": "188.114.97.2"
    }
  ],
  "processResponseTime": "35ms",
  "domain": "emresavas.com",
  "requestType": "A",
  "warnings": []
}
```

## Install on ChatGPT
More details on [ChatGPT Plugins Docs](https://platform.openai.com/docs/plugins/introduction)
