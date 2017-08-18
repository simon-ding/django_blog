from django import forms
from django.utils.safestring import mark_safe


class SimpleMDE(forms.Textarea):
    class Media:
        js = (
            'https://cdn.jsdelivr.net/simplemde/latest/simplemde.min.js',
        )
        css = {
           'all': ('https://cdn.jsdelivr.net/simplemde/latest/simplemde.min.css',)
        }

    def __init__(self, attrs={'id':'textarea_id'}):
        self.attrs = attrs
        super(self.__class__, self).__init__(self.attrs)

    def render(self, name, value, attrs=None, renderer=None):
        rendered = super(self.__class__, self).render(name, value, attrs=None, renderer=None)
        return rendered + mark_safe("""<script>
            var simplemde = new SimpleMDE({{ element: document.getElementById('{0}'), 	renderingConfig: {{singleLineBreaks: false}} }});
            </script>""".format(self.attrs.get('id'))
            )