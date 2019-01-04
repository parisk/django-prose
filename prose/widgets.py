from django.forms.widgets import Textarea


class DocumentEditor(Textarea):
    template_name = 'prose/forms/widgets/editor.html'

    class Media:
        css = {
            'all': (
                'https://cdnjs.cloudflare.com/ajax/libs/trix/1.0.0/trix.css',
                'prose/editor.css',
            ),
        }
        js = (
            'https://cdnjs.cloudflare.com/ajax/libs/trix/1.0.0/trix.js',
        )
