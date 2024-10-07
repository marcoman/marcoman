# Introduction

This is a demonstration of using some of the features availble to me on the free tier.

So I learned a few things.  I don't have permissions to do API work, and it is hard to do web scraping when a site requires you to authenticate via Google OAuth.

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

This one didn't work too good.  😒

I'll use python and beautiful soup to scrape the website.  I believe the first test is to ensure I can authenticate from my python application and read a page.

Okay, I had to push the pause button on this one because while I could get my python app to authenticate, I wasn't able to get my credentials to pass over correctly to sign onto the snyk website for scraping.

THIS MAY NOT BE ALLOWED.

I did follow the docs and I learned a few things along the way.
- Best to use the API, rather than scrape.
- If we wish to sign on, we should have an understanding of these  types of resources.
    - Google Cloud console, to generate OAUTH credentials.
    - Google Cloud console, to add our redirect URL to the credential.  This one was a PITA for me as a developer, because I had to update the URL list just about every time I ran my application and my localhost URL changed.  (maybe I can specify the port?).  I could get into a valid authentication flow, but my endpoint would 401.
    - I was reminded to keep my client-secret.json file separate from my code.  I only kept it in my home directory.
    - I was reminded to keep using environment variables to specify interesting details, such as my tokens and endpoints.

For fun, I downloaded the page as a file, but alas our page is partly rendered by javascript.  That means downloading a page doesn't work.