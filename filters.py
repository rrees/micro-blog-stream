import markdown
import bleach

allowed_tags = bleach.ALLOWED_TAGS + ['p', 'h3', 'h4', 'br']

def safe_html(some_markdown):
	return bleach.clean(markdown.markdown(some_markdown), tags=allowed_tags)
	#return markdown.markdown(some_markdown)