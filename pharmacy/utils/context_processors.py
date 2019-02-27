def get_context(request):
    context = dict()
    context['site_title'] = "Pharma"
    context["site_title_long"] = "Pharmacy System"
    context["site_author"] = "Jerry Shikanga"
    context["site_description"] = "This is a demo project for the class project."
    return context
