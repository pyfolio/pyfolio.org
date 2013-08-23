"""
    Folio website.
"""

from folio import Folio

__version__ = '0.3'

proj = Folio(__name__, extensions=['themes'],
             jinja_extensions=['jinja2_highlight.HighlightExtension'])

proj.config.update({
    'THEME': 'folio',
})

@proj.context('*.html')
def version(env):
    return {'version': __version__}

def debug():
    import logging

    # Print DEBUG messages to STDOUT.
    proj.logger.addHandler(logging.StreamHandler())
    proj.logger.setLevel(logging.DEBUG)

    # Change DEBUG config option.
    proj.config['DEBUG'] = True

if __name__ == '__main__':
    debug()
    proj.build()
