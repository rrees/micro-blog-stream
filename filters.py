import markdown
import bleach

def safe_html(some_markdown):
	#return bleach.clean(markdown.markdown(some_markdown))
	return markdown.markdown(some_markdown)