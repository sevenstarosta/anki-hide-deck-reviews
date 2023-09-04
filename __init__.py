#from aqt.deckbrowser import DeckBrowser
import re
from aqt import gui_hooks

def replace_review_table_spans(html:str, klass: str) -> str:
    pattern = re.compile(r'<span class="' + re.escape(klass) + r'">[1-9]+[0-9]*</span>')
    return re.sub(pattern, f'<span class="{klass}">?</span>', html)

def update_deck_review_counts(browser, content):
    content.tree = replace_review_table_spans(content.tree, klass='learn-count')
    content.tree = replace_review_table_spans(content.tree, klass='review-count')

gui_hooks.deck_browser_will_render_content.append(update_deck_review_counts)