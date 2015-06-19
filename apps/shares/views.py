from django.shortcuts import render_to_response


def root(request):
    return render_to_response('shares/share_list.html', {})