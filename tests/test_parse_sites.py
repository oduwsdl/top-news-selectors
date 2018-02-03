from tns import SiteParser
import os


def test_parse_site():
    """
    Samples taken from:
    http://web.archive.org/web/20161101010000if_/{NEWS-URI}
    The first day of November 2016 at 1AM GMT
    """
    sample_dir = os.path.dirname(__file__) + '/samples/'
    for f in os.listdir(sample_dir):
        if f.endswith('.html'):
            filename = os.path.join(sample_dir, f)
            html = open(filename).read()
            parser = SiteParser(html)
            method_name = f[:-5]
            # filename convert to method call
            result = getattr(parser, method_name)()
            # There is no selector to discern headline from hero
            # story on day 01
            if method_name != "washingtonpost":
                assert len(result["hero_text"]) > 0
                assert len(result["hero_link"]) > 0
                assert len(result["headlines"]) >= 3
            else:
                assert len(result["headlines"]) >= 3
