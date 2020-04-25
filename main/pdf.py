def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html  = template.render(context)
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode('utf-8')), result, show_error_as_pdf=True, encoding='UTF-8')
    if not pdf.err:
        return result.getvalue()
    return False
pdf = render_to_pdf('article_pdf.html', {
    'article': article,
    'MEDIA_ROOT': settings.MEDIA_ROOT,
})

if pdf:
    pdf_file = open("%s/%s.pdf" % (settings.ARTICLE_PDF_PATH, article.slug), 'w').write(pdf)