from django.shortcuts import render
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from .forms import SignUpForm
from django.views import generic


def add_signup(request):
    # Get the context from the request.
    context = RequestContext(request)

    # A HTTP POST?
    if request.method == 'POST':
        form = SignUpForm(request.POST or None)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)
            #post_save.connect(send_update, sender=Book)
            # Now call the index() view.
            # The user will be shown the homepage.
            return redirect('/thanks/')
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = SignUpForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render_to_response('add_signup.html', {'form': form}, context)


class ThanksPage(generic.TemplateView):
    template_name = "thanks.html"