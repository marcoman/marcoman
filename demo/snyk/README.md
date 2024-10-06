# Introduction

This is a demonstration of using some of the features availble to me on the free tier.

## Curl example


Given the online resoure, this command should work:

```bash
curl --request GET \
--url "https://api.snyk.io/rest/orgs/{orgId}/projects?version=2024-06-10" \
--header "Content-Type: application/vnd.api+json" \
--header "Authorization: token API_TOKEN"
```

For me, and using envrionment variables, this becomes:

```bash
curl --request GET \
--url "https://api.snyk.io/rest/orgs/${SNYK_ORG_ID}/projects?version=2024-06-10" \
--header "Content-Type: application/vnd.api+json" \
--header "Authorization: token ${SNYK_AUTH_TOKEN}"
```

However, this doesn't work!  The reason is simple.  I don't have API acces when I'm on the free trial.  I'll have to find an alternate solution.  This is what I see:

```bash
curl --request GET \
--url "https://api.snyk.io/rest/orgs/${SNYK_ORG_ID}/projects?version=2024-06-10" \
--header "Content-Type: application/vnd.api+json" \
--header "Authorization: token ${SNYK_AUTH_TOKEN}"

'{"jsonapi":{"version":"1.0"},"errors":[{"status":"401","details":"Unauthorized"}]}'
```

Next, I'll look into web scraping.

## Web scraping.  

I'll use python and beautiful soup to scrape the website.  I believe the first test is to ensure I can authenticate from my python application and read a page.


