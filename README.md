# Top-news-selectors (tns)

A static HTML site parser for parsing the top story titles and URIs for the following websites:

- https://www.washingtonpost.com/
- http://www.foxnews.com
- http://abcnews.go.com/
- https://www.nytimes.com/
- https://www.usatoday.com/
- https://www.cbsnews.com/
- http://www.chicagotribune.com/
- https://www.nbcnews.com/
- http://www.latimes.com/
- https://www.npr.org/
- https://www.wsj.com/

This parser is built on [Beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) based on the CSS selectors found inside the respective HTML documents.
These selectors were chosen based on the selectors that were present during the 30 days for the month of **November 2016**.

This package has not been tested beyond the month of November 2016, 11/01/2016 - 11/30/2016.
Use at your own risk when going beyond that range.

## Install

This package is available via pip:

```
$ pip install tns
```

## Usage

```python
>>> from tns import SiteParser
>>> html = open('npr.html').read()
>>> parser = SiteParser(html)
>>> parser.npr()
{
'hero_text': "foo",
'hero_link': 'http://bar.com',
'headlines': [{'splash_title': 'baz', 'link': 'http://qux.com'}]
}
>>> parser.washingtonpost()
{'hero_text': '', 'hero_link': '', 'headlines': []}
```

The keys `hero_text` and `hero_link` refer to the top most identified news post, often identified by a enlarged picture or text across the top of the page.
Headlines refer to the subsequent headlines after the hero article, where `splash_title` refers to the title found on the home page of the site not the actual title of the article.

You can see that the second function call with parser, `parser.washingtonpost()`, has zero entries because the document passed to SiteParser was not intended for that parser.

Each of the sites are paired to a function:

```python
"http://abcnews.go.com/":          parser.abcnews()
"https://www.cbsnews.com/":        parser.cbsnews()
"https://www.nbcnews.com/":        parser.nbcnews()
"https://www.washingtonpost.com/": parser.washingtonpost()
"https://www.npr.org/":            parser.npr()
"http://www.latimes.com/":         parser.latimes()
"https://www.usatoday.com/":       parser.usatoday()
"https://www.wsj.com/":            parser.wsj()
"https://www.nytimes.com/":        parser.nytimes()
"http://www.foxnews.com":          parser.foxnews()
"http://www.chicagotribune.com/":  parser.chicagotribune()
```

## Debugging

When the parser fails to find specific headlines or returns no headlines at all, this could be due to:

- Iframes loading content dynamically
- Headlines being injected via Javascript
- The wrong parser is being used for the specified site
